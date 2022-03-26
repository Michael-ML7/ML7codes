# Python Spam Bot code
# Author: ML7

import pyautogui, time
def SendMessage():
    time.sleep(5)
    text = open("text.txt")
    for each_line in text:
        pyautogui.typewrite(each_line)
        pyautogui.press('enter')
SendMessage()
