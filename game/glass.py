import random
from tkinter import *

window = Tk()
window.title("오징어게임")
window.geometry("1280x720")
window.configure(bg='black')


def fail(event):  # 유리 사다리 게임 실패시 실패 화면이 나오게 하는 함수 정의
    photo = PhotoImage(file="img/glass/오징어.png")
    w = Label(window, image=photo, bg="black")
    w.photo = photo
    w.pack()
    w.place(x=1, y=20)

def goal(event):  # 게임 성공시 나오는 goal 함수 정의
    end = Button(None, text="골인")
    end.pack()
    end.bind("<Button-1>", goal)
    end.place(x=625, y=30)
    photo = PhotoImage(file="img/glass/오징어게임 성공.png")
    w = Label(window, image=photo)
    w.photo = photo
    w.pack()


def glass(event):  # 유리 사다리 게임 실행 화면
    photo = PhotoImage(file="img/glass/오징어게임 유리다리.png")
    w = Label(window, image=photo)
    w.photo = photo
    w.pack()

    b1 = Button(window, text=" ", height=5, width=20)
    b1["bg"] = "white"
    b1.pack()
    b1.place(x=480, y=70)
    b1.bind("<Button-1>", goal)

    b2 = Button(window, text=" ", height=5, width=20)
    b2["bg"] = "white"
    b2.pack()
    b2.place(x=670, y=70)
    b2.bind("<Button-1>", goal)

    for t in range(3, 11, 2):  # 반복문 사용
        for i in range(3, 11, 2):
            bi = Button(window, text=" ", height=5, width=5 * (i + 3))  # 홀수번 버튼 생성
            bi["bg"] = "white"
            bi.pack()
            bi.place(x=510 - (i * 30), y=60 + (i - 1) * 70)

            bt = Button(window, text=" ", height=5, width=5 * (i + 3))  # 짝수번 버튼 생성
            bt["bg"] = "white"
            bt.pack()
            bt.place(x=670, y=60 + (i - 1) * 70)

            k = random.randint(1, 2)  # 랜덤을 사용하여 홀수,짝수 버튼 중 탈락 버튼 결정
            if k == 1:
                bi.bind("<Button-1>", fail)

            else:
                bt.bind("<Button-1>", fail)

    window.mainloop()


start = Button(None, text="시작하기")  # 시작버튼 생성
start.pack()
start.bind("<Button-1>", glass)

start.mainloop()