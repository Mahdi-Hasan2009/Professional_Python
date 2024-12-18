from tkinter import *
root = Tk()
root.geometry("400x300")
root.title("Main")

def topwin1():
  top = Toplevel()
  top.geometry("180x100")
  top.title("Top Level")
  l2 = Label(top, text = "The top level window")
  l2.pack
  top.mainloop()
  
l = Label(root, text = "This is the root window")
btn = Button(root, text = "Click here to open another window", command = topwin1)

l.pack()
btn.pack()

root.mainloop()