from tkinter import *
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from constant import Color
from frame import SGFrame
from frame import HomeFrame

# 2021.11.30 @구지원
# 게임 실패 화면 클래스
class FailedFrame(SGFrame.SGFrame):
    def __init__(self, parent):
        super(FailedFrame, self).__init__(parent)
        self.gameFrame = Frame(width=1280, height=500, bg=Color.BLACK)
        self.gameFrame.place(x=0, y=130)

        self.label = Label(self.gameFrame, text='탈락입니다.\n\n당신은 오징어 입니다.', fg=Color.WHITE,
                           bg=Color.BLACK, font=('맑은 고딕', 25), width=20, height=10)
        self.label.place(x=480, y=0)

        # 상단, 하단에 오징어 이미지 삽입
        self.squidImage = PhotoImage(file="img/description/squid.png")
        self.setSquidImage(30, 0)
        self.setSquidImage(800,160)

        # 하단 시작화면으로 돌아가기 버튼
        self.setMoveHomeButton()

    # 오징어 이미지를 set하는 함수
    def setSquidImage(self, xCoordinate, yCoordinate):
        squidImageLabel = Label(self.gameFrame, image=self.squidImage, bg=Color.BLACK, bd=0)
        squidImageLabel.place(x=xCoordinate, y=yCoordinate)

    # 시작화면으로 돌아가는 함수
    def setMoveHomeButton(self):
        self.homeButton = Label(self.gameFrame, text='시작화면으로 돌아가기', fg=Color.WHITE, bg=Color.GRAY, bd=0, font=('맑은 고딕', 25), width=20,
                                height=2)
        self.homeButton.place(x=490, y=300)
        self.homeButton.bind('<Button>', self.moveHome)

    def moveHome(self, event):
        self.gameFrame.destroy()
        self.homeFrame = HomeFrame.HomeFrame(self)