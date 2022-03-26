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

slide = MouseSlider(window, [100, 5], [1, 0], [50, 450], [255,255,255], [0, windowSize[0]])
ball = Ball(window, 12, [1, 1], [10, 10], [255,255,255], [0, windowSize[0]], [0, windowSize[1]], 'Circle.png')

sliders = Sliders(window)
sliders.add(slide)

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
        ball.ChangeDirection(False)
        score += 1
    except:
        pass

def CheckLose():
    if (ball.rect.bottom > windowSize[1]):
        Lost()

def Lost():
    DrawText(loseFont, 'You Lost', [200, 190])

    f = open('SimpleTenisScore.txt', 'a')
    f.close()

    f = open('SimpleTenisScore.txt', 'r')
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
        f = open('SimpleTenisScore.txt', 'w')
        f.write(str(score))
        f.close()
    ExitGame()

def Update(): 
    window.fill(windowColor)
    
    slide.update()
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

    Update()

ExitGame()
