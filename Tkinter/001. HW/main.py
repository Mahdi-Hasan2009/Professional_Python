# Import necessary libraries
from tkinter import *
from datetime import date

# Create Window
root = Tk()
root.title('Getting started with widgets')
root.geometry('400x300')

# Add widgets
# Add Label
lbl = Label(
  text="Let's Multiply Two Numbers",
  fg="white",
  bg = "#072F5F",
  height=1,
  width=300
)

# Add Widgets
# Add label
n1_lbl = Label(
  text="Enter Number 1",
  bg="#3895D3"
)
n1_entry = Entry()

# Add label for getting name input from user
# Use Entry Widgets to create a text box for user to enter details
n2_lbl = Label(
  text="Enter Number 2",
  bg="#3895D3"
)
n2_entry = Entry()

# Function to Calculate the Product
def multiply():
  # Fetch the numbers from entry boxes
  n1 = int(n1_entry.get())
  n2 = int(n2_entry.get())
  product = n1*n2
  
  # Display details in a text box
  # Specify where to add the details inside the box
  text_box.insert(END, "Here's the final product...\n")
  text_box.insert(END, product)
  
  
# Add a Text Widget to display information/message
text_box = Text(height=3)

# Add button and give value of command as name of the function
# Press button, display function will be called automatically
btn = Button(
  text = "Calculate",
  command=multiply,
  height=1,
  bg="#1261A0",
  fg='white'
)

# Organize all the widgets in the window
lbl.pack()
n1_lbl.pack()
n1_entry.pack()
n2_lbl.pack()
n2_entry.pack()
btn.pack()
text_box.pack()
root.mainloop()
