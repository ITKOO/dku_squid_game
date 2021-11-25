# 할일 : 랭킹 저장

from tkinter import *

window = Tk()
window.title("오징어게임")
window.geometry("1280x720")
window.configure(bg='black')


def Exit(event):
    window.destroy()


def SecondFrame(event):
    photo = PhotoImage(file="img/description/환영.png")
    w = Label(window, image=photo)
    w.photo = photo
    w.pack()
    w.place(x=1, y=1)

    b = Button(window, text="다음", bg="grey", fg="white", height=2, width=5)
    b.place(x=1000, y=600)
    b.bind("<Button-1>", ThirdFrame)


def ThirdFrame(event):
    photo = PhotoImage(file="img/description/공지1.png")
    w = Label(window, image=photo)
    w.photo = photo
    w.pack()
    w.place(x=1, y=1)

    b = Button(window, text="다음", bg="grey", fg="white", height=2, width=5)
    b.place(x=1000, y=600)
    b.bind("<Button-1>", FourthFrame)


def FourthFrame(event):
    photo = PhotoImage(file="img/description/공지2.png")
    w = Label(window, image=photo)
    w.photo = photo
    w.pack()
    w.place(x=1, y=1)

    b = Button(window, text="다음", bg="grey", fg="white", height=2, width=5)
    b.place(x=1000, y=600)
    b.bind("<Button-1>", FifthFrame)


def FifthFrame(event):
    photo = PhotoImage(file="img/description/공지3.png")
    w = Label(window, image=photo)
    w.photo = photo
    w.pack()
    w.place(x=1, y=1)

    b = Button(window, text="다음", bg="grey", fg="white", height=2, width=5)
    b.place(x=1000, y=600)
    b.bind("<Button-1>", SixthFrame)


def SixthFrame(event):  # 시간이 지나면 화면 넘어가는거
    photo = PhotoImage(file="img/description/선택.png")
    w = Label(window, image=photo)
    w.photo = photo
    w.pack()
    w.place(x=1, y=1)

    b = Button(window, text="게임 그만두기", bg="grey", fg="white", height=5, width=40, font=(100))
    b.place(x=410, y=500)
    b.bind("<Button-1>", Exit)

    window.after(5000, SeventhFrame)  # 함수가 들어갈 자리라서 안들어가지는듯


def SeventhFrame():  # 캐릭터고르기,함수로 수정
    photo = PhotoImage(file="img/description/캐릭터.png")
    w = Label(window, image=photo)
    w.photo = photo
    w.pack()
    w.place(x=1, y=1)

    b1 = Button(window, text="", bg="white", height=6, width=20)
    b1.place(x=200, y=450)
    b2 = Button(window, text="", bg="white", height=6, width=20)
    b2.place(x=570, y=450)
    b3 = Button(window, text="", bg="white", height=6, width=20)
    b3.place(x=940, y=450)


# 메인화면 부분
photo = PhotoImage(file="img/description/메인 화면.png")
w = Label(window, image=photo)
w.photo = photo
w.pack()
b1 = Button(window, text="게임시작", bg="grey", fg="white", height=5, width=42, font=(100))
b1.place(x=409, y=363)
b1.bind("<Button-1>", SecondFrame)

b2 = Button(window, text="그만두기", bg="grey", fg="white", height=5, width=42, font=(100))
b2.place(x=409, y=546)
b2.bind("<Button-1>", Exit)
window.mainloop()
