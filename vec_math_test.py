from math import cos, sin, pi
from random import randint
from vec_math import *
import pygame

screen = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()

angle = 0

x, y = 300, 300

while True:
	a = vec2(1, 0)
	
	#clock.tick(0)
#	screen.fill((50, 50, 50))
	
	for e in pygame.event.get():
		if e == pygame.QUIT:
			exit()
	
	a *= mat2(
		vec2(sin(angle)*cos(angle), sin(angle)),
		vec2(cos(angle)+angle/randint(20, 1000), -sin(angle))
	)
	
	pygame.draw.line(screen, (0, 255, 0), (x, y), (x+a.y*100, y+a.x*100), 1)
	
	pygame.display.flip()
	
	angle += 0.1