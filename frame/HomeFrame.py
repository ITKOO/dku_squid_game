from tkinter import *
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from constant import Color
from frame import SGFrame
from frame import DescriptionFrame

class HomeFrame(SGFrame.SGFrame):
    def __init__(self, parent):
        super(HomeFrame, self).__init__(parent)
        self.moveHome()

    def moveHome(self):
        self.photo = PhotoImage(file="img/description/로고.png")
        self.w = Label(image=self.photo,bd=0)
        self.w.photo = self.photo
        self.w.pack()
        self.w.place(x=250,y=30)
        
        self.startButton = Label(text='게임 시작하기', fg=Color.WHITE, bg=Color.GRAY, bd=0, font=('맑은 고딕', 25), width=20, height=2)
        self.startButton.place(x=450, y=450)
        self.startButton.bind('<Button-1>', self.startGame)

        self.lankingButton = Label(text='랭킹 보기', fg=Color.WHITE, bg=Color.GRAY, bd=0, font=('맑은 고딕', 25), width=20, height=2)
        self.lankingButton.place(x=450, y=600)
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
        self.w.destroy()

