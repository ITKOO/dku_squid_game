from tkinter import *
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from constant import Color

# 2021.11.30 @구지원
# 게임에서 사용될 기본 프레임 클래스
class SGFrame(Frame):
    def __init__(self, parent):
        super(SGFrame, self).__init__(parent)
        self.config(width=1280, height=800, bg=Color.BLACK)
        self.place(x=0, y=130)