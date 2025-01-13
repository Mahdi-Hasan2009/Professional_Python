from flask import Flask, render_template_string, send_from_directory, request, jsonify
import os
import time
from datetime import datetime
import json
from nbconvert import HTMLExporter
from nbformat import read
from nbformat import NO_CONVERT
from traitlets.config import Config

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Advanced File Viewer</title>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <style>
        :root[data-theme="light"] {
            --primary-gradient: linear-gradient(135deg, #FF6B6B, #4ECDC4);
            --secondary-gradient: linear-gradient(135deg, #A8E6CF, #DCEDC1);
            --background-color: #f4f7fc;
            --card-background: #ffffff;
            --text-color: #34495e;
            --border-color: #dcdde1;
            --hover-color: #f1f3f5;
            --shadow: 0 4px 8px rgba(0,0,0,0.1);
            --icon-color: #FF6B6B;
            --meta-color: #7f8c8d;
        }

        :root[data-theme="dark"] {
            --primary-gradient: linear-gradient(135deg, #FF6B6B, #4ECDC4);
            --secondary-gradient: linear-gradient(135deg, #2C3E50, #3498DB);
            --background-color: #1a1a1a;
            --card-background: #2d2d2d;
            --text-color: #ecf0f1;
            --border-color: #404040;
            --hover-color: #363636;
            --shadow: 0 4px 8px rgba(0,0,0,0.3);
            --icon-color: #4ECDC4;
            --meta-color: #bdc3c7;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: "Poppins", sans-serif;
            transition: background-color 0.3s ease, color 0.3s ease;
        }

        body {
            background: var(--background-color);
            color: var(--text-color);
            line-height: 1.6;
            padding: 1rem 0;
        }

        .header {
            background: var(--primary-gradient);
            color: white;
            padding: 2rem 1.5rem;
            text-align: center;
            position: relative;
        }

        .theme-toggle {
            position: absolute;
            right: 2rem;
            top: 50%;
            transform: translateY(-50%);
            background: transparent;
            border: none;
            color: white;
            font-size: 1.5rem;
            cursor: pointer;
            padding: 0.5rem;
            border-radius: 50%;
            transition: background-color 0.3s ease;
        }

        .theme-toggle:hover {
            background: rgba(255, 255, 255, 0.2);
        }

        .search-container {
            max-width: 1200px;
            margin: 1.5rem auto;
            padding: 0 2rem;
            display: flex;
            justify-content: center;
        }

        .search-box {
            width: 80%;
            max-width: 800px;
            padding: 0.8rem 1.2rem;
            border: 2px solid var(--border-color);
            border-radius: 25px;
            font-size: 1.1rem;
            background-color: var(--card-background);
            color: var(--text-color);
            box-shadow: var(--shadow);
            transition: all 0.3s ease;
        }

        .search-box:focus {
            outline: none;
            border-color: #4ECDC4;
            box-shadow: 0 0 8px rgba(78, 205, 196, 0.5);
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 1rem 2rem;
        }

        .grid-container {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 1.5rem;
            padding: 1rem 0;
        }

        .card {
            background: var(--card-background);
            border-radius: 15px;
            box-shadow: var(--shadow);
            overflow: hidden;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
        }

        .card-content {
            padding: 1.5rem;
        }

        .card-header {
            display: flex;
            align-items: center;
            margin-bottom: 0.75rem;
        }

        .card-icon {
            font-size: 2rem;
            margin-right: 1rem;
            color: var(--icon-color);
        }

        .card-title {
            flex-grow: 1;
            font-size: 1.2rem;
            font-weight: 600;
            color: var(--text-color);
            text-decoration: none;
            word-break: break-word;
            transition: color 0.3s ease;
        }

        .card-title:hover {
            color: var(--icon-color);
        }

        .card-meta {
            font-size: 0.9rem;
            color: var(--meta-color);
            margin-top: 0.5rem;
        }

        .breadcrumb {
            padding: 1rem;
            background: var(--card-background);
            border-radius: 8px;
            margin-bottom: 1rem;
            box-shadow: var(--shadow);
        }

        .breadcrumb a {
            color: var(--icon-color);
            text-decoration: none;
            font-weight: 600;
            transition: color 0.3s ease;
        }

        .breadcrumb a:hover {
            opacity: 0.8;
        }

        .jupyter-notebook {
            border-left: 4px solid #F37626;
        }

        .jupyter-icon {
            color: #F37626 !important;
        }

        @media (max-width: 768px) {
            .grid-container {
                grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
            }
            .container {
                padding: 1rem;
            }
            .theme-toggle {
                right: 1rem;
            }
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>Advanced File Viewer</h1>
        <button class="theme-toggle" id="themeToggle">
            <i class="fas fa-moon"></i>
        </button>
    </div>
    
    <div class="search-container">
        <input type="text" 
               class="search-box" 
               placeholder="Search files and folders..." 
               id="searchInput"
               autocomplete="off">
    </div>

    <div class="container">
        <div class="breadcrumb">
            <a href="/"><i class="fas fa-home"></i></a> /
            {% for part in breadcrumbs %}
                <a href="{{ part.path }}">{{ part.name }}</a>
                {% if not loop.last %} / {% endif %}
            {% endfor %}
        </div>

        <div class="grid-container" id="fileGrid">
            {% for item in items %}
            <div class="card {% if item.name.endswith('.ipynb') %}jupyter-notebook{% endif %}" data-name="{{ item.name.lower() }}">
                <div class="card-content">
                    <div class="card-header">
                        {% if item.is_dir %}
                            <i class="card-icon fas fa-folder"></i>
                        {% elif item.name.endswith('.ipynb') %}
                            <i class="card-icon fab fa-python jupyter-icon"></i>
                        {% else %}
                            <i class="card-icon fas fa-file"></i>
                        {% endif %}
                        <a href="{{ item.path }}" class="card-title">{{ item.name }}</a>
                    </div>
                    <div class="card-meta">
                        <i class="fas fa-clock"></i> {{ item.modified_time }}
                    </div>
                </div>
            </div>
            {% endfor %}
        </div>
    </div>

    <script>
        // Theme Toggle
        const themeToggle = document.getElementById('themeToggle');
        const html = document.documentElement;
        const toggleIcon = themeToggle.querySelector('i');

        // Check for saved theme preference
        const savedTheme = localStorage.getItem('theme') || 'light';
        html.setAttribute('data-theme', savedTheme);
        updateThemeIcon(savedTheme);

        themeToggle.addEventListener('click', () => {
            const currentTheme = html.getAttribute('data-theme');
            const newTheme = currentTheme === 'light' ? 'dark' : 'light';
            
            html.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
            updateThemeIcon(newTheme);
        });

        function updateThemeIcon(theme) {
            toggleIcon.className = theme === 'light' ? 'fas fa-moon' : 'fas fa-sun';
        }

        // Search functionality
        const searchInput = document.getElementById('searchInput');
        const fileGrid = document.getElementById('fileGrid');
        const cards = fileGrid.getElementsByClassName('card');

        searchInput.addEventListener('input', function(e) {
            const searchTerm = e.target.value.toLowerCase();
            let hasVisibleCards = false;

            Array.from(cards).forEach(card => {
                const fileName = card.dataset.name;
                const isMatch = fileName.includes(searchTerm);
                card.style.display = isMatch ? '' : 'none';
                if (isMatch) hasVisibleCards = true;
            });

            const existingNoResults = fileGrid.querySelector('.no-results');
            if (!hasVisibleCards && !existingNoResults) {
                const noResults = document.createElement('div');
                noResults.className = 'no-results';
                noResults.innerHTML = '<i class="fas fa-search"></i> No matching files or folders found';
                fileGrid.appendChild(noResults);
            } else if (hasVisibleCards && existingNoResults) {
                existingNoResults.remove();
            }
        });
    </script>
</body>
</html>
"""


def get_breadcrumbs(path):
    """Generate breadcrumbs for navigation."""
    parts = path.split('/')
    breadcrumbs = []
    for i in range(len(parts)):
        breadcrumb_path = '/'.join(parts[:i + 1])
        breadcrumbs.append({'name': parts[i], 'path': '/' + breadcrumb_path})
    return breadcrumbs

def get_file_info(path, base_path):
    """Retrieve file metadata."""
    full_path = os.path.normpath(os.path.join(base_path, path))
    stats = os.stat(full_path)
    return {
        'name': os.path.basename(path),
        'path': '/' + path.replace(os.sep, '/'),
        'is_dir': os.path.isdir(full_path),
        'modified_time': datetime.fromtimestamp(stats.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
    }

@app.route('/')
@app.route('/<path:subpath>')
def index(subpath=''):
    """Main route to handle file navigation and rendering."""
    base_path = os.path.abspath('.')
    current_path = os.path.normpath(os.path.join(base_path, subpath))

    if not os.path.exists(current_path):
        return "Path not found", 404

    if os.path.isfile(current_path):
        if current_path.endswith('.ipynb'):
            try:
                with open(current_path, 'r', encoding='utf-8') as f:
                    notebook_content = read(f, as_version=NO_CONVERT)
                html_exporter = HTMLExporter()
                notebook_html, _ = html_exporter.from_notebook_node(notebook_content)
                return notebook_html
            except Exception as e:
                return f"Error rendering notebook: {e}", 500
        return send_from_directory(os.path.dirname(current_path), os.path.basename(current_path))

    items = []
    for item in os.listdir(current_path):
        if not item.startswith('.'):  # Ignore hidden files
            full_path = os.path.join(subpath, item) if subpath else item
            items.append(get_file_info(full_path, base_path))

    items.sort(key=lambda x: (not x['is_dir'], x['name'].lower()))

    return render_template_string(
        HTML_TEMPLATE,
        items=items,
        current_path=subpath,
        breadcrumbs=get_breadcrumbs(subpath)
    )

if __name__ == '__main__':
    app.run(debug=True, port=8000)