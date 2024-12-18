# Import necessary libraries
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

# Setup Root Window
screen = Tk()
screen.title("Text Editor")
screen.geometry("400x300")
screen.rowconfigure(0, minsize=800, weight=1)
screen.columnconfigure(1, minsize=800, weight=1)

# Function to Open a file
def open_file():
    """Open a file for editing"""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, END)
    # If a file is opened, display the contents of the file
    with open(filepath, "r") as input_file:
        # Read the contents of the input file
        text = input_file.read()
        # Insert contents of the file in the editor box
        txt_edit.insert(END, text)
    screen.title(f"Text Editor - {filepath}")

# Function to Save a file
def save_file():
    """Save the current file"""
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    # Save the contents of the text box to the file
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, END)  # Get all text from the text box
        output_file.write(text)
    screen.title(f"Text Editor - {filepath}")

# Add widgets in the application
txt_edit = Text(screen)
fr_buttons = Frame(screen, relief=RAISED, bd=2)
btn_open = Button(fr_buttons, text="Open", command=open_file)
btn_save = Button(fr_buttons, text="Save as", command=save_file)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5, pady=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

screen.mainloop()
