from tkinter import *
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from constant import Color

class SGFrame(Frame):
    def __init__(self, parent):
        super(SGFrame, self).__init__(parent)
        self.config(width=1280, height=800, bg=Color.BLACK)
        self.place(x=0, y=130)