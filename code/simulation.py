import pygame
from bots import *
pygame.init()

window = pygame.display.set_mode((500,500))
pygame.display.set_caption("A literal moving block")
vel = 5
run = True
movenum = 0
moves = 400



while run:
    pygame.time.delay(1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill((0,0,0))

    pygame.draw.circle(window, (0,255,0), (250,20), 10, 20)
    if(dots[i].x<=255 and dots[i].x>=245 and dots[i].y>=15 and dots[i].y<=25 and dots[i].won==False):
        dots[i].botWin(movenum)



        if(dots[i].movement[movenum] == 0): # W
            dots[i].y += vel
        if(dots[i].movement[movenum] == 1): # S
            dots[i].y -= vel
        if(dots[i].movement[movenum] == 2): # A
            dots[i].x -= vel
        if(dots[i].movement[movenum] == 3): # D
            dots[i].x += vel
    
    pygame.draw.rect(window, (255,0,0), (dots[i].x, dots[i].y, dots[i].width, dots[i].height))
    movenum+=1
    
    if(movenum>=moves):
        done = True
        

    pygame.display.update() 
    



pygame.quit()