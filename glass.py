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

    b1 = Button(window, text=" ", height=5, width=20)  # 첫번째 버튼
    b1["bg"] = "white"
    b1.pack()
    b1.place(x=470, y=60)
    a = 1

    b2 = Button(window, text=" ", height=5, width=20)  # 두번째 버튼
    b2["bg"] = "white"
    b2.pack()
    b2.place(x=670, y=60)
    a = 1

    k = random.randint(1, 3)  # 랜덤을 사용하여 첫번째 두번째 버튼 중 탈락 버튼 결
    if k == 1:
        b1.bind("<Button-1>", fail)
    else:
        b2.bind("<Button-1>", fail)

    b3 = Button(window, text=" ", height=5, width=25)  # 세번째 버튼
    b3["bg"] = "white"
    b3.pack()
    b3.place(x=440, y=200)

    b4 = Button(window, text=" ", height=5, width=25)  # 네번째 버튼
    b4["bg"] = "white"
    b4.pack()
    b4.place(x=670, y=200)

    k = random.randint(1, 3)  # 랜덤을 사용하여 세번째 네번째 버튼 중 탈락 버튼 결정
    if k == 1:
        b3.bind("<Button-1>", fail)
    else:
        b4.bind("<Button-1>", fail)

    b5 = Button(window, text=" ", height=5, width=30)  # 다섯번째 버튼
    b5["bg"] = "white"
    b5.pack()
    b5.place(x=410, y=350)

    b6 = Button(window, text=" ", height=5, width=30)  # 여섯번째 버튼
    b6["bg"] = "white"
    b6.pack()
    b6.place(x=670, y=350)

    k = random.randint(1, 3)  # 랜덤을 사용하여 5번째 6번째 버튼 중 탈락 버튼 결정
    if k == 1:
        b5.bind("<Button-1>", fail)
    else:
        b6.bind("<Button-1>", fail)

    b7 = Button(window, text=" ", height=5, width=35)  # 7번째 버튼
    b7["bg"] = "white"
    b7.pack()
    b7.place(x=380, y=500)

    b8 = Button(window, text=" ", height=5, width=35)  # 8번째 버튼
    b8["bg"] = "white"
    b8.pack()
    b8.place(x=670, y=500)

    k = random.randint(1, 3)  # 랜덤을 사용하여 7번째 8번째 버튼 중 탈락 버튼 결정
    if k == 1:
        b7.bind("<Button-1>", fail)
    else:
        b8.bind("<Button-1>", fail)

    b9 = Button(window, text=" ", height=5, width=40)  # 9번째 버튼
    b9["bg"] = "white"
    b9.pack()
    b9.place(x=350, y=650)

    b10 = Button(window, text=" ", height=5, width=40)  # 10번째 버튼
    b10["bg"] = "white"
    b10.pack()
    b10.place(x=670, y=650)

    k = random.randint(1, 3)  # 랜덤을 사용하여 9번째 10번째 버튼 중 탈락 버튼 결정
    if k == 1:
        b9.bind("<Button-1>", fail)
    else:
        b10.bind("<Button-1>", fail)

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
