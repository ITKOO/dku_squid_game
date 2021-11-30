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

    def moveHome(self): #게임 메인화면 부분
        #description의 로고.png 파일을 불러와서 적용
        self.photo = PhotoImage(file="../img/description/로고.png")
    def moveHome(self):
        self.photo = PhotoImage(file="img/description/로고.png")
        self.w = Label(image=self.photo,bd=0)
        #bd=0으로 해야 테두리에 흰 선이 생기지 않음.
        self.w.photo = self.photo
        self.w.pack()
        self.w.place(x=250,y=30)
        
        self.startButton = Label(text='게임 시작하기', fg=Color.WHITE, bg=Color.GRAY, bd=0, font=('맑은 고딕', 25), width=20, height=2)
        self.startButton.place(x=450, y=450)
        self.startButton.bind('<Button-1>', self.startGame)
        #게임시작하기 button -> strartGame 이벤트 실행 (게임 설명 시작)

        self.lankingButton = Label(text='랭킹 보기', fg=Color.WHITE, bg=Color.GRAY, bd=0, font=('맑은 고딕', 25), width=20, height=2)
        self.lankingButton.place(x=450, y=600)
        self.lankingButton.bind('<Button>', self.viewRanking)
        #랭킹 보기 button -> viewRanking 이벤트 실행 (랭킹 화면으로 이동)


    def startGame(self, event):
        self.removeHomeButton()     #이전 화면의 라벨과 버튼 삭제
        self.descriptionFrame = DescriptionFrame.DescriptionFrame(self)
        # 게임 설명 화면으로 넘어가는 함수

    def viewRanking(self, event):
        self.removeHomeButton()     #이전 화면의 라벨과 버튼 삭제
        self.rankingFrame = RankingFrame.RankingFrame(self)
        # 랭킹 화면으로 넘어가는 함수

    def removeHomeButton(self):     #이전 화면의 요소를 삭제하는 함수
        self.startButton.destroy()
        self.lankingButton.destroy()
        self.w.destroy()

