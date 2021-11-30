import sys, os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from model import SGWindow
from model import HomeFrame

window = SGWindow.SGWindow('오징어게임', False)
homeFrame = HomeFrame.HomeFrame(window.root)
homeFrame.mainloop()



