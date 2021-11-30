from tkinter import *
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from constant import Color
from model import SGFrame
from model import DescriptionFrame

class HomeFrame(SGFrame.SGFrame):
    def __init__(self, parent):
        super(HomeFrame, self).__init__(parent)
        self.moveHome()

    def moveHome(self):
        self.startButton = Label(text='게임 시작하기', fg=Color.WHITE, bg=Color.GRAY, bd=0, font=('맑은 고딕', 25), width=20, height=2)
        self.startButton.place(x=490, y=200)
        self.startButton.bind('<Button-1>', self.startGame)

        self.lankingButton = Label(text='랭킹 보기', fg=Color.WHITE, bg=Color.GRAY, bd=0, font=('맑은 고딕', 25), width=20, height=2)
        self.lankingButton.place(x=490, y=350)
        self.lankingButton.bind('<Button>', self.viewRanking)

    def startGame(self, event):
        self.removeHomeButton()
        self.descriptionFrame = DescriptionFrame.DescriptionFrame(self)

    def viewRanking(self, event):
        self.removeHomeButton()
        self.descriptionFrame = DescriptionFrame.DescriptionFrame(self)

    def removeHomeButton(self):
        self.startButton.destroy()
        self.lankingButton.destroy()
