import sys, os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from model import SGWindow
from model import HomeFrame
from model import SugarFrame
from model import RankingFrame
from model import GlassFrame

window = SGWindow.SGWindow('오징어게임', False)
# homeFrame = GlassFrame.GlassFrame(window.root)
homeFrame = HomeFrame.HomeFrame(window.root)
# homeFrame = SugarFrame.SugarFrame(window.root)
homeFrame.mainloop()



