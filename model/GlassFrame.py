import random
from tkinter import *
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from constant import Color
from model import SGFrame
from model import FailedFrame
from model import RankingFrame


class GlassFrame(SGFrame.SGFrame):   #유리 사다리 게임
    clickCount = 0
    def __init__(self, parent):
        super(GlassFrame, self).__init__(parent)
        self.glass()

    def fail(self, event):  # 유리 사다리 게임 실패시 실패 화면이 나오게 하는 함수 정의
       self.removeGlassElement()
       self.failedFrame = FailedFrame.FailedFrame(self)

    def success(self, event, buttonElement):     #강화유리 선택 시 clickCount가 1씩 더해짐
        print('성공')
        self.clickCount += 1
        buttonElement.destroy()

        if self.clickCount >= 5:      #5개의 강화 유리 선택 시 goal 호출
            self.goal()

    def goal(self):  # 게임 성공 후 랭킹 등록으로 이동
        self.removeGlassElement()
        self.rankingFrame = RankingFrame.RankingFrame(self)

    def glass(self):  # 유리 사다리 게임 실행
        photo = PhotoImage(file="../img/glass/오징어게임 유리다리.png")
        self.background = Label(image=photo, width=1280, height=800)
        self.background.place(x=0, y=100)
        self.background.photo = photo
        self.background.pack()

        randomXList = [400, 630]
        for i in range(1, 6):      #강화유리 일반유리 5번 반복하여 생성
            randomX1 = randomXList[0]
            randomX2 = randomXList[1]
            randomNum = random.randint(1, 100)

            if(randomNum % 2 == 0): # 짝수면 오른쪽
                randomX1 = randomXList[1]
                randomX2 = randomXList[0]

            self.setSuccessButton(randomX1, 100 * i)
            self.setFailButton(randomX2, 100 * i)


    def setSuccessButton(self, xCoordinate, yCoordinate):    #강화 유리 좌표 설정
        print('성공 ', '(', str(xCoordinate), ',', str(yCoordinate), ')')    #강화 유리 보여주기
        button1 = Button(self.background, text="성공", height=5, width=20, bg='white')
        button1.place(x=xCoordinate, y=yCoordinate)
        button1.bind("<Button>", lambda event, buttonElement=button1: self.success(event, buttonElement))  #강화유리 선택 시 success함수 호출

    def setFailButton(self, xCoordinate, yCoordinate):     #일반 유리 좌표 설정
        print('실패 ', '(', str(xCoordinate), ',', str(yCoordinate), ')')
        button1 = Button(self.background, text=" ", height=5, width=20, bg='white')
        button1.place(x=xCoordinate, y=yCoordinate)
        button1.bind('<Button>', self.fail)     #일반 유리 선택 시 fail 함수 호출

    def removeGlassElement(self):   #선택된 유리 삭제
        self.background.destroy()
