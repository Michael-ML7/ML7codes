# Python Spam Bot code
# Author: ML7

import pyautogui, time
def SendMessage():
    time.sleep(5)
    text = open("text.txt") # to be created and this will be your text
    for each_line in text:
        pyautogui.typewrite(each_line)
        pyautogui.press('enter')
SendMessage()
