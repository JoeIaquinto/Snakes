#Dan GORMAN
#3/12/13
#SPACE INVADING


import pygame, sys, time, random
from pygame.locals import *

# set up pygame
pygame.init()

# set up the window
WINDOWWIDTH = 600
WINDOWHEIGHT = 600
window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Animation')

# set up direction variables
location=4

MOVESPEED = 4

# set up the colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
Purple=(120,0,120)
WHITE=(255,255,255)
yellow=(255,255,0)
points=0
snakes=[]
initlength=5
brea=False
gameworkscorrectly='yes'
new=0
newcount=6
blah=newcount

# set up the rect data structure

def newfood(x,y):
    return {'rect':pygame.Rect(x*10,y*10,10,10),'x':x,'y':y}

def texts(score,color,size=30):
    font=pygame.font.Font(None,size)
    scoretext=font.render("Score:"+str(score), 1,color)
    window.blit(scoretext, (0, WINDOWHEIGHT-size+10))

def snakerect(x,y,dire):
    return {'rect':pygame.Rect(x,y,10,10),'dir':dire}


def smake(leng):
    snake=[]
    for i in range(leng):
       snake.append(snakerect(WINDOWWIDTH/2,WINDOWHEIGHT/2+(10*i),'UP'))
    return snake

snakes.append(smake(15))

food='no'

# run the game loop
while True:
    # check for the QUIT event
    for event in pygame.event.get():
        
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        #moves ship
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if snakes[0][0]['dir']!='RIGHT':
                    snakes[0][0]['dir']='LEFT'
            elif event.key == pygame.K_RIGHT:
                if snakes[0][0]['dir']!='LEFT':
                    snakes[0][0]['dir']='RIGHT'
            elif event.key == pygame.K_UP:
                if snakes[0][0]['dir']!='DOWN':
                    snakes[0][0]['dir']='UP'
            elif event.key == pygame.K_DOWN:
                if snakes[0][0]['dir']!='UP':
                    snakes[0][0]['dir']='DOWN'
            elif event.key== pygame.K_SPACE:
                snakes.append(smake(initlength))
                points+=1
                

    if food=='no' and random.randint(0,176)>175:
        foo=newfood(random.randint(0,(WINDOWWIDTH-10)/10),random.randint(0,(WINDOWHEIGHT-10)/10))
        food='yes'
        print 'blah'


    # draw the black background onto the surface
    window.fill(BLACK)
    b=0
    c=0
    col=(random.randint(55,255),random.randint(55,255),random.randint(55,255))

    if new>=blah:
        blah+=newcount

        snakes.append(smake(initlength))
    for snake in snakes:
        if col==WHITE:
            dirc=random.randint(0,13)
            if dirc<=3 or dirc>7:
                pass
            elif dirc==4 and snake[0]['dir']!='DOWN':
                snake[0]['dir']='UP'
            elif dirc==5 and snake[0]['dir']!='UP':
                snake[0]['dir']='DOWN'
            elif dirc==6 and snake[0]['dir']!='LEFT':
                snake[0]['dir']='RIGHT'
            else:
                snake[0]['dir']='LEFT'
            for i in range(len(snakes[0])-1):
                for s in snake:
                    if s['rect'].top==snakes[0][i]['rect'].top and s['rect'].left==snakes[0][i]['rect'].left:
                        snakes[0].remove(snakes[0][len(snakes[0])-1])
                        if len(snakes[0])<=3:
                                         
                            while True:
                                for event in pygame.event.get():
                                    
                                    if event.type == QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    if event.type==pygame.KEYDOWN:
                                        if event.key==pygame.K_r:
                                            if gameworkscorrectly=='yes':
                                                    snakes=[]
                                                    new=0
                                                    blah=10
                                                    points=0

                                            snakes.append(smake(15))
                                            brea=True
                                if brea:
                                    brea=False
                                    break
                        brea=True
                        break
                if brea:
                    brea=False
                    break

        else:
            if food=='yes':
                if snake[0]['rect'].left/10==foo['x'] and snake[0]['rect'].top/10==foo['y']:
                    for b in range(2):
                        i=len(snake)-1
                        if snake[i]['dir']=='UP':
                            x=snake[i]['rect'].left
                            y=snake[i]['rect'].top+10
                        elif snake[i]['dir']=='DOWN':
                            x=snake[i]['rect'].left
                            y=snake[i]['rect'].top-10
                        elif snake[i]['dir']=='LEFT':
                            y=snake[i]['rect'].top
                            x=snake[i]['rect'].left+10
                        else:
                            y=snake[i]['rect'].top
                            x=snake[i]['rect'].left-10
                        snake.append(snakerect(x,y,snake[i]['dir']))
                    points+=1
                    food='no'
                
            
        for s in snake:
            if s['dir']=='UP':
                s['rect'].top-=10
                if s['rect'].top==-10:
                    s['rect'].top=WINDOWHEIGHT-10
            elif s['dir']=='DOWN':
                s['rect'].top+=10
                if s['rect'].top==WINDOWHEIGHT:
                    s['rect'].top=0
            elif s['dir']=='RIGHT':
                s['rect'].left+=10
                if s['rect'].left==WINDOWWIDTH:
                    s['rect'].left=0
            else:
                s['rect'].left-=10
                if s['rect'].left==-10:
                    s['rect'].left=WINDOWWIDTH-10
            

            
            pygame.draw.rect(window,col,s['rect'],0)
        col=WHITE
            
    for snake in snakes:
        for i in reversed(range(len(snake))):
            if i!=0:
                snake[i]['dir']=snake[i-1]['dir']    # draw the window onto the screen
    points+=.04
    texts(int(points),WHITE)
    if food=='yes':
        pygame.draw.rect(window,Purple,foo['rect'])
    pygame.display.update()
    new+=.04
    time.sleep(0.036)
