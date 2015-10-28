# -*- coding: utf-8 -*-
import Tkinter as tk


TITLE_FONT = ("Helvetica", 18, "bold")


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            frame = F(container, self)
            self.frames[F] = frame
            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, c):
        '''Show a frame for the given class'''
        frame = self.frames[c]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Diary", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="写日记",
                            command=lambda: controller.show_frame(PageOne))
        button2 = tk.Button(self, text="读日记",
                            command=lambda: controller.show_frame(PageTwo))

        self.photo1=tk.PhotoImage(file="images/write_200.gif")
        canvas1=tk.Canvas(self, width=self.photo1.width(), height=self.photo1.height())
        canvas1.create_image(100,70,image=self.photo1)


        self.photo2=tk.PhotoImage(file="images/read_200.gif")
        canvas2=tk.Canvas(self, width=self.photo2.width(), height=self.photo1.height())
        canvas2.create_image(100,80,image=self.photo2)

        canvas1.pack()
        button1.pack()
        canvas2.pack()
        button2.pack()

        canvas=tk.Canvas(self,width=400,height=10)
        canvas.pack()
        # 让界面宽一点，同时给底部添加一个pady，因为还不知道具体用法，先用weight和height来占位

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="写日记", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go back",
                           command=lambda: controller.show_frame(StartPage))
        button.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="读日记", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go back",
                           command=lambda: controller.show_frame(StartPage))
        button.pack()
        
        text = tk.Text(self,height=2, width=30)
        text.pack()
        text.insert(tk.END, "Just a text Widget\nin two lines\n")


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
