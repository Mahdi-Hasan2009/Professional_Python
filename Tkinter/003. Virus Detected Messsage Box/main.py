# Import necessary libraries
from tkinter import *
from tkinter import messagebox

# Create Window
window = Tk()
window.geometry("200x200")

# Function to display warning message
# This will be called once the button is clicked
# messagebox.showwarning("Alert", "Stop! Virus Found.")
def msg():
  messagebox.showwarning("Alert", "Stop! Virus Found.")
  
# Adding Button Widget to Window
button = Button(window, text="Scan for Virus", command=msg)
button.place(x=40, y=80)

# Entering main event loop
window.mainloop()
