from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk  # A library to add images in tkinter - pillow

root = Tk()
root.title('Denomination Calculator')
root.configure(bg='light blue')
root.geometry('650x400')

# Load and display the image
try:
    upload = Image.open("app_img.jpg")
    upload = upload.resize((300, 300))
    image = ImageTk.PhotoImage(upload)
    label = Label(root, image=image, bg='light blue')
    label.place(x=180, y=20)
except FileNotFoundError:
    label = Label(root, text="Image not found", bg='light blue', fg='red')
    label.place(x=250, y=150)

# Welcome label
label1 = Label(
    root,
    text="Hey User! Welcome to Denomination Calculator.",
    bg='light blue'
)
label1.place(relx=0.5, y=340, anchor=CENTER)

# Function to display the denomination calculator
def msg():
    MsgBox = messagebox.showinfo(
        "Alert", "Do you want to calculate the denomination count?"
    )
    if MsgBox == 'ok':
        topwin()

# Button to start the calculation
button1 = Button(
    root,
    text="Let's get started!",
    command=msg,
    bg='brown',
    fg='white'
)
button1.place(x=260, y=360)

# Top window function
def topwin():
    top = Toplevel(root)
    top.title("Denominations Calculator")
    top.configure(bg='light grey')
    top.geometry("600x350+50+50")

    # Widgets in the top window
    label = Label(top, text="Enter total amount", bg='light grey')
    entry = Entry(top)
    lbl = Label(top, text="Here are notes of denomination", bg='light grey')

    l1 = Label(top, text="2000", bg='light grey')
    l2 = Label(top, text="500", bg='light grey')
    l3 = Label(top, text="100", bg='light grey')

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)

    # Calculator function
    def calculator():
        try:
            amount = int(entry.get())
            note2000 = amount // 2000
            amount %= 2000
            note500 = amount // 500
            amount %= 500
            note100 = amount // 100

            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)

            t1.insert(END, str(note2000))
            t2.insert(END, str(note500))
            t3.insert(END, str(note100))
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    btn = Button(top, text='Calculate', command=calculator, bg='brown', fg='white')

    # Centering Widgets in the Top Window
    label.place(x=230, y=50)
    entry.place(x=200, y=80)
    btn.place(x=240, y=120)
    lbl.place(x=140, y=170)

    l1.place(x=180, y=200)
    l2.place(x=180, y=230)
    l3.place(x=180, y=260)

    t1.place(x=270, y=200)
    t2.place(x=270, y=230)
    t3.place(x=270, y=260)

# Run the main loop
root.mainloop()