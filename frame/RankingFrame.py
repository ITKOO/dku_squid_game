from tkinter import *
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from constant import Color
from frame import SGFrame

class RankingFrame(SGFrame.SGFrame):                #게임 종료 후 입력받은 이름을 저장받을 nameList
    nameList = []

    def __init__(self, parent):
        super(RankingFrame, self).__init__(parent)  #RankingFrame에서 클래스를 상속받음
        self.resist()

    def saveRankingUser(self, event, inputField):   #nameList에 이름을 추가하도록 하는 함수
        self.nameList.append(inputField.get())

    def resist(self):   #게임을 모두 통과했을 시, 플레이어가 이름을 등록할 수 있도록 하는 함수
        lb1 = Label(text="축하드립니다. 모든 게임을 통과하셨습니다.", bg="black", fg="white", font=(100))
        lb1.place(x=450, y=250)
        lb2 = Label(text="랭킹에 회원님의 정보를 올리기 위해 이름을 입력해주세요.", bg="black", fg="white", font=(100))
        lb2.place(x=400, y=300)
        #    lb3= Label(window,text=character_number,bg="black",fg="white",font=(100))
        #    lb3.place(x=455,y=300)     #main.py 캐릭터 선택창에 character_number 변수 넣어놨으니 코드 합칠 때 주석풀어주세요.
        inputText = Entry(width=30)
        inputText.place(x=500, y=500, width=200, height=30)
        b1 = Button(text="확인")
        b1.place(x=720, y=500)
        b1.bind("<Button>", lambda event, inputField=inputText: self.saveRankingUser(event, inputField))
        # b1 button -> nameList에 이름 추가

        b2 = Button(text="랭킹보기", bg="#393838", fg="white", height=5, width=42, font=(100))
        b2.place(x=409, y=550)
        b2.bind("<Button-1>", self.ranking)
        # b2 button -> ranking 화면으로 전환

    def ranking(self, event):   #nameList에 등록된 이름을 등록 순서대로 1대~3대까지 출력하는 함수
        photo = PhotoImage(file="img/ranking/랭킹.png")
        w = Label(image=photo)
        w.photo = photo
        w.pack()
        w.place(x=1, y=1)

        # nameList의 n번째 항목에 원소가 없을 경우 오류를 처리하기 위해 if문 사용
        if len(self.nameList) > 0:     
            first = Label(text=self.nameList[0], bg="black", fg="white", font="500")
            first.place(x=700, y=250)

        if len(self.nameList) > 1:
            second = Label(text=self.nameList[1], bg="black", fg="white", font="500")
            second.place(x=700, y=330)

        if len(self.nameList) > 2:
            third = Label(text=self.nameList[2], bg="black", fg="white", font="500")
            third.place(x=700, y=410)
