import pygame as pd
import time
from datetime import datetime
def draw_number(timer,posx,posy):
    for number in timer:
        printed_number = numbers[number]
        for i in range(1,8):
            lines = [[10+posx, 0+posy], [90+posx, 0+posy], [100+posx, 10+posy], [100+posx, 90+posy], [100+posx, 110+posy], [100+posx, 190+posy], [90+posx, 200+posy], [10+posx, 200+posy],
                     [0+posx, 110+posy],[0+posx, 190+posy],  [0+posx, 10+posy],[0+posx, 90+posy], [10+posx, 100+posy], [90+posx, 100+posy]]
            if printed_number[i-1] == '1':
                pd.draw.line(screen,(255,255,255),lines[(i*2)-2],lines[(i*2)-1],9)
        posx += 120
pd.init()



size  = (1400,900)
screen = pd.display.set_mode(size)
pd.display.set_caption("Clock")
numbers = {'0' : '1111110',
           '1' : '0110000',
           '2' : '1101101',
           '3' : '1111001',
           '4' : '0110011',
           '5' : '1011011',
           '6' : '1011111',
           '7' : '1110000',
           '8' : '1111111',
           '9' : '1111011',
           '-' : '0000001'}


done = False
clock = pd.time.Clock()
background = (200,250,250)
black = (0,0,0)
fps = 60

while not done:
    for event in pd.event.get():
        if event.type == pd.QUIT:
            done = True
    screen.fill(black)

    now = datetime.now()
    current_time = now.strftime("%H-%M-%S")
    screen.fill(black)
    draw_number(current_time, 200, 350)
    pd.display.update()
    pd.event.pump()

    pd.display.flip()
    clock.tick(60)

pd.quit()



