import os
from pynput.keyboard import Key, Controller
from pynput.mouse import Button, Controller
from time import sleep

keyboard = Controller()

#site = "https://capra.fclar.unesp.br/moodle/"


os.startfile(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
sleep(2)    
#for l in range(0, len(site)):
    #keyboard.press(site[l])
    #keyboard.release(site[l])
keyboard.press(Key.enter)
keyboard.release(Key.enter)
    
keyboard.press('h')
keyboard.release('h')
keyboard.press('t')
keyboard.release('t')
#keyboard.press(site[5])
#keyboard.release(site[5])
#keyboard.press(f'{site[7]}')
#keyboard.release(f'{site[7]}')