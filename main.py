import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from frame import HomeFrame
from frame import SGWindow


window = SGWindow.SGWindow('오징어게임', False)
homeFrame = HomeFrame.HomeFrame(window.root)
homeFrame.mainloop()



