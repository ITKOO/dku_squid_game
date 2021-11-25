from tkinter import *


class Window:
    app = Tk()

    def __init__(self, title):
        self.title = title

    def load(self):
        self.app.title(self.title)
        self.app.geometry('200 X 50')
        self.app.resizable(False, False)
        self.app.protocol('WM_DELETE_WINDOW', exit())
        self.app.mainloop()
