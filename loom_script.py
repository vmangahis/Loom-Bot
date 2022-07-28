import pyautogui as auto
import os
import time


auto.FAILSAFE = True

auto.hotkey('alt', 'tab')
os.startfile('C:\\Users\\Shard\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Loom.lnk')

#Click Fullscreen
time.sleep(1.5)
auto.moveTo(180, 310)
time.sleep(1.5)
auto.click()

#click window
time.sleep(2)
auto.moveTo(200, 400)
time.sleep(1)
auto.click()

#Select App
time.sleep(2)
auto.moveTo(80, 210)
time.sleep(1)
auto.click()

#Start recording
time.sleep(2)
auto.hotkey('ctrl', 'shift', 'l')
time.sleep(1.55)

#Proceed
auto.moveTo(1040,588)
time.sleep(1.5)
auto.click()

#Actual Record
time.sleep(6.15)
auto.hotkey('playpause')
time.sleep(.9)
auto.hotkey('ctrl', 'shift', 'd')




#1942
