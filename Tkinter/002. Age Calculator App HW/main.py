# Import necessary libraries
from tkinter import *
import datetime

# Create Window
root = Tk()
root.title('Age Calculator App')
root.geometry('400x400')

# Create a frame to organize elements better
frame = Frame(master=root, height=200, width=360, bg="#FAB072")

# Add widgets
# Add Label
lbl1 = Label(frame, text='Name', bg="navyblue", fg='white', width=12)
lbl2 = Label(frame, text='Year', bg="navyblue", fg='white', width=12)
lbl3 = Label(frame, text='Month', bg="navyblue", fg='white', width=12)
lbl4 = Label(frame, text='Date', bg="navyblue", fg='white', width=12)

# Use 