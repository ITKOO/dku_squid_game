from tkinter import *
import time

import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from constant import Color

class SGWindow():
    def __init__(self, title, isTimerShow):
        # 1. 윈도우 기본 설정(이름, 창크기, 배경색 ..)
        self.root = Tk()
        self.root.title(title)
        self.root.geometry('1280x720')
        self.root['bg'] = Color.BLACK
        self.root.resizable(False, False)

        # 2. 오른쪽 사이드 상단 작은 로고 삽입
        self.setSideLogoImage()

        # 3. 타이머
        if isTimerShow:
            self.timerLabel = Label(
                fg=Color.MAIN,
                bg=Color.BLACK,
                font=('맑은 고딕', 35))
            self.timerLabel.pack()
            self.setTimer()

    def setSideLogoImage(self):
        self.smallLogoImage = PhotoImage(file="../img/sugar/small_logo.png")
        self.sideLogoLabel = Label(self.root,
                                   image=self.smallLogoImage,
                                   bd=0)
        self.sideLogoLabel.place(x=1100, y=30)

    def setTimer(self):
        now = time.strftime("%M:%S")
        self.timerLabel.configure(text=now)
        self.timerLabel.place(x=50, y=30)
        self.root.after(1000, self.setTimer)