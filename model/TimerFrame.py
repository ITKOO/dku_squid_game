from tkinter import *
import time
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from constant import Color

class TimerFrame(Frame):
    def __init__(self, parent):
        super(TimerFrame, self).__init__(parent)
        self.timerLabel = Label(fg=Color.MAIN, bg=Color.BLACK, font=('맑은 고딕', 35))
        self.timerLabel.pack()
        self.setTimer()

    def setTimer(self):
        now = time.strftime("%M:%S")
        self.timerLabel.configure(text=now)
        self.timerLabel.place(x=50, y=30)
        self.after(1000, self.setTimer)