from pynput import keyboard
from pynput.keyboard import Controller as KeyboardController
from pynput.keyboard import Key
import pyautogui as pg
from discord import utils
import threading
import random
import time
import os
FLAG = True

counter = 0
first = 0
last = 0


current_time = time.strftime("%H:%M:%S", time.localtime())
print('-'*33)
print(f'The time of starting is: {current_time}')
print('-'*33 + '\n\n')

def send(message):
    keyboard1 = KeyboardController()

    keyboard1.type(message)
    keyboard1.press(Key.enter)
    keyboard1.release(Key.enter)

def findButton():
    color = (88, 101, 242)
    clicked = False
    s = pg.screenshot()
    for x in range(s.width):
        for y in range(s.height):
            if s.getpixel((x, y)) == color:
                pg.click(x, y)
                clicked = True
                break 
        if clicked == True:
            break
    keyboard2 = KeyboardController()
    keyboard2.press(Key.tab)
    keyboard2.release(Key.tab)


def search_loop(counter, first, last):
    time.sleep(5)

    while FLAG:
        send('pls search')
        time.sleep(3)
        findButton()
        print("Pressed the button succesfully")
        send('pls postmeme')
        time.sleep(3)
        findButton()
        print("pressed the button succesfully")
        send('pls dig')
        time.sleep(2)
        print("sent pls dig")
        send('pls hunt')
        time.sleep(1)
        print("sent pls hunt")
        send("pls beg")
        time.sleep(1)
        print('Sent pls beg')
        send("pls dep all")
        print('sent pls dep all')
        time.sleep(random.randint(34, 37))


threads = [threading.Thread(target=search_loop(counter, first, last))]

for thread in threads:
    thread.start()
