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
  text="Hey There",
  fg="white",
  bg = "#3895D3",
  height=1,
  width=300
)

# Add label for getting name input from user
# Use Entry Widgets to create a text box for user to enter details
name_lbl = Label(
  text="Full Name",
  bg="#3895D3"
)
name_entry = Entry()

# Function to display a Message
def display():
  # Read the input given by user
  name = name_entry.get()
  # Declaring a global variable
  # to make it accessible anywhere in the programme
  global message
  message = "Welcome to the Application! \nToday's date is: "
  greet = "Hello "+name+"\n"
  
  # Display details in a text box
  # Specify where to add details inside the text box
  text_box.insert(END, greet)
  text_box.insert(END, message)
  text_box.insert(END, date.today())
  
# Add a Text Width display information/message
text_box = Text(height=3)

# Add button and give value of command as name of the function
# Press button, display function will be called automatically
btn = Button(
  text = "Begin",
  command=display,
  height=1,
  bg="#1261A0",
  fg='white'
)

# Organize all the widgets in the window
lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()
root.mainloop()