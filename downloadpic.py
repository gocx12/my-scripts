import pyautogui as pag
import time

time.sleep(3)
sizex, sizey=pag.size()

n_pic = 146
i = 0
while(i < n_pic):
    # 查看大图
    pag.moveTo(1861,1050)
    pag.click(button='left')
    time.sleep(2)


    # 保存图片

    pag.moveTo(sizex/2, sizey/2)
    pag.click(button='right')
    pag.moveRel(1279-1204, 461-398, duration=0.2)
    pag.click(button='left')

    time.sleep(0.5)
    pag.write("pic_"+str(i))
    time.sleep(0.5)


    pag.press('enter')
    # pag.moveTo(1592, 101)
    # pag.click(button='left')
    time.sleep(0.5)
    pag.moveTo(sizex/2, sizey/2)
    pag.click(button='left')


    # 下一张图
    pag.press('right')
    time.sleep(0.5)
    i += 1