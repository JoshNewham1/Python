import pygame
from time import sleep
pygame.init()
width=350;
height=400
 
screen = pygame.display.set_mode( ( width, height) )
goat1 = pygame.image.load("goat1.gif").convert()
goat2 = pygame.image.load("goat2.gif").convert()
goat3 = pygame.image.load("goat3.gif").convert()
goat4 = pygame.image.load("goat4.gif").convert()
goat5 = pygame.image.load("goat5.gif").convert()
fpsClock = pygame.time.Clock()
imageX= 200; # x coordinate of image
imageY= 30; # y coordinate of image
running = True
black = ( 0 , 0 , 0)
while (running): # main game loop
    #imageX -= 20 ;
##    screen.fill(black) # clear screen 
    screen.blit(goat1 , (imageX, imageY) )
    pygame.display.update()
    fpsClock.tick(30)
    sleep(2.07)
    screen.fill(black)
    screen.blit(goat2 , (imageX, imageY) )
##    sleep(0.07)
##    screen.blit(goat3 , (imageX, imageY) )
##    sleep(0.07)
##    screen.blit(goat4 , (imageX, imageY) )
##    sleep(0.07)
##    screen.blit(goat5 , (imageX, imageY) )
##    sleep(0.07)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Set the x, y postions of the mouse click
            x, y = event.pos
    pygame.display.update()
    fpsClock.tick(30)
#loop over, quit pygame
pygame.quit()
