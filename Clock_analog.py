import pygame as pd
import time
from datetime import datetime
import sympy as sp
import numpy as np
import math as mt
pd.init()
def scos(x): return sp.N(sp.cos(x))
def ssin(x): return sp.N(sp.sin(x))
def next_point(x,lines,center):
    pi = sp.pi
    angle =(2*pi)/lines
    T1 = np.array([[1, 0, -center[0]], [0, 1, -center[1]], [0, 0, 1]])
    T2 = np.array([[1, 0, center[0]], [0, 1,center[1]], [0, 0, 1]])
    M = np.array([[scos(angle), -ssin(angle), 0],
                 [ssin(angle), scos(angle), 0],
                 [0, 0, 1]])
    x = np.array([[x[0]], [x[1]], [1]])
    xt = T1.dot(x)
    xt2 = M.dot(xt)
    xt3 = T2.dot(xt2)
    return xt3[0:2]

def get_minutes(hours,minutes,point,center):
    for i in range(int(hours)%12):
        point = next_point(point,12,center)
        #print(point)
    for i in range(int(minutes)):
        point = next_point(point,12*60,center)
        #print(point)
    return point[0:2]
def get_seconds(seconds,point,center):
    for i in range(int(seconds)+1):
        point = next_point(point,60,center)
    return point[0:2]
size  = (1200,800)
screen = pd.display.set_mode(size)
pd.display.set_caption("Clock")
done = False
clock = pd.time.Clock()
background = (200,250,250)
black = (0,0,0)
white = (255,255,255)



while not done:
    for event in pd.event.get():
        if event.type == pd.QUIT:
            done = True
    screen.fill(black)

    screen.fill(black)
    point_A = [600,150]
    point_B = [600,100]
    point_C = [600,50]
    center = [600,400]
    for i in range(12,0,-1):
        pd.draw.line(screen,white,[int(point_A[0]),int(point_A[1])],[int(point_B[0]),int(point_B[1])],5)
        font = pd.font.SysFont('Calibri', 30, True, False)
        text = font.render('{}'.format(i), True, white)
        screen.blit(text, [int(point_C[0]),int(point_C[1])])
        npoint_A = next_point(point_A,-12, center)
        npoint_B = next_point(point_B,-12, center)
        npoint_C = next_point(point_C,-12, center)
        for y in range(2):
            point_A[y] = npoint_A[y][0]
            point_B[y] = npoint_B[y][0]
            point_C[y] = npoint_C[y][0]

    now = datetime.now()

    current_Hours = now.strftime("%H")
    current_Minutes = now.strftime("%M")
    current_Seconds = now.strftime("%S")
    #print((int(current_Hours)%12) ,int(current_Minutes),current_Minutes)
    point_Minutes = [600,250]
    point_Seconds = [600,220]
    point_Minutes = get_minutes(current_Hours,current_Minutes,point_Minutes,center)
    point_Seconds = get_seconds(current_Seconds , point_Seconds,center)
    pd.draw.line(screen, white, center, [int(point_Minutes[0]),int(point_Minutes[1])], 5)
    pd.draw.line(screen, white, center,[int(point_Seconds[0]),int(point_Seconds[1])] , 5)



    pd.display.flip()
    clock.tick(60)

pd.quit()



