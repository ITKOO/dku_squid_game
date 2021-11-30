import random
from tkinter import *
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from constant import Color
from frame import SGFrame
from frame import FailedFrame
from frame import RankingFrame


class GlassFrame(SGFrame.SGFrame):
    clickCount = 0
    def __init__(self, parent):
        super(GlassFrame, self).__init__(parent)
        self.glass()

    def fail(self, event):  # 유리 사다리 게임 실패시 실패 화면이 나오게 하는 함수 정의
       self.removeGlassElement()
       self.failedFrame = FailedFrame.FailedFrame(self)

    def success(self, event, buttonElement):
        print('성공')
        self.clickCount += 1
        buttonElement.destroy()

        if self.clickCount >= 5:
            self.goal()

    def goal(self):  # 게임 성공시 나오는 goal 함수 정의
        self.removeGlassElement()
        self.rankingFrame = RankingFrame.RankingFrame(self)

    def glass(self):  # 유리 사다리 게임 실행 화면
        photo = PhotoImage(file="img/glass/오징어게임 유리다리.png")
        self.background = Label(image=photo, width=1280, height=800)
        self.background.place(x=0, y=100)
        self.background.photo = photo
        self.background.pack()

        randomXList = [400, 630]
        for i in range(1, 6):
            randomX1 = randomXList[0]
            randomX2 = randomXList[1]
            randomNum = random.randint(1, 100)

            if(randomNum % 2 == 0): # 짝수면 오른쪽
                randomX1 = randomXList[1]
                randomX2 = randomXList[0]

            self.setSuccessButton(randomX1, 100 * i)
            self.setFailButton(randomX2, 100 * i)


    def setSuccessButton(self, xCoordinate, yCoordinate):
        print('성공 ', '(', str(xCoordinate), ',', str(yCoordinate), ')')
        button1 = Button(self.background, text="성공", height=5, width=20, bg='white')
        button1.place(x=xCoordinate, y=yCoordinate)
        button1.bind("<Button>", lambda event, buttonElement=button1: self.success(event, buttonElement))

    def setFailButton(self, xCoordinate, yCoordinate):
        print('실패 ', '(', str(xCoordinate), ',', str(yCoordinate), ')')
        button1 = Button(self.background, text=" ", height=5, width=20, bg='white')
        button1.place(x=xCoordinate, y=yCoordinate)
        button1.bind('<Button>', self.fail)

    def removeGlassElement(self):
        self.background.destroy()
