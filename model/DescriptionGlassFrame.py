from tkinter import *
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from constant import Color
from model import SGFrame
from model import GlassFrame

class DescriptionGlassFrame(SGFrame.SGFrame):
    def __init__(self, parent):
        super(DescriptionGlassFrame, self).__init__(parent)
        self.description = Label(fg=Color.WHITE, bd=0, bg=Color.BLACK, font=('맑은 고딕', 25))
        self.nextButton = Label(text='→', fg=Color.WHITE, bd=0, bg=Color.BLACK, font=('맑은 고딕', 80))
        self.nextButton.place(x=1100, y=550)

        self.moveDescription()

    def moveDescription(self):
        self.description.config(text='축하드립니다.다음 게임은 유리다리 게임입니다.\n\n두개의 발판에는 일반유리와 강화유리가 섞여있습니다.')
        self.description.place(x=530, y=280)
        self.nextButton.bind('<Button>', self.moveGlass)

    def moveGlass(self, event):
        self.removeElement()
        self.glassFrame = GlassFrame.GlassFrame(self)

    def removeElement(self):
        self.description.destroy()
        self.nextButton.destroy()
