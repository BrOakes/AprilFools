from ctypes import windll, Structure, c_ulong, byref
import time, random


class POINT(Structure):
    _fields_ = [("x", c_ulong), ("y", c_ulong)]


def mouseX():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return pt.x

def mouseY():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return pt.y

loop = 0
loopEnd = random.randrange(200,300)
horiz = random.choice([-1,1])
vert = random.choice([-1,0,1])
posX = int(mouseX())
posY = int(mouseY())
while loop < loopEnd:
    posX += horiz
    posY -= vert
    windll.user32.SetCursorPos(posX, posY)
    loop += 1
    time.sleep(0.002)


