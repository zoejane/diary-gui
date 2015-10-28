'''from Tkinter import *
class App:
  def __init__(self, master):
    frame = Frame(master)
    frame.pack()
    self.button = Button(frame, 
                         text="QUIT", fg="red",
                         command=frame.quit)
    self.button.pack(side=LEFT)


    self.slogan = Button(frame,
                         text="Hello",
                         command=self.write_slogan)
    self.slogan.pack(side=LEFT)
  def write_slogan(self):
    print "Tkinter is easy to use!"

root = Tk()
app = App(root)
root.mainloop()'''

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

        button = Tkinter.Button(frame, text = "Ende", command = master.destroy)
        button.pack()
        
        self.photo2=Tkinter.PhotoImage(file="images/read_200.gif")
        canvas=Tkinter.Canvas(frame, width=self.photo2.width(), height=self.photo2.height())
        canvas.create_image(0,0,anchor=NW,image=self.photo2)
        canvas.pack()

        button = Tkinter.Button(frame, text = "Ende", command = master.destroy)
        button.pack()


tk = Tkinter.Tk()

app = Application(tk)

tk.mainloop()

'''from Tkinter import *

canvas_width = 300
canvas_height =300

master = Tk()

canvas = Canvas(master, 
           width=canvas_width, 
           height=canvas_height)
canvas.pack()

img1 = PhotoImage(file="images/write_200.gif")
canvas.create_image(20,20, anchor=NW, image=img1)
img2 = PhotoImage(file="images/read_200.gif")
canvas.create_image(200,20, anchor=NW, image=img2)

mainloop()'''
