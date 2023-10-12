import win32api, win32con, win32gui
import time
import mouse

def move(x,y):
    win32api.SetCursorPos((x,y))
    
def click():
    mouse.click('right')

print('Start')    
flag = 0
while True:
    flags, hcursor, (x,y) = win32gui.GetCursorInfo()
    if flag == 0:
        move(x + 10,y)
        time.sleep(1)
        click()
        flag = 1
    else:
        move(x - 10,y)
        time.sleep(1)
        click()
        flag = 0
    time.sleep(300)