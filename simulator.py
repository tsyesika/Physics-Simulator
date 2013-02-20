import pygame, time, random, sys
from pygame.locals import *

# World size
width = 500
height = 500

#SETUP
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Physics Simulator")

#GLOBALS
clock = pygame.time.Clock()
gravity = 1
mass = 50
friction = 10
p = [50, 50, 100, 100]
############################## - MAINLOOP - ##############################


# Objects
class Item():
    mass = 1
    xvel = 0
    yvel = 0
    weight = gravity * mass
    p = [50, 50, 100, 100]

    def validate(self):
        """ Validates that it's not colided with the wall """
        # x validate
        if self.p[0] <= 0:
            self.p[0] = 0
            self.xvel *= -0.5
        elif self.p[0] > self.calculate_side():
            self.p[0] = self.calculate_side()
            self.xvel *= -0.5
        
        # y validate
        if self.p[1] <= 0:
            # top
            self.p[1] = 0
            self.yvel *= -0.5
        elif self.p[1] > self.calculate_base():
            # bottom
            self.p[1] = self.calculate_base()
            self.yvel *= -0.5
    
    def debug(self, message):
        if Debug:
            print "[debug] %s" % message

    def calculate_base(self):
        """ Calculates the base of the object """
        bottom_item = height - self.p[3]
        base = bottom_item
        return base
    
    def calculate_side(self):
        """ Calculates the right side of the object """
        return width - self.p[2]

    def clicked(self, pos):
        """ Returns if the block has been clicked on """
        if pos[0] < self.p[0]:
            return False

        # pointer is on or below block
        if pos[0] > (self.p[1] + self.p[2]):
            return False
        
        # now need to check the x axis
        if pos[1] < self.p[1]:
            return False
        
        if pos[1] > (self.p[1] + self.p[3]):
            return False
       
        return True # yay!

class Block(Item):
    def __init__(self):
        self.mass = 5
        self.ydiff = 0
        self.xdiff = 0
    
    def show(self):
        """Draws block"""
        self.apply_volocity()
        self.validate()
        pygame.draw.rect(screen, (0, 255, 0), tuple(self.p))
   

    def apply_volocity(self):
        if Gravity:
            # okay gravity is on, lets apply it!
            if not (self.ydiff or self.xdiff):
                self.debug("setting the ydiff = %s" % self.weight)
                self.ydiff = self.weight
            self.xvel += self.xdiff
            self.yvel += self.ydiff
 
        
        # apply volocity
        self.p[0] += self.xvel
        self.p[1] += self.yvel
##      
# Settings
##

Friction = True
Gravity = True
Debug = False

_END = False

##
# Object instansiation
##
object_list = [Block()]
object_list[0].p = [200, 200, 100, 100]
while not _END:
    for event in pygame.event.get():
        if event.type == QUIT:
            _END = True
            break
        if event.type == pygame.KEYDOWN:
            if event.key == K_f:
                if Friction:
                    Friction = False
                else:
                    Friction = True
            elif event.key == K_g:
                if Gravity:
                    Gravity = False
                else:
                    Gravity = True
            elif event.key == K_q:
                _END = True
                break
            elif event.key == K_d:
                if Debug:
                    print "Turning debug mode off"
                    Debug = False
                else:
                    print "Turning debug mode on"
                    Debug = True
    if _END:
        break


    ##
    # Code
    ##
    screen.fill((0,0,0))
    
    r_mouse_button = pygame.mouse.get_pressed()[0]   
    if r_mouse_button:
        mouse_position = pygame.mouse.get_pos()

    #Make sure gravity is good stuff :P
    for item in object_list:
        if r_mouse_button:
            # okay the right mouse button has been pressed
            item.clicked(mouse_position)
            if starting_
            
        item.show()


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
