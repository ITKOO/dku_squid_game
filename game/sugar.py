from tkinter import *
import time

import sys, os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from constant import Color
from model import Point

for i in range(0, 181):
    limitedTime = time.gmtime(180 - i)
    minute = limitedTime.tm_min
    second = limitedTime.tm_sec
    print(mi)

    if minute / 10 == 0:
        minute = '0' + str(minute)

    if second / 10 == 0:
        second = '0' + str(second)

    print(minute, ':', minute)

# 상수 선언
STARTING_POINT = 140
STANDARD_POINT_X = 160
POINT_RANGE = 30

totalSugarLineCount = 0
clickCount = 0


# 달고나 선택시 실행되는 함수(게임 실패)
def clickSugar(event):
    # 실패 화면으로 프레임 교체
    failedFrame = Frame(width=1280, height=500, bg=Color.BLACK).place(x=0, y=130)
    failedLabel = Label(failedFrame, text='실패', fg=Color.WHITE, font=('맑은 고딕', 100)).place(x=530, y=250)


# 달고나 모양 라인 클릭시 실행되는 함수(게임 성공)
def clickLine(event, canvas, lineElement):
    global clickCount
    canvas.itemconfig(lineElement, fill='#D54C7E')
    clickCount += 1

    if checkGameStatus(clickCount):
        # 성공 화면으로 프레임 교체
        passFrame = Frame(width=1280, height=500, bg=Color.BLACK).place(x=0, y=130)
        passLabel = Label(passFrame, text='성공', fg=Color.WHITE, font=('맑은 고딕', 100)).place(x=530, y=250)


# 게임 성공여부 판단하는 함수(달고나 모양대로 클릭했는지 판단)
def checkGameStatus(clickCount):
    global totalSugarLineCount
    if totalSugarLineCount == clickCount:
        return TRUE

    return FALSE


# 삼각형을 그리는 함수
def drawTriangle(canvas):
    # 삼각형 왼쪽 빗변
    drawPartTriangle(canvas, 'LEFT', 0, STARTING_POINT, POINT_RANGE)
    # 삼각형 오른쪽 빗변
    drawPartTriangle(canvas, 'RIGHT', 0, STARTING_POINT, POINT_RANGE)
    # 삼각형 아랫변
    drawPartTriangle(canvas, 'BOTTOM', 5, 290, POINT_RANGE)


# 삼각형의 변들을 그리는 함수(오른쪽 빗변, 왼쪽 빗변, 밑변)
def drawPartTriangle(canvas, location, start, end, pointRange):
    global totalSugarLineCount
    for i in range(start, end, pointRange):
        pointList = getPointsByLocation(location, i)
        line = canvas.create_line(pointList[0].x, pointList[0].y, pointList[1].x, pointList[1].y, width=10,
                                  fill='#C4C4C4')
        canvas.tag_bind(line, "<Button>", lambda event, item=line: clickLine(event, canvas, item))
        totalSugarLineCount += 1


# 삼각형 변의 위치에 따라 좌표를 정해 라인을 그리는 함수
def getPointsByLocation(location, value):
    pointList = []
    point1 = ''
    point2 = ''

    if location == 'LEFT':
        point1 = Point.Point(STANDARD_POINT_X - value, value)
        point2 = Point.Point((STANDARD_POINT_X - (value + POINT_RANGE)), value + POINT_RANGE)

    if location == 'RIGHT':
        point1 = Point.Point(STANDARD_POINT_X + value, value)
        point2 = Point.Point((STANDARD_POINT_X + (value + POINT_RANGE)), value + POINT_RANGE)

    if location == 'BOTTOM':
        point1 = Point.Point(value, STARTING_POINT)
        point2 = Point.Point(value + POINT_RANGE, STARTING_POINT)

    pointList.append(point1)
    pointList.append(point2)

    return pointList


# 1. Tkinter 윈도우 창 생성
app = Tk()
app.title('달고나게임')
app.geometry('1280x720')
app['bg'] = Color.BLACK
app.resizable(False, False)

# 2. 오른쪽 사이드 상단 작은 로고 삽입
smallLogoImage = PhotoImage(file="img/sugar/small_logo.png")
sideLogoLabel = Label(app,
                      image=smallLogoImage,
                      bd=0).place(x=1100, y=30)

# 3. 왼쪽 사이드 상단 타이머 표시
timerLabel = Label(text='2 : 58',
                   fg=Color.MAIN,
                   bg=Color.BLACK,
                   font=('맑은 고딕', 35))

timerLabel.place(x=50, y=30)

# TODO 4. 타이머 기능 설정
timerLabel.config(text='aaa')

# 5. 달고나 몸판 그리기
sugarFrame = Frame(width=1280, height=500, bg=Color.BLACK).place(x=0, y=130)

sugarImage = PhotoImage(file="img/sugar/sugar.png")
sugarLabel = Label(app,
                   image=sugarImage,
                   bg=Color.BLACK,
                   bd=0)

sugarLabel.place(sugarFrame, x=450, y=150)

# 6. 달고나 모양 삽입(삼각형)
sugarLabel.bind('<Button>', clickSugar)
canvas = Canvas(app, bg=Color.SUGAR, bd=0, highlightthickness=0, relief='ridge', width=330)
canvas.place(sugarFrame, x=500, y=260)

# 삼각형 그리기
# 총 달고라 라인 갯수(달고나 라인 갯수만큼 클릭시 게임 성공)
drawTriangle(canvas)

# 창 실행
app.mainloop()
app.protocol('WM_DELETE_WINDOW', exit())
