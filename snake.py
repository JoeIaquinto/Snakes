#Dan GORMAN
#3/12/13
#SPACE INVADING


import pygame, sys, time, random
from pygame.locals import *

# set up pygame
pygame.init()

# set up the window
scale=1
WINDOWWIDTH = WINDOWHEIGHT = 400*scale
window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Snake')

# set up direction variables
location=4*scale

MOVESPEED = 4*scale

# set up the colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
Purple=(120,0,120)
WHITE=(255,255,255)
yellow=(255,255,0)
points=0
snake=[]
initlength=5
brea=False
levelcolor=WHITE
gameworkscorrectly='no'



def newfood(x,y):
    z=scale*10
    return {'rect':pygame.Rect(x*z,y*z,z,z),'x':x,'y':y}

# set up the rect data structure

def texts(score,color,size=(30*scale)):
    font=pygame.font.Font(None,size)
    scoretext=font.render("Score:"+str(score), 1,color)
    window.blit(scoretext, (0, WINDOWHEIGHT-size+10))

def snakerect(x,y,dire,color):
    return {'rect':pygame.Rect(x,y,10*scale,10*scale),'dir':dire, 'col':color}


for i in range(initlength):
    snake.append(snakerect(WINDOWWIDTH/2,WINDOWHEIGHT/2+(10*i*scale),'UP',WHITE))
q=10*scale
food=newfood(random.randint(0,(WINDOWWIDTH-q)/q),random.randint(0,(WINDOWHEIGHT-q)/q))

# run the game loop
while True:
    # check for the QUIT event
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        #moves ship
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                if snake[0]['dir']!='RIGHT':
                    snake[0]['dir']='LEFT'
            elif event.key == pygame.K_d:
                if snake[0]['dir']!='LEFT':
                    snake[0]['dir']='RIGHT'
            elif event.key == pygame.K_w:
                if snake[0]['dir']!='DOWN':
                    snake[0]['dir']='UP'
            elif event.key == pygame.K_s:
                if snake[0]['dir']!='UP':
                    snake[0]['dir']='DOWN'


    # draw the black background onto the surface
    window.fill(BLACK)
    b=0
    f=10*scale
    for s in snake:
        if s['dir']=='UP':
            s['rect'].top-=f
            if s['rect'].top==-f:
                s['rect'].top=WINDOWHEIGHT-f
        elif s['dir']=='DOWN':
            s['rect'].top+=f
            if s['rect'].top==WINDOWHEIGHT:
                s['rect'].top=0
        elif s['dir']=='RIGHT':
            s['rect'].left+=f
            if s['rect'].left==WINDOWWIDTH:
                s['rect'].left=0
        else:
            s['rect'].left-=f
            if s['rect'].left==-f:
                s['rect'].left=WINDOWWIDTH-f
        if b>=1:
            if s['rect'].top==snake[0]['rect'].top and s['rect'].left==snake[0]['rect'].left:
                while True:
                    for event in pygame.event.get():

                        if event.type == QUIT:
                            pygame.quit()
                            sys.exit()
                        if event.type==pygame.KEYDOWN:
                            if event.key==pygame.K_r:
                                if gameworkscorrectly=='yes':
                                        snake=[]
                                        points=0
                                else:
                                    levelcolor=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
                                for i in range(initlength):
                                    snake.append(snakerect(WINDOWWIDTH/2,WINDOWHEIGHT/2+(f*i),'UP',WHITE))
                                food=newfood(random.randint(0,(WINDOWWIDTH-f)/f),random.randint(0,(WINDOWHEIGHT-f)/f))
                                brea=True
                    if brea:
                        brea=False
                        break
        b+=1
        pygame.draw.rect(window,s['col'],s['rect'],0)

    if snake[0]['rect'].left/f==food['x'] and snake[0]['rect'].top/f==food['y']:
        i=len(snake)-1
        if snake[i]['dir']=='UP':
            x=snake[i]['rect'].left
            y=snake[i]['rect'].top+f
        elif snake[i]['dir']=='DOWN':
            x=snake[i]['rect'].left
            y=snake[i]['rect'].top-f
        elif snake[i]['dir']=='LEFT':
            y=snake[i]['rect'].top
            x=snake[i]['rect'].left+f
        else:
            y=snake[i]['rect'].top
            x=snake[i]['rect'].left-f
        snake.append(snakerect(x,y,snake[i]['dir'],levelcolor))
        food=newfood(random.randint(0,(WINDOWWIDTH-f)/f),random.randint(0,(WINDOWHEIGHT-f)/f))
        points+=10

    for i in reversed(range(len(snake))):
        if i!=0:
            snake[i]['dir']=snake[i-1]['dir']    # draw the window onto the screen
    pygame.draw.rect(window,(random.randint(0,255),random.randint(0,255),random.randint(0,255)),food['rect'])
    texts(points,WHITE)
    pygame.display.update()
    time.sleep(0.036)
