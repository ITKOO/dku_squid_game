import random
from tkinter import *
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from constant import Color
from model import SGFrame
from model import FailedFrame

class GlassFrame(SGFrame.SGFrame):
    def __init__(self, parent):
        super(GlassFrame, self).__init__(parent)
        self.glass()

    def fail(self, event):  # 유리 사다리 게임 실패시 실패 화면이 나오게 하는 함수 정의
       self.failedFrame = FailedFrame.FailedFrame(self)

    def goal(self, event):  # 게임 성공시 나오는 goal 함수 정의
        end = Button(None, text="골인")
        end.pack()
        end.bind("<Button-1>", self.goal)
        end.place(x=625, y=30)
        photo = PhotoImage(file="../img/glass/오징어게임 성공.png")
        w = Label(image=photo)
        w.photo = photo
        w.pack()

    def glass(self):  # 유리 사다리 게임 실행 화면
        photo = PhotoImage(file="../img/glass/오징어게임 유리다리.png")
        w = Label(image=photo)
        w.photo = photo
        w.pack()

        b1 = Button(text=" ", height=5, width=20)
        b1["bg"] = "white"
        b1.pack()
        b1.place(x=480, y=70)
        b1.bind("<Button-1>", self.goal)

        b2 = Button(text=" ", height=5, width=20)
        b2["bg"] = "white"
        b2.pack()
        b2.place(x=670, y=70)
        b2.bind("<Button-1>", self.goal)

        for t in range(3, 11, 2):  # 반복문 사용
            for i in range(3, 11, 2):
                bi = Button(text=" ", height=5, width=5 * (i + 3))  # 홀수번 버튼 생성
                bi["bg"] = "white"
                bi.pack()
                bi.place(x=510 - (i * 30), y=60 + (i - 1) * 70)

                bt = Button(text=" ", height=5, width=5 * (i + 3))  # 짝수번 버튼 생성
                bt["bg"] = "white"
                bt.pack()
                bt.place(x=670, y=60 + (i - 1) * 70)

                k = random.randint(1, 2)  # 랜덤을 사용하여 홀수,짝수 버튼 중 탈락 버튼 결정
                if k == 1:
                    bi.bind("<Button-1>", self.fail)

                else:
                    bt.bind("<Button-1>", self.fail)