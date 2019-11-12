import os
import pyautogui as pygui
from time import sleep

os.startfile(r"C:\Program Files (x86)\Microsoft Office\root\Office16\EXCEL.EXE")
sleep(9)

pygui.moveTo(100, 220)
sleep(0.5)  
pygui.click()
pygui.moveTo(90, 280)
sleep(1)
pygui.click()
pygui.hotkey('ctrl', 'shift', 'down')
pygui.hotkey('ctrl', 'c')