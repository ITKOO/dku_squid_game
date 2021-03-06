from tkinter import *
from frame import SGWindow
from model import Point
from frame import FailedFrame
from frame import TimerFrame
from frame import SGFrame
from frame import DescriptionGlassFrame
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from constant import Color

# 2021.11.30 @구지원
# 달고나게임 클래스
class SugarFrame(SGFrame.SGFrame):
    # 상수 선언
    STARTING_POINT = 140
    STANDARD_POINT_X = 160
    POINT_RANGE = 30

    totalSugarLineCount = 0
    clickCount = 0

    def __init__(self, parent):
        super(SugarFrame, self).__init__(parent)

        # 0. 타이머 호출
        self.timerFrame = TimerFrame.TimerFrame(self)

        # 1. 달고나 몸판 그리기
        self.gameFrame = Frame(width=1280, height=500, bg=Color.BLACK)
        self.gameFrame.place(x=0, y=130)

        self.sugarImage = PhotoImage(file="img/sugar/sugar.png")
        self.sugarLabel = Label(self.gameFrame, image=self.sugarImage, bg=Color.BLACK, bd=0)

        self.sugarLabel.place(x=450, y=30)

        # 2. 달고나 모양 삽입(삼각형)
        self.sugarLabel.bind('<Button>', self.clickSugar)
        self.canvas = Canvas(self.gameFrame, bg=Color.SUGAR, bd=0, highlightthickness=0, relief='ridge', width=330)
        self.canvas.place(x=500, y=140)

        # 3. 삼각형 그리기
        # 총 달고라 라인 갯수(달고나 라인 갯수만큼 클릭시 게임 성공)
        self.drawTriangle()

    # 달고나 선택시 실행되는 함수(게임 실패)
    def clickSugar(self, event):
        # 실패 화면으로 프레임 교체
        self.removeElement()
        self.failedFrame = FailedFrame.FailedFrame(self)

    # 달고나 모양 라인 클릭시 실행되는 함수(게임 성공)
    def clickLine(self, event, canvas, lineElement):
        canvas.itemconfig(lineElement, fill='#D54C7E')
        self.clickCount += 1

        if self.checkGameStatus():
            # 성공 화면으로 프레임 교체
            self.removeElement()
            self.successFrame = DescriptionGlassFrame.DescriptionGlassFrame(self)

    # 게임 성공여부 판단하는 함수(달고나 모양대로 클릭했는지 판단)
    def checkGameStatus(self):
        if self.totalSugarLineCount == self.clickCount:
            return TRUE

        return FALSE

    # 삼각형을 그리는 함수
    def drawTriangle(self):
        # 삼각형 왼쪽 빗변
        self.drawPartTriangle(self.canvas, 'LEFT', 0, self.STARTING_POINT, self.POINT_RANGE)
        # 삼각형 오른쪽 빗변
        self.drawPartTriangle(self.canvas, 'RIGHT', 0, self.STARTING_POINT, self.POINT_RANGE)
        # 삼각형 아랫변
        self.drawPartTriangle(self.canvas, 'BOTTOM', 5, 290, self.POINT_RANGE)

    # 삼각형의 변들을 그리는 함수(오른쪽 빗변, 왼쪽 빗변, 밑변)
    def drawPartTriangle(self, canvas, location, start, end, pointRange):
        for i in range(start, end, pointRange):
            pointList = self.getPointsByLocation(location, i)
            line = canvas.create_line(pointList[0].x, pointList[0].y, pointList[1].x, pointList[1].y, width=10,
                                      fill='#C4C4C4')
            canvas.tag_bind(line, "<Button>", lambda event, item=line: self.clickLine(event, canvas, item))
            self.totalSugarLineCount += 1

    # 삼각형 변의 위치에 따라 좌표를 정해 라인을 그리는 함수
    def getPointsByLocation(self, location, value):
        pointList = []
        point1 = ''
        point2 = ''

        # 삼각형 왼쪽 빗변
        if location == 'LEFT':
            point1 = Point.Point(self.STANDARD_POINT_X - value, value)
            point2 = Point.Point((self.STANDARD_POINT_X - (value + self.POINT_RANGE)), value + self.POINT_RANGE)

        # 삼각형 오른쪽 빗변
        if location == 'RIGHT':
            point1 = Point.Point(self.STANDARD_POINT_X + value, value)
            point2 = Point.Point((self.STANDARD_POINT_X + (value + self.POINT_RANGE)), value + self.POINT_RANGE)

        # 삼각형 아랫변
        if location == 'BOTTOM':
            point1 = Point.Point(value, self.STARTING_POINT)
            point2 = Point.Point(value + self.POINT_RANGE, self.STARTING_POINT)

        pointList.append(point1)
        pointList.append(point2)

        return pointList

    # 달고나게임에 사용되었던 프레임들을 삭제하는 함수
    def removeElement(self):
        self.timerFrame.destroy()
        self.gameFrame.destroy()
