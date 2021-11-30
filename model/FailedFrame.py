from tkinter import *
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from constant import Color
from model import SGFrame

class FailedFrame(SGFrame.SGFrame):
    def __init__(self, parent):
        super(FailedFrame, self).__init__(parent)
        self.label = Label(text='실패', fg=Color.WHITE, font=('맑은 고딕', 100)).place(x=530, y=250)