from cgi import print_arguments
from time import sleep
import pyautogui as pag

def clickDelete():
    left, top, width, height = pag.locateOnScreen('delete.png', region=(200,191,729-200,399-191))
    center = pag.center((left, top, width, height))
    pag.click(center)
    sleep(1.2)


while True:
    if pag.locateOnScreen('delete.png', region=(200,191,729-200,399-191)):
        clickDelete() 
    else:
        print("cannot find delete button")