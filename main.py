from pygame import *


window = display.set_mode((700, 500))
back = (255, 255, 255)
window.fill(back)
pic = image.load('2a91cec1d6.jpg')
picture = transform.scale(pic, (700,500))
run = True
while run:

    window.blit(picture,(0,0))
    time.delay(50)
    for e in event.get():
        if e.type == QUIT:
            run = False
    display.update()
