# 랭킹시스템
from tkinter import *

window = Tk()
window.title("오징어게임")
window.geometry("1280x720")
window.configure(bg='black')


def ranking(event):
    name = ["이채린", "구지원", "최지은"]  # 게임종료후 입력받은 이름 name에 저장하기
    photo = PhotoImage(file="img/ranking/랭킹.png")
    w = Label(window, image=photo)
    w.photo = photo
    w.pack()
    w.place(x=1, y=1)

    first = Label(window, text=name[0], bg="black", fg="white", font="500")
    first.place(x=700, y=250)

    second = Label(window, text=name[1], bg="black", fg="white", font="500")
    second.place(x=700, y=330)
    third = Label(window, text=name[2], bg="black", fg="white", font="500")
    third.place(x=700, y=410)
    window.mainloop()


b = Button(None, text="랭킹")
b.pack()
b.bind("<Button-1>", ranking)

b.mainloop()
