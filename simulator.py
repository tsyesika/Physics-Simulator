import pygame, time, random, sys
from pygame.locals import *


#SETUP
pygame.init()
screen = pygame.display.set_mode((672, 672))
pygame.display.set_caption("Physics Simulator")

#GLOBALS
clock = pygame.time.Clock()
gravity = 1
mass = 50
friction = 10
p = [50, 50, 100, 100]
############################## - MAINLOOP - ##############################


# Objects
class Block():
    def __init__(self):
        self.p = [50, 50, 100, 100]
        self.mass = 50000
        self.yvel = 0
        self.xvel = 0
        self.ydiff = 0
        self.xdiff = 0
    
    def show(self):
        """Draws block"""
        self.apply_volocity()
        pygame.draw.rect(screen, (0, 255, 0), tuple(self.p))
    
    def cal_vel(self):
        """ Calculates next position """
        if self.p[1] > 572:
            self.p[1] = 572
            self.p[1] *= -0.5
        elif self.p[1] < 0:
            self.p[1] = 0
        else:
            self.yvel += gravity

    def apply_volocity(self):
            l_mouse_press, m_mouse_press, r_mouse_press = pygame.mouse.get_pressed()
            l_mouse_pos, r_mouse_pos = pygame.mouse.get_pos()
            if not (o.ydiff or o.xdiff) and l_mouse_press:
                o.xdiff = l_mouse_pos
                o.ydiff = r_mouse_pos
            elif not l_mouse_press and (o.xdiff or o.ydiff):
                try:
                    o.xvel = (l_mouse_press - o.xdiff) / o.mass
                except ZeroDivisionError:
                    o.xvel = 0
                try:
                    o.yvel = ((l_mouse_press - o.ydiff) / o.mass) + o.yvel
                except ZeroDivisionError:
                    o.yvel = 0
                    o.xdiff = 0
                    o.ydiff = 0

            # should we be applying gravity?
            if not l_mouse_press:
                # oh why yes we should :)
                self.cal_vel()
                o.p[0] += o.xvel
                o.p[1] += o.yvel


##          
# Settings
##

Friction = True
Gravity = True

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
    if _END:
        break


    ##
    # Code
    ##
    screen.fill((0,0,0))
    
    #Make sure gravity is good stuff :P
    for i in range(len(object_list)):
        o = object_list[i]
        if not (o.ydiff or o.xdiff) and pygame.mouse.get_pressed()[0]:
            o.xdiff = pygame.mouse.get_pos()[0]
            o.ydiff = pygame.mouse.get_pos()[1]
        elif not pygame.mouse.get_pressed()[0] and (o.xdiff or o.ydiff):
            try:
                o.xvel = (pygame.mouse.get_pos()[0] - o.xdiff) / o.mass
            except ZeroDivisionError:
                o.xvel = 0
            try:
                o.yvel = ((pygame.mouse.get_pos()[0] - o.ydiff) / o.mass) + o.yvel
            except ZeroDivisionError:
                o.yvel = 0
            o.xdiff = 0
            o.ydiff = 0

        # Calculate weight

        mpos = pygame.mouse.get_pos()
        cond = pygame.mouse.get_pressed()[0]
        
        
        #Allows you to pick blocks up
        if cond and (mpos[0] > o.p[0]-1 and mpos[0] <= o.p[0] + 150) and (mpos[1] > o.p[1]-1 and mpos[1] <= o.p[1]+150): 
            #clicked mouse over box
            o.p[0] = pygame.mouse.get_pos()[0] - (o.p[2] / 2)
            if o.p[0] != pygame.mouse.get_pos()[1]:
                #applied force on x
                try:
                    o.xvel = (o.p[0] / pygame.mouse.get_pos()[1]) / o.mass
                except ZeroDivisionError:
                    o.xvel = 0
            o.p[1] = pygame.mouse.get_pos()[1] - (o.p[3] / 2)
            
                
        #DRAW SHIZZLE
        o.show()


    pygame.display.flip()
    clock.tick(150)

pygame.quit()
