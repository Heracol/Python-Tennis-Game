import pygame
pygame.init()
pygame.font.init()

pygame.version.ver = '1.0.0'
pygame.version.vernum = (1, 0, 0)

from Sliders import *
from Slider import *
from Ball import *

pygame.mouse.set_visible(False)

windowSize = [800, 500]
windowColor = [0,0,0]

window = pygame.display.set_mode(windowSize)
window.fill(windowColor)

sb1 = [False, False]
sb2 = [False, False]
slide1 = SimpleSlider(window, [5, 100], [0, 1], [50, 50], [255,255,255], [0, windowSize[1]])
slide2 = SimpleSlider(window, [5, 100], [0,  1], [windowSize[0]-50, 50], [255,255,255], [0, windowSize[1]])
ball = Ball(window, 12, [1, 1], [100, 100], [255,255,255], [0, windowSize[0]], [0, windowSize[1]], None)

sliders = Sliders(window)
sliders.add(slide1)
sliders.add(slide2)

scoreFont = pygame.font.SysFont('Comic Sans MS', 20)
loseFont = pygame.font.SysFont('Arial', 100)

score = 0

def DrawText(font, text, pos):
    newText = font.render(str(text), True, [255,255,255], [0,0,0])
    window.blit(newText, pos)

def CheckCollision():
    global score
    
    ball_hit_list = pygame.sprite.spritecollide(ball, sliders, False)

    try:
        sprite = ball_hit_list[0]
        ball.ChangeDirection(True)
        score += 1
    except:
        pass

def CheckLose():
    if (ball.rect.left < 0):
        Lost('Left Lost')
    if (ball.rect.right > windowSize[0]):
        Lost('Right Lost')

def Lost(text):
    DrawText(loseFont, text, [200, 190])

    f = open('DoubleTenisScore.txt', 'a')
    f.close()

    f = open('DoubleTenisScore.txt', 'r')
    hs = f.read()
    if (hs == ''):
        hs = 0

    hfont = pygame.font.SysFont('Arial', 35)
    DrawText(hfont, 'High Score:', [250, 310])
    DrawText(hfont, hs, [450, 310])

    pygame.display.update()
    pygame.time.delay(3000)
    f.close()
    if (int(hs) < score):
        f = open('DoubleTenisScore.txt', 'w')
        f.write(str(score))
        f.close()
    
    pygame.display.update()
    pygame.time.delay(3000)
    ExitGame()

def Update(): 
    window.fill(windowColor)
    
    if (sb1[0]):
        slide1.moveLeft()
    if (sb1[1]):
        slide1.moveRight()
    if (sb2[0]):
        slide2.moveLeft()
    if (sb2[1]):
        slide2.moveRight()

    sliders.update()
    ball.update()

    DrawText(scoreFont, score, [730, 5])

    CheckCollision()
    CheckLose()
    
    pygame.display.update()
    pygame.time.delay(5)

def ExitGame():
    pygame.display.quit()
    pygame.quit()
    exit()

DrawText(scoreFont, score, [730, 5])
pygame.display.update()

running = True
while running:
    
    events = pygame.event.get()
    for event in events:
        if (event.type == pygame.QUIT):
            running = False

        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_UP):
                sb2[0] = True
            if (event.key == pygame.K_DOWN):
                sb2[1] = True
            if (event.key == pygame.K_w):
                sb1[0] = True
            if (event.key == pygame.K_s):
                sb1[1] = True

        if (event.type == pygame.KEYUP):
            if (event.key == pygame.K_UP):
                sb2[0] = False
            if (event.key == pygame.K_DOWN):
                sb2[1] = False
            if (event.key == pygame.K_w):
                sb1[0] = False
            if (event.key == pygame.K_s):
                sb1[1] = False

    Update()

ExitGame()
