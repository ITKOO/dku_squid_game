from tkinter import *
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from constant import Color
from model import SGFrame

class FailedFrame(SGFrame.SGFrame):
    def __init__(self, parent):
        super(FailedFrame, self).__init__(parent)
        self.label = Label(text='탈락입니다.\n\n당신은 오징어 입니다.', fg=Color.WHITE,
                           bg=Color.BLACK, font=('맑은 고딕', 25), width=40, height=10)
        self.label.place(x=300, y=160)