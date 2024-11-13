from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("200x200")

# showwarning(): Show the user the warning.
def msg():
  messagebox.showwarning("Alert", "Stop! Virus Found.")
  
button = Button(window, text="Scan for Virus", command=msg)
button.place(x=40, y=80)

# showinfo(): Provide the user with some helpful information.
def info():
  messagebox.showinfo("Hey", "The message box is create by Mahdi")
  
button = Button(window, text="About me", command=info)
button.place(x=40, y=50)

# showwarning(): Show the user the warning.
def warning():
  messagebox.showwarning("Copyright", "All rights are reserved by Mahdi")
  
button = Button(window, text="Copyright Info", command=warning)
button.place(x=40, y=110)

# showerror(): Shows the user the error message.
def error():
  messagebox.showerror("Error", "It is a mistake")
  
button = Button(window, text="Error Button", command=error)
button.place(x=40, y=20)

# askquestion(): Pose a question to the user, who must respond with a yes or no.
def ask_question():
  messagebox.askquestion("Hello", "Are you fine?")
  
button = Button(window, text="About You", command=ask_question)
button.place(x=40, y=-10)


"""
The MessageBox Widget is used in Python programs to show message boxes. This module is used to display a message and has various features.
messagebox.Function_Name(title, message)
The messagebox widget has several functions and methods. The name of these functions are mentioned below, along with their uses -
showinfo(): Provide the user with some helpful information.
showwarning(): Show the user the warning.
showerror(): Shows the user the error message.
askquestion(): Pose a question to the user, who must respond with a yes or no.
askokcancel(): Confirm the user's action concerning a particular application activity.
askyesno(): The user can respond with a yes or no for various actions.
askretrycancel(): Inquires whether the user wants to repeat a task.
"""
window.mainloop()