from util import Colors
from util import Drawer
from util.window import CreateWindow as win

train_body = [80, 460, 150, 100]
train_body_1 = [230, 380, 100, 180]
window_body = [245, 395, 65, 65]
pipe_1s = [105, 460]; pipe_1e = [105, 420]
pipe_2s = [140, 460]; pipe_2e = [140, 420]
pipe_3s = [105, 420]; pipe_3e = [140, 420]
coach_body = [365, 395, 300, 165]
chain_S = [330, 530]; chain_E = [365, 530]
wheel_1 = [110, 585]; wheel_2 = [275, 585]; wheel_3 = [400, 585]
wheel_4 = [465, 585]; wheel_5 = [575, 585]; wheel_6 = [640, 585]
smoke_1 = [120, 375]; smoke_2 = [150, 340]; smoke_3 = [190, 304]

def draw():
    Drawer.drawRect(win.window, Colors.OLD_TRAIN_BODY, train_body, 0)
    Drawer.drawRect(win.window, Colors.OLD_TRAIN_BODY, train_body_1, 0)
    Drawer.drawRect(win.window, Colors.OLD_TRAIN_WINDOW, window_body, 0)

    Drawer.drawLine(win.window, Colors.BROWN, pipe_1s, pipe_1e, 5)
    Drawer.drawLine(win.window, Colors.BROWN, pipe_2s, pipe_2e, 5)
    Drawer.drawLine(win.window, Colors.BROWN, pipe_3s, pipe_3e, 5)

    Drawer.drawRect(win.window, Colors.OLD_TRAIN_COACH, coach_body, 0)
    Drawer.drawLine(win.window, Colors.BLACK, chain_S, chain_E, 5)

    Drawer.drawCircle(win.window, Colors.OLD_TRAIN_WHEELS, wheel_1, 25, 0)
    Drawer.drawCircle(win.window, Colors.OLD_TRAIN_WHEELS, wheel_2, 25, 0)
    Drawer.drawCircle(win.window, Colors.OLD_TRAIN_WHEELS, wheel_3, 25, 0)
    Drawer.drawCircle(win.window, Colors.OLD_TRAIN_WHEELS, wheel_4, 25, 0)
    Drawer.drawCircle(win.window, Colors.OLD_TRAIN_WHEELS, wheel_5, 25, 0)
    Drawer.drawCircle(win.window, Colors.OLD_TRAIN_WHEELS, wheel_6, 25, 0)

    Drawer.drawCircle(win.window, Colors.OLD_TRAIN_SMOKE, smoke_1, 10, 0)
    Drawer.drawCircle(win.window, Colors.OLD_TRAIN_SMOKE, smoke_2, 20, 0)
    Drawer.drawCircle(win.window, Colors.OLD_TRAIN_SMOKE, smoke_3, 30, 0)
def update():
    print(0)