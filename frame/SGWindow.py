from tkinter import *

import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from constant import Color

# 2021.11.30 @구지원
# 기본 창 관련 클래스
class SGWindow():
    def __init__(self, title, isTimerShow):
        # 1. 윈도우 기본 설정(이름, 창크기, 배경색 ..)
        self.root = Tk()
        self.root.title(title)
        self.root.geometry('1280x720')
        self.root['bg'] = Color.BLACK
        self.root.resizable(False, False)

        # 2. 오른쪽 사이드 상단 작은 로고 삽입
        self.setSideLogoImage()

    # 오른쪽 사이드 로고 이미지를 설정하는 함수
    def setSideLogoImage(self):
        self.smallLogoImage = PhotoImage(file="img/sugar/small_logo.png")
        self.sideLogoLabel = Label(self.root,
                                   image=self.smallLogoImage,
                                   bd=0)
        self.sideLogoLabel.place(x=1100, y=30)