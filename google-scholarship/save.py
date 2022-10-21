from time import sleep
import pyautogui as pag

def clickSave():
    left, top, width, height =  pag.locateOnScreen('unsave.png', region=(200,191,350-200,1060-191)) #please set the region where the save button may appear according to your own monitor
    center = pag.center((left, top, width, height))
    pag.click(center)
    print(center)
    sleep(1)
    pag.click(770,615)


count = 0
while True:
    if pag.locateOnScreen('unsave.png', region=(200,191,350-200,1060-191)): #please set the region where the save button may appear according to your own monitor
        clickSave() 
        count = 0
    else:
        count += 1
        pag.scroll(-500)
        print('no save button, scroll down')
        if count > 2:
            print('next page')
            if pag.locateOnScreen('next.png', region=(200,910,870-200,1060-910)): #please set the region where the next page button may appear according to your own monitor
                left, top, width, height =  pag.locateOnScreen('next.png', region=(200,910,870-200,1060-910))
                center = pag.center((left, top, width, height))
                pag.click(center)
                sleep(3)
            else:
                print('end!')
                break