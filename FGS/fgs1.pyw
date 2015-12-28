# Version 1
import os, urllib2
from Tkinter import *
from PIL import Image, ImageTk

def search(txt):
    os.system("start chrome https://www.google.com/search?q=%s"%txt.replace(" ", "+"))

if __name__ == '__main__':
    app = Tk()
    app.minsize(width=350, height=250)
    app.maxsize(width=350, height=250)
    app.title("")
    app.configure(background='white')

    img = ImageTk.PhotoImage(Image.open('logo.png')) # Google logo 220x74
    Label(app, image = img, borderwidth=0).pack(pady=30)

    txt = Entry(app,font=("Verdana", 15))
    txt.pack(fill=X,padx=40)
    Button(app,text="Search",command=lambda: search(txt.get()), bg="#3369E8", fg='white',font=("Verdana", 11)).pack(pady=10)

    app.mainloop()
