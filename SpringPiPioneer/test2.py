import pygame
import sys
from time import sleep
speed = 10
direction = "Left"
def load_image(name):
    image = pygame.image.load(name)
    return image

class TestSprite(pygame.sprite.Sprite):
    def __init__(self):
        super(TestSprite, self).__init__()
        self.images = []
        self.images.append(load_image('goat1.gif').convert_alpha())
        self.images.append(load_image('goat2.gif').convert_alpha())
        self.images.append(load_image('goat3.gif').convert_alpha())
        self.images.append(load_image('goat4.gif').convert_alpha())
        self.images.append(load_image('goat5.gif').convert_alpha())
        self.images.append(load_image('goat1flipped.png').convert_alpha())
        self.images.append(load_image('goat2flipped.png').convert_alpha())
        self.images.append(load_image('goat3flipped.png').convert_alpha())
        self.images.append(load_image('goat4flipped.png').convert_alpha())
        self.images.append(load_image('goat5flipped.png').convert_alpha())
        self.x=5
        self.y=5
        
        
        self.index = 5
        self.image = self.images[self.index]
        self.rect = pygame.Rect(self.x, self.y, 116, 128)
        

    def update(self):
        '''This method iterates through the elements inside self.images and 
        displays the next one each tick. For a slower animation, you may want to 
        consider using a timer of some sort so it updates slower.'''
        print(self.rect.y)
        if direction == "Right":
            if self.index >= 4:
                self.index = 0
            else:
                self.index+=1
        elif direction == "Left":
            if self.index >= 9:
                self.index = 5
            else:
                self.index +=1
        global direction
        global speed
        global level

        if self.rect.x == 605 and direction == "Left":
            speed = -10
            direction = "Right"
            self.index = 0
        elif self.rect.x == -5 and direction == "Right":          
            speed=10
            direction = "Left"
            self.index = 5

        if self.rect.x >= 550 and level == 1:
            screen.blit(background, (self.rect.x, self.rect.y))
            self.rect.y = self.rect.y + 230
            level = 2
        
        self.rect.x += speed
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        screen.blit(background, (self.rect.x, self.rect.y))
        screen.blit(ground, (0, 120))
        screen.blit(ground, (300, 350))
        # Each frame of animation is displayed for 0.07 seconds
        sleep(0.07)
        
        
def main():
    pygame.init()
    global leftkeypressed
    global rightkeypressed
    global screen
    global background
    global ground
    global level
    global direction
    global speed
    level = 1
    screen = pygame.display.set_mode((800, 600))
    background = pygame.image.load('background.bmp').convert()
    screen.blit(background, (0,0))
    ground = pygame.image.load('ground.png').convert()
    leftkeypressed = False
    rightkeypressed = False
    my_sprite = TestSprite()
    my_group = pygame.sprite.Group(my_sprite)
    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "Right"
                    speed = -10
                    leftkeypressed = True
                    leftkeypressed = False
                elif event.key == pygame.K_RIGHT:
                    direction = "Left"
                    speed = 10
                    rightkeypressed = True
                    rightkeypressed = False

        # Calling the 'my_group.update' function calls the 'update' function of all 
        # its member sprites. Calling the 'my_group.draw' function uses the 'image'
        # and 'rect' attributes of its member sprites to draw the sprite.
        my_group.update()
        my_group.draw(screen)
        pygame.display.flip()

if __name__ == '__main__':
    main()
