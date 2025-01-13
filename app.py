from flask import Flask, jsonify, request, render_template, send_file
import os
from functools import wraps
from flask_cors import CORS
from datetime import datetime
import json
from base64 import b64encode
import mimetypes

app = Flask(__name__)
CORS(app)

def require_password(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        password = os.environ.get('DIRECTORY_PASSWORD', 'admin123')
        auth_header = request.headers.get('Authorization')
        if not auth_header or auth_header != f'Bearer {password}':
            return jsonify({"error": "Unauthorized"}), 401
        return f(*args, **kwargs)
    return decorated

def get_directory_info(path):
    items = []
    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        if os.path.isdir(full_path):
            try:
                stats = os.stat(full_path)
                mod_time = datetime.fromtimestamp(stats.st_mtime)
                items.append({
                    "name": item,
                    "type": "directory",
                    "modified": mod_time.strftime("%Y-%m-%d %H:%M:%S"),
                    "path": full_path.replace("\\", "/"),
                    "size": stats.st_size
                })
            except OSError as e:
                print(f"Error accessing directory {full_path}: {e}")
                continue
        else:
            try:
                stats = os.stat(full_path)
                mod_time = datetime.fromtimestamp(stats.st_mtime)
                mime_type, _ = mimetypes.guess_type(full_path)
                items.append({
                    "name": item,
                    "type": "file",
                    "modified": mod_time.strftime("%Y-%m-%d %H:%M:%S"),
                    "path": full_path.replace("\\", "/"),
                    "size": stats.st_size,
                    "mime_type": mime_type or "application/octet-stream"
                })
            except OSError as e:
                print(f"Error accessing file {full_path}: {e}")
                continue
    
    return sorted(items, key=lambda x: (x['type'] == 'file', x['name'].lower()))

def get_file_content_base64(path):
    _, file_extension = os.path.splitext(path)
    file_extension = file_extension.lower()

    # Define supported file types and their handlers
    handlers = {
        'image': ('.jpg', '.jpeg', '.png', '.gif', '.bmp'),
        'text': ('.txt', '.md', '.csv', '.json', '.yml', '.yaml'),
        'code': ('.py', '.js', '.html', '.css', '.java', '.cpp', '.c', '.h', '.hpp')
    }

    try:
        if file_extension in handlers['image']:
            with open(path, 'rb') as file:
                encoded_content = b64encode(file.read()).decode('utf-8')
                return {"type": 'image', "content": f'data:image/{file_extension[1:]};base64,{encoded_content}'}
        
        elif file_extension in handlers['text'] or file_extension in handlers['code']:
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
                return {"type": 'code' if file_extension in handlers['code'] else 'text', "content": content}
        
        else:
            return {"type": 'error', "content": 'File type not supported'}

    except Exception as e:
        return {"type": 'error', "content": f'Error reading file: {str(e)}'}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/file_viewer')
def file_viewer():
    return render_template('file_viewer.html')

@app.route('/api/directories')
@require_password
def list_directories():
    base_path = "."
    try:
        directories = get_directory_info(base_path)
        return jsonify(directories)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/file_content')
@require_password
def file_content():
    file_path = request.args.get('path')
    if not file_path:
        return jsonify({"error": "Path parameter missing"}), 400
    
    if not os.path.exists(file_path):
        return jsonify({"error": "File not found"}), 404
    
    if not os.path.isfile(file_path):
        return jsonify({"error": "Path is not a file"}), 400
    
    try:
        content = get_file_content_base64(file_path)
        return jsonify(content)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=52156)