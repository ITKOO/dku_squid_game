from tkinter import *
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from constant import Color
from model import SGFrame
from model import HomeFrame
from model import SugarFrame

class DescriptionFrame(SGFrame.SGFrame):
    def __init__(self, parent):
        super(DescriptionFrame, self).__init__(parent)
        self.description = Label(fg=Color.WHITE, bd=0, bg=Color.BLACK, font=('맑은 고딕', 25))
        self.nextButton = Label(text='→', fg=Color.WHITE, bd=0, bg=Color.BLACK, font=('맑은 고딕', 80))
        self.nextButton.place(x=1100, y=550)

        self.moveFrame1()

    def moveFrame1(self):
        self.description.config(text='이자리에 오신 여러분을\n\n진심으로 환영합니다.')
        self.description.place(x=530, y=280)
        self.nextButton.bind('<Button>', self.moveFrame2)

    def moveFrame2(self, event):
        self.description.config(text='모두에게 공정한 게임을 위해서\n\n게임 정보는 사전에 공개할 수 없습니다.')
        self.description.place(x=460, y=280)
        self.nextButton.bind('<Button>', self.moveFrame3)

    def moveFrame3(self, event):
        self.description.config(text='게임에 참가를 원하지 않는 분께서는\n\n지금 아래 버튼을 눌러주시기 바랍니다.')
        self.description.place(x=460, y=280)
        self.nextButton.bind('<Button>', self.moveCharacterFrame)

        self.exitButton = Label(text='게임 그만두기', fg=Color.WHITE, bg=Color.GRAY, bd=0, font=('맑은 고딕', 25), width=20, height=2)
        self.exitButton.place(x=490, y=450)
        self.exitButton.bind('<Button>', self.moveHome)

    def moveCharacterFrame(self, event):
        self.description.config(text='게임을 진행할 캐릭터를 선택해주세요')
        self.description.place(x=470, y=160)
        self.exitButton.destroy()
        self.nextButton.destroy()

    def moveSugarDescriptionFrame(self, event):
        self.description.config(text='반갑습니다. 000 참가자\n\n첫번째 게임은 설탕뽑기입니다.\n\n\n모양은 랜덤으로 선택됩니다.')
        self.description.place(x=530, y=230)
        self.nextButton.destroy()

    def moveHome(self, event):
        self.removeDescriptionElement()
        self.homeFrame = HomeFrame.HomeFrame(self)

    def moveSugar(self, event):
        self.removeDescriptionElement()
        self.sugarFrame = SugarFrame.SugarFrame(self)

    def removeDescriptionElement(self):
        self.description.destroy()
        self.nextButton.destroy()
        self.exitButton.destroy()