from tkinter import *
import datetime

import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from constant import Color

# 2021.11.30 @구지원
# 타이머 클래스
class TimerFrame(Frame):
    def __init__(self, parent):
        super(TimerFrame, self).__init__(parent)
        self.timerLabel = Label(fg=Color.MAIN, bg=Color.BLACK, font=('맑은 고딕', 35))
        self.timerLabel.pack()

        self.currentTime = datetime.datetime.now()
        self.setTimer()

    def setTimer(self):
        # print(datetime.datetime.now())
        self.limitedTime = self.currentTime + datetime.timedelta(minutes=3)
        limitedTimeTxt = str(self.limitedTime - datetime.datetime.now())[2:7]

        self.timerLabel.configure(text=limitedTimeTxt)
        self.timerLabel.place(x=50, y=30)
        self.after(1000, self.setTimer)