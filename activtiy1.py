from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title('Denomination Counter')
root.configure(bg='light blue')
root.geometry('650x400')

upload = Image.open("app_img.jpg")
upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, bg='light blue')
label.place(x=180, y=20)

label1 = Label(root, text="Hey User!, Welcome to Denomination Counter Application.", bg='light blue')
label1.place(relx=0.5, y=340, anchor=CENTER)

def msg():
    Msgbox = messagebox.askyesno("Alert", "Do you want to calculate the denomination count?")
    if Msgbox:
        topwin()

button1 = Button(root, text="Let's get started!", command=msg, bg='brown', fg='white')
button1.place(x=260, y=360)

def topwin():
    top = Toplevel()
    top.title("Denomination Counter")
    top.configure(bg='light grey')
    top.geometry("600x350+50+50")

    label = Label(top, text='Enter total amount', bg='light grey')
    label.place(x=50, y=30)

    entry = Entry(top)
    entry.place(x=200, y=30)

    lbl = Label(top, text='Here are the number of notes for each denomination:', bg='light grey')
    lbl.place(x=50, y=70)

    l1 = Label(top, text="2000", bg='light grey')
    l1.place(x=50, y=110)
    t1 = Entry(top)
    t1.place(x=200, y=110)

    l2 = Label(top, text="500", bg='light grey')
    l2.place(x=50, y=150)
    t2 = Entry(top)
    t2.place(x=200, y=150)

    l3 = Label(top, text="100", bg='light grey')
    l3.place(x=50, y=190)
    t3 = Entry(top)
    t3.place(x=200, y=190)

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

    btn = Button(top, text="Calculate", command=calculator, bg='brown', fg='white')
    btn.place(x=200, y=250)

root.mainloop()
