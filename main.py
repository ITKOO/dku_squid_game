# 할일 : 랭킹 저장
# 2021/11/25/ 첫 시작 화면
# 테스트 주석

#설명문 부분
from tkinter import *

window = Tk()
window.title("오징어게임")
window.geometry("1280x720")
window.configure(bg='black')


def Exit(event):
    window.destroy()


def SecondFrame(event): #첫번째 안내문
    photo = PhotoImage(file="img/description/검은화면.png")
    w = Label(window, image=photo)
    w.photo = photo
    w.pack()
    w.place(x=1, y=1)
    lb= Label(window,text="이자리에 오신 여러분을 진심으로 환영합니다",bg="black",fg="white",font=(100))
    lb.place(x=450,y=350)

    b = Button(window, text="다음", bg="grey", fg="white", height=2, width=5)
    b.place(x=1000, y=600)
    b.bind("<Button-1>", ThirdFrame)


def ThirdFrame(event):
    photo = PhotoImage(file="img/description/검은화면.png")
    w = Label(window, image=photo)
    w.photo = photo
    w.pack()
    w.place(x=1, y=1)
    lb= Label(window,text="여러분들은 앞으로 10분간 모두 2개의 게임에 참가하시게 됩니다.",bg="black",fg="white",font=(100))
    lb.place(x=360,y=350)

    b = Button(window, text="다음", bg="grey", fg="white", height=2, width=5)
    b.place(x=1000, y=600)
    b.bind("<Button-1>", FourthFrame)


def FourthFrame(event):
    photo = PhotoImage(file="img/description/검은화면.png")
    w = Label(window, image=photo)
    w.photo = photo
    w.pack()
    w.place(x=1, y=1)
    lb= Label(window,text="두 개의 게임을 모두 이긴 분들께는 거액의 00이 지급됩니다.",bg="black",fg="white",font=(100))
    lb.place(x=400,y=350)

    b = Button(window, text="다음", bg="grey", fg="white", height=2, width=5)
    b.place(x=1000, y=600)
    b.bind("<Button-1>", FifthFrame)


def FifthFrame(event):
    photo = PhotoImage(file="img/description/검은화면.png")
    w = Label(window, image=photo)
    w.photo = photo
    w.pack()
    w.place(x=1, y=1)
    lb= Label(window,text="모두에게 공정한 게임을 위해 게임 정보는 사전에 공개할 수 없습니다.",bg="black",fg="white",font=(100))
    lb.place(x=350,y=350)

    b = Button(window, text="다음", bg="grey", fg="white", height=2, width=5)
    b.place(x=1000, y=600)
    b.bind("<Button-1>", SixthFrame)


def SixthFrame(event):  # 시간이 지나면 화면 넘어가는거
    photo = PhotoImage(file="img/description/검은화면.png")
    w = Label(window, image=photo)
    w.photo = photo
    w.pack()
    w.place(x=1, y=1)
    lb= Label(window,text="게임에 참가를 원하지 않는 분께서는 지금 아래 버튼을 눌러주시기 바랍니다.",bg="black",fg="white",font=(100))
    lb.place(x=320,y=350)

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
photo = PhotoImage(file="img/description/로고.png")
w = Label(window, image=photo,bd=0)
w.photo = photo
w.pack()
w.place(x=280,y=80)

b1 = Button(window, text="게임시작", bg="grey", fg="white", height=5, width=42, font=(100))
b1.place(x=409, y=333)
b1.bind("<Button-1>", SecondFrame)

b2 = Button(window, text="그만두기", bg="grey", fg="white", height=5, width=42, font=(100))
b2.place(x=409, y=576)
b2.bind("<Button-1>", Exit)

b2 = Button(window, text="랭킹보기", bg="grey", fg="white", height=5, width=42, font=(100))
b2.place(x=409, y=454)
b2.bind("<Button-1>", Exit)

window.mainloop()
