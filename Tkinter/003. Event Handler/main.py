# Import necessary libraries
from tkinter import *

# Create Window
window = Tk()
window.title('Event Handler')
window.geometry("100x100")

# Event Handler for Keypress
def handle_keypress(event):
  """Print the Character associated to the key pressed"""
  print(event.char)

# Bind keypress event to handle_keypress()
window.bind("<Key>", handle_keypress)

# Event handler for button click
def handle_click(event):
  print("\nThe button was clicked!")
  
button = Button(text="Click me!")
button.pack()

# Bind click event to handle_click()
button.bind("<Button-1>", handle_click)

window.mainloop()