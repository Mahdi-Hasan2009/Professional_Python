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