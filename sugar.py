from tkinter import *


# 클릭 테스트용 함수
def clickSugar(event):
    print('click')


# 1. Tkinter 윈도우 창 생성
app = Tk()
app.title('달고나게임')
app.geometry('1280x720')
app['bg'] = 'black'
app.resizable(False, False)

# 2. 오른쪽 사이드 상단 작은 로고 삽입
small_logo_image = PhotoImage(file="img/sugar/small_logo.png")
side_logo_label = Label(app,
                        image=small_logo_image,
                        bd=0).place(x=1100, y=30)

# 3. 왼쪽 사이드 상단 타이머 표시
timer_label = Label(text='2:58',
                    fg='#FF387F',
                    font=('나눔스퀘어', 30)).place(x=50, y=30)

# TODO 4. 타이머 기능 설정

sugar_image = PhotoImage(file="img/sugar/sugar.png")
sugar_label = Label(app,
                    image=sugar_image,
                    bg='black',
                    bd=0)

sugar_label.place(x=450, y=150)

sugar_label.bind('<Button>', clickSugar)
canvas = Canvas(app, bg='#D0AD52', bd=0, highlightthickness=0, relief='ridge')
canvas.place(x=510, y=260)

for i in range(0, 150, 5):
    canvas.create_line(150 - i, i, (150 - (i + 5)), i + 5, width=10, fill='#C4C4C4')

for i in range(0, 250, 5):
    canvas.create_line(i, 150, i + 5, 150, width=10, fill='#C4C4C4')

# 점을 겁나 찍는다
# 점 클릭시 색상이 변경되고 상태도 변경된다
# 클릭된 갯수가 점 갯수랑 같을 때 통과 된다

# 사진을 라벨에 넣는다 라벨 누르면 사진이 바뀐다


app.mainloop()
app.protocol('WM_DELETE_WINDOW', exit())
