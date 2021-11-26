import random
from tkinter import *

window = Tk()
a = 0


def fail(event):  # 유리 사다리 게임 실패시 실패 화면이 나오게 하는 함수 정의
    photo = PhotoImage(file="img/glass/오징어게임 실패화면.png")
    w = Label(window, image=photo)
    w.photo = photo
    w.pack()
    w.place(x=1, y=20)
    a = 0  # 게임 시작과 함께 a=0으로 할당
    return 0


def glass(event):  # 유리 사다리 게임 실행 화면
    photo = PhotoImage(file="img/glass/오징어게임 유리다리.png")
    w = Label(window, image=photo)
    w.photo = photo
    w.pack()

    for t in range(2, 11, 2):  # 반복문 사용
        for i in range(1, 11, 2):
            bi = Button(window, text=" ", height=5, width=5 * (i + 3))  # 홀수번 버튼 생성
            bi["bg"] = "white"
            bi.pack()
            bi.place(x=510 - (i * 30), y=60 + (i - 1) * 70)
            a = 1

            bt = Button(window, text=" ", height=5, width=5 * (i + 3))  # 짝수번 버튼 생성
            bt["bg"] = "white"
            bt.pack()
            bt.place(x=670, y=60 + (i - 1) * 70)
            a = 1

            k = random.randint(1, 3)  # 랜덤을 사용하여 홀수,짝수 버튼 중 탈락 버튼 결정
            if k == 1:
                bi.bind("<Button-1>", fail)
            else:
                bt.bind("<Button-1>", fail)

    window.mainloop()


if a != 0:  # 성공했을 경우 a는 계속 0이므로 성공했을 경우 성공화면
    photo = PhotoImage(file="img/glass/오징어게임 성공.png")
    w = Label(window, image=photo)
    w.photo = photo
    w.pack()

start = Button(None, text="시작하기")  # 시작버튼 생성
start.pack()
start.bind("<Button-1>", glass)

start.mainloop()
