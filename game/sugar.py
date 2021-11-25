from tkinter import *

from constant import Color
from model.Point import Point

# 상수 선언
STARTING_POINT = 140
STANDARD_POINT_X = 160
POINT_RANGE = 30


# 달고나 선택시 실행되는 함수(게임 실패)
def clickSugar(event):
    print('click')


# 달고나 모양 라인 클릭시 실행되는 함수(게임 성공)
def clickLine(event, canvas, lineElement):
    canvas.itemconfig(lineElement, fill='#D54C7E')
    print(lineElement)


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
    for i in range(start, end, pointRange):
        pointList = getPointsByLocation(location, i)
        line = canvas.create_line(pointList[0].x, pointList[0].y, pointList[1].x, pointList[1].y, width=10,
                                  fill='#C4C4C4')
        canvas.tag_bind(line, "<Button>", lambda event, item=line: clickLine(event, canvas, item))


# 삼각형 변의 위치에 따라 좌표를 정해 라인을 그리는 함수
def getPointsByLocation(location, value):
    pointList = []
    point1 = ''
    point2 = ''

    if location == 'LEFT':
        point1 = Point(STANDARD_POINT_X - value, value)
        point2 = Point((STANDARD_POINT_X - (value + POINT_RANGE)), value + POINT_RANGE)

    if location == 'RIGHT':
        point1 = Point(STANDARD_POINT_X + value, value)
        point2 = Point((STANDARD_POINT_X + (value + POINT_RANGE)), value + POINT_RANGE)

    if location == 'BOTTOM':
        point1 = Point(value, STARTING_POINT)
        point2 = Point(value + POINT_RANGE, STARTING_POINT)

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
                   font=('맑은 고딕', 35)).place(x=50, y=30)

# TODO 4. 타이머 기능 설정

# 5. 달고나 몸판 그리기
sugarImage = PhotoImage(file="img/sugar/sugar.png")
sugarLabel = Label(app,
                   image=sugarImage,
                   bg=Color.BLACK,
                   bd=0)

sugarLabel.place(x=450, y=150)

# 6. 달고나 모양 삽입(삼각형)
sugarLabel.bind('<Button>', clickSugar)
canvas = Canvas(app, bg=Color.SUGAR, bd=0, highlightthickness=0, relief='ridge', width=330)
canvas.place(x=500, y=260)

# 삼각형 그리기
drawTriangle(canvas)

# 창 실행
app.mainloop()
app.protocol('WM_DELETE_WINDOW', exit())
