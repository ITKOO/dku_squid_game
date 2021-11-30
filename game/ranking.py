# 랭킹시스템
from tkinter import *

nameList = ["냠"]  # 게임종료후 입력받은 이름 name에 저장하기

window = Tk()
window.title("오징어게임")
window.geometry("1280x720")
window.configure(bg='black')


def saveRankingUser(event, inputField):
    nameList.append(inputField.get())
    print(nameList)

def resist(event):
#    photo = PhotoImage(file="img/ranking/money.png")
#    w = Label(window, image=photo, bd=0)
#    w.photo = photo
#    w.pack()
#    w.place(x=240, y=450)
    
    lb1= Label(window,text="축하드립니다. 모든 게임을 통과하셨습니다.",bg="black",fg="white",font=(100))
    lb1.place(x=450,y=250)
    lb2= Label(window,text="랭킹에       번 님의 정보를 올리기 위해 이름을 입력해주세요.",bg="black",fg="white",font=(100))
    lb2.place(x=400,y=300)
#    lb3= Label(window,text=character_number,bg="black",fg="white",font=(100))
#    lb3.place(x=455,y=300)     #main.py 캐릭터 선택창에 character_number 변수 넣어놨으니 코드 합칠 때 주석풀어주세요.
    inputText = Entry(window, width=30)
    inputText.place(x=500,y=500, width=200, height=30)
    b1 = Button(window, text="확인")
    b1.place(x=720,y=500)
    b1.bind("<Button>", lambda event, inputField=inputText: saveRankingUser(event, inputField))

    b2 = Button(window, text="랭킹보기", bg="#393838", fg="white", height=5, width=42, font=(100))
    b2.place(x=409, y=550)
    b2.bind("<Button-1>",ranking)
    
def ranking(event):
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
b.bind("<Button-1>", resist)

b.mainloop()
