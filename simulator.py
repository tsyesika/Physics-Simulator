import pygame, time, random
from pygame.locals import *

class _globals():
	pass

#SETUP
pygame.init()
screen = pygame.display.set_mode((672, 672))
pygame.display.set_caption("my window")

#GLOBALS
g = _globals()
clock = pygame.time.Clock()
gravity = 10
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
		pygame.draw.rect(screen, (0, 255, 0), (self.p[0], self.p[1], self.p[2], self.p[3]))



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

while True:
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

		# while(True):
		#update world
		#draw world
		mpos = pygame.mouse.get_pos()
		cond = pygame.mouse.get_pressed()[0]
	
		#checks to make sure objects don't collide
		#for i1 in range(len(object_list)):
		#	if i != i1:
		#		#Not current object (check hasn't collided)
		#		if pygame.Rect(o.p[0],o.p[1],o.p[2],o.p[3]).colliderect(pygame.Rect(object_list[i1].p[0],object_list[i1].p[1],object_list[i1].p[2],object_list[i1].p[3])):
		#			if (o.p[0]+o.p[2]) - (object_list[i1].p[0] + object_list[i1].p[3]) > 0:
						#hit the top
		#				o.yvel *= -1
		#				object_list[i1].yvel *= -1
		
		if not cond and Gravity:
			if o.p[1] > 572:
				o.p[1] = 572
				o.yvel *= -0.5
			elif o.p[1] > (572 - gravity) or o.p[1] < 0:
				o.yvel *= -0.5
			else:
				o.yvel += gravity
		elif not cond:
			#friction ?
			if Friction:
				#Yes, apply
				if o.xvel > 0:
					try:
						o.xvel -= friction / mass
					except ZeroDivisionError:
						o.xvel = 0
					if o.xvel < 0:
						o.xvel = 0
				elif o.xvel < 0:
					try:
						o.xvel += friction / mass
					except ZeroDivisionError:
						o.xvel = 0
					if o.xvel > 0:
						o.xvel = 0
			
			
			o.p[1] += o.yvel
			o.p[0] += o.xvel
		
			# Keep from sides
			if o.p[0] < 0:
			 	o.xvel*= -1
			elif o.p[0] > 572:
				o.xvel *= -1
		
		
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
			
						
				#elif o.p[1] > object_list[i1].p[1]+object_list[i1].p[3] and o.p[1] < object_list[i1].p[1]-1 :
					#Collided on the bottom
				#	print "bottom"
				#	object_list[i1].xvel += (object_list[i1].xvel + o.xvel) / 2
				#	o.xvel -= (object_list[i1].xvel + o.xvel) / 2
				#elif o.p[0] > object_list[i1].p[1]+150:
					#Collided on the left
				#	print "left"
				#	object_list[i1].yvel += (object_list[i1].yvel + o.yvel) / 2
				#	o.yvel -= (object_list[i1].xvel + o.yvel) / 2
				#elif o.p[0] <= object_list[i1].p[1]+150:
					#collided on the right
				#	print "right"
				#	object_list[i1].yvel -= (object_list[i1].xvel + o.yvel) / 2
				#	o.yvel += (object_list[i1].xvel + o.yvel) / 2
					
		#DRAW SHIZZLE
		o.show()


	pygame.display.flip()
	clock.tick(150)

pygame.quit()
