# pip install pyautogui
# pip install pandas openpyxl numpy

import pyautogui
import time
import datetime

pyautogui.PAUSE = 0.6
#Find the App t/Access
pyautogui.press('win')
pyautogui.write("")
time.sleep(3)
pyautogui.press('enter')

time.sleep(5)
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('enter')

time.sleep(5)
#pyautogui.click(x=25, y=358)
#pyautogui.doubleClickpress()
#pyautogui.doubleClick(x=30, y=360)

#Find the Other -> Access It
pyautogui.press('win')
time.sleep(3)
pyautogui.write("")
time.sleep(3)

pyautogui.press('enter')
time.sleep(4)
pyautogui.hotkey('shift', 'tab')
pyautogui.press('enter')
time.sleep(4)
#pyautogui.write("")

#pyautogui.write("")
#time.sleep(6)
#pyautogui.hotkey('shift', '2')
#time.sleep(5)
#pyautogui.write("")
#time.sleep(6)
#pyautogui.press('tab')
#pyautogui.press('tab')

pyautogui.press('capslock')
time.sleep(2)
pyautogui.press('')
time.sleep(1)
pyautogui.press('')
time.sleep(1)
pyautogui.press('')
time.sleep(1)
pyautogui.press('capslock')
time.sleep(1)
pyautogui.hotkey('shift', '2')
time.sleep(1)
pyautogui.press('')
time.sleep(1)
pyautogui.press('')
time.sleep(1)
pyautogui.press('')
time.sleep(1)
pyautogui.press('')
time.sleep(3)
pyautogui.press('enter')

time.sleep(5)
pyautogui.hotkey('shift', 'tab')
pyautogui.press('enter')

#time.sleep(7)
#pyautogui.hotkey('shift', 'tab')
time.sleep(4)
pyautogui.click(x=716, y=454)
pyautogui.hotkey('ctrl', 'a')

#Insert the Credentials..
time.sleep(3)
pyautogui.write("")
time.sleep(4)
pyautogui.press('tab')
pyautogui.write("")

time.sleep(3)
pyautogui.press('tab')
pyautogui.press('enter')

time.sleep(7)
#19tabs

for _ in range(18):
    pyautogui.press('tab')

time.sleep(2)
pyautogui.press('enter')

time.sleep(5)
pyautogui.press('enter')
time.sleep(2)
pyautogui.press('alt')

time.sleep(2)
pyautogui.hotkey('ctrl', 'right')
pyautogui.hotkey('ctrl', 'right')
pyautogui.press('enter')
time.sleep(2)

for _ in range(10):
    pyautogui.hotkey('ctrl', 'down')
pyautogui.press('enter')

time.sleep(4)
pyautogui.press('a')
pyautogui.press('backspace')

time.sleep(3)
pyautogui.hotkey('ctrl', 'down')
pyautogui.press('enter')
pyautogui.write("01/01/2024")
time.sleep(2)
pyautogui.press('enter')

data_atual = datetime.datetime.now().strftime("%d/%m/%y")
time.sleep(2)
pyautogui.write(data_atual)


time.sleep(2)
pyautogui.press('enter')

time.sleep(2)
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('enter')

time.sleep(50)
for _ in range(6):
    pyautogui.press('tab')
time.sleep(2)
pyautogui.press('enter')

time.sleep(70)
#pyautogui.hotkey('alt', 'tab')
pyautogui.click(x=376, y=876)
time.sleep(5)

pyautogui.hotkey('ctrl', 'shift', 'right')
time.sleep(2)
pyautogui.hotkey('ctrl', 'shift', 'down')
time.sleep(2)
pyautogui.hotkey('ctrl', 'c')

time.sleep(5)
pyautogui.press('win')
time.sleep(2)
pyautogui.write("Excel")
time.sleep(2)
pyautogui.press('enter')

time.sleep(4)
pyautogui.press('enter')
time.sleep(2)
pyautogui.hotkey('ctrl', 'v')

time.sleep(4)
pyautogui.hotkey('ctrl', 'down')
time.sleep(4)
pyautogui.press('down')

time.sleep(4)
pyautogui.keyDown('alt')
pyautogui.press('tab')
pyautogui.press('right')
pyautogui.keyUp('alt')

#time.sleep(14)
time.sleep(2)
for _ in range(12):
    pyautogui.hotkey('shift', 'tab')
pyautogui.press('backspace')

time.sleep(3)
for _ in range(4):
    #pyautogui.hotkey('ctrl', 'down')
    pyautogui.press('down')
    time.sleep(2)
pyautogui.press('enter')

time.sleep(4)
for _ in range(5):
    pyautogui.press('tab')
pyautogui.press('enter')

time.sleep(50)
pyautogui.keyDown('alt')
pyautogui.press('tab')
pyautogui.press('right')
pyautogui.keyUp('alt')

time.sleep(10)
#pyautogui.hotkey('alt', 'f4')
#pyautogui.hotkey('alt', 'f4')
pyautogui.click(x=1407, y=0)
time.sleep(3)
#pyautogui.click(x=644, y=493)
#pyautogui.hotkey('shift', 'tab')
pyautogui.click(x=728, y=487)
time.sleep(2)
pyautogui.click(x=732, y=501)
#pyautogui.press('enter')
time.sleep(2)
pyautogui.click(x=304, y=881)

time.sleep(8)
for _ in range(6):
    pyautogui.press('tab')
pyautogui.press('enter')

time.sleep(90)
pyautogui.click(x=359, y=867)

#pyautogui.keyDown('alt')
#pyautogui.press('tab')
#pyautogui.press('right')
#pyautogui.keyUp('alt')
time.sleep(4)
pyautogui.press('down')
time.sleep(3)
pyautogui.hotkey('ctrl', 'shift', 'right')
time.sleep(3)
pyautogui.hotkey('ctrl', 'shift', 'down')
time.sleep(3)
pyautogui.hotkey('ctrl', 'c')
time.sleep(5)
pyautogui.click(x=210, y=885)
#pyautogui.keyDown('alt')
#pyautogui.press('tab')
#pyautogui.press('right')
#pyautogui.keyUp('alt')
time.sleep(3)
pyautogui.hotkey('ctrl', 'v')
time.sleep(3)
pyautogui.hotkey('ctrl', 'down')

time.sleep(2)
pyautogui.press('alt')
pyautogui.press('a')
pyautogui.press('a')
pyautogui.press('y')
pyautogui.press('4')

time.sleep(6)
pyautogui.write("")

time.sleep(7)
for _ in range(7):
    pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(6)
pyautogui.hotkey('shift', 'tab')
time.sleep(4)
pyautogui.press('enter')

time.sleep(4)
pyautogui.hotkey('alt', 'f4')

time.sleep(10)
pyautogui.click(x=1407, y=0)
#pyautogui.hotkey('alt', 'f4')
#pyautogui.hotkey('alt', 'f4')
time.sleep(10)
pyautogui.click(x=713, y=495)
#pyautogui.hotkey('shift', 'tab')
#pyautogui.press('enter')
time.sleep(6)
pyautogui.click(x=1423, y=4)
time.sleep(10)
pyautogui.click(x=733, y=490)
#pyautogui.click(x=732, y=501)

time.sleep(10)
pyautogui.click(x=1418, y=12)
pyautogui.click(x=1414, y=0)
#pyautogui.hotkey('alt', 'f4')
time.sleep(10)
pyautogui.click(x=1414, y=7)
time.sleep(10)
pyautogui.click(x=779, y=505)
#pyautogui.hotkey('alt', 'f4')

#pyautogui.hotkey('shift', 'tab')
#pyautogui.press('enter')
time.sleep(8)
pyautogui.click(x=1028, y=13)
time.sleep(4)
pyautogui.press('enter')
