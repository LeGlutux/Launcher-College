import pyautogui as pt
from time import sleep

# Helper function


def write(str):
    for letter in str:
        if letter == " ":
            sleep(0.1)
            pt.press("enter")
            sleep(0.5)
        else: 
            pt.press(letter)


def nav_to_image(img, clicks=1, off_x=0, off_y=0):
    position = pt.locateCenterOnScreen('images/'+img+'.PNG', confidence=.8)

    if position is None:
        print(f'{img} not found...')
        return 0
    else:
        pt.moveTo(position, duration=.1)
        pt.moveRel(off_x, off_y, duration=.1)
        pt.click(clicks=clicks, interval=.2)


def locate(img):
    position = pt.locateCenterOnScreen('images/'+img+'.PNG', confidence=.8)

    if position is None:
        return False
    else:
        return True

def altTab():
   
    pt.keyDown('alt')
    pt.press('tab')
    pt.keyUp('alt')

def deskTop():
    pt.keyDown('win')
    pt.press('d')
    pt.keyUp('win')

def waitAndClick(string):
    while locate(string) == False:
        print("waiting")
    nav_to_image(string, 2)

def newTab():
    pt.keyDown("ctrl")
    pt.press("t")
    pt.keyUp("ctrl")

# Launch setup

counter = 0

pt.press('win')
sleep(0.1)
write('ordi p p mat lpb 3e')

pt.keyDown('ctrl')
pt.press('enter')
pt.keyUp('ctrl')

altTab()

write("5e met")

pt.press("enter")
pt.press("down")
pt.press("up")
pt.press("enter")
pt.press("down")
pt.press("up")
pt.press("enter")

deskTop()

write('ent ')

waitAndClick('laclasse-id')

waitAndClick('pronote')

newTab()

waitAndClick('biblio-manuel')

newTab()

waitAndClick('gmail')

pt.keyDown("ctrl")
pt.press("tab")
pt.press("tab")
pt.keyUp("ctrl")
