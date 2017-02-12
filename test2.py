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
        self.images.append(load_image('goatblack1.gif'))
        self.images.append(load_image('goatblack2.gif'))
        self.images.append(load_image('goatblack3.gif'))
        self.images.append(load_image('goatblack4.gif'))
        self.images.append(load_image('goatblack5.gif'))
        self.images.append(load_image('goatblack1flipped.gif'))
        self.images.append(load_image('goatblack2flipped.gif'))
        self.images.append(load_image('goatblack3flipped.gif'))
        self.images.append(load_image('goatblack4flipped.gif'))
        self.images.append(load_image('goatblack5flipped.gif'))
        self.x=5
        self.y=5
        
        self.index = 5
        self.image = self.images[self.index]
        self.rect = pygame.Rect(self.x, self.y, 116, 128)
        

    def update(self):
        '''This method iterates through the elements inside self.images and 
        displays the next one each tick. For a slower animation, you may want to 
        consider using a timer of some sort so it updates slower.'''
        global leftkeypressed
        global rightkeypressed
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
        global speed
        global direction

        if self.rect.x == 605 and direction == "Left":
            speed = -10
            direction = "Right"
            self.index = 0
        elif self.rect.x == -5 and direction == "Right":          
            speed=10
            direction = "Left"
            self.index = 5
        self.rect.x += speed
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        # Each frame of animation is displayed for 0.07 seconds
        sleep(0.07)
        
        
def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    leftkeypressed = False
    rightkeypressed = False
    global speed
    global leftkeypressed
    global rightkeypressed
    global direction
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
