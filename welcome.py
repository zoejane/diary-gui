# -*- coding: utf-8 -*-

import Tkinter
from Tkconstants import *

class Application:
    def __init__(self, master):
        frame = Tkinter.Frame(master)
        frame.pack()

        self.photo1=Tkinter.PhotoImage(file="images/write_200.gif")
        canvas=Tkinter.Canvas(frame, width=self.photo1.width(), height=self.photo1.height())
        canvas.create_image(0,0,anchor=NW,image=self.photo1)
        canvas.pack()

        button = Tkinter.Button(frame, text = "写日记", command = master.destroy)
        button.pack()
        
        self.photo2=Tkinter.PhotoImage(file="images/read_200.gif")
        canvas=Tkinter.Canvas(frame, width=self.photo2.width(), height=self.photo2.height())
        canvas.create_image(0,0,anchor=NW,image=self.photo2)
        canvas.pack()

        button = Tkinter.Button(frame, text = "读日记", command = master.destroy)
        button.pack()


tk = Tkinter.Tk()

app = Application(tk)

tk.mainloop()
'''

import Tkinter
from Tkconstants import *

def fenster(tk):
    frame=Tkinter.Frame(tk)
    frame.pack()
    photo=Tkinter.PhotoImage(file="images/read_200.gif")
    canvas=Tkinter.Canvas(frame,width=400,height=500,bg="blue")
    canvas.create_image(200, 250, image=photo)
    canvas.pack()
    button=Tkinter.Button(frame, text="EXIT", command=tk.destroy)
    button.pack()
    return photo
    
tk = Tkinter.Tk()
ergebnis=fenster(tk)
tk.mainloop()


'''