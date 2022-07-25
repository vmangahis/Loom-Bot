import pyautogui as pg
import time

time.sleep(5)

adj = open('adj.txt', 'r')

for x in adj:
    pg.write('Vince is ' + str(x))
    pg.press('Enter')
