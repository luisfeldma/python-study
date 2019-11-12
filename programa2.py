import os
import pyautogui
from time import sleep

site = 'https://capra.fclar.unesp.br/moodle/'
user = 'luisfelipe'
senha = 'Miranda2801'

os.startfile(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
sleep(5)
pyautogui.typewrite(site)

pyautogui.press('enter')
sleep(5)
          
pyautogui.press('tab', 3)

pyautogui.press('enter')   
sleep(3)
pyautogui.press('tab', 7)

pyautogui.typewrite(user)       
pyautogui.press('tab', 2)

pyautogui.press(senha)
pyautogui.press('tab')
pyautogui.press('enter')

