import serial
import time
import pygame, sys
from pygame.locals import *
pygame.init()
FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

ser=serial.Serial(port='COM4',timeout=3)
s = 0
pending = 0 
score = 0
while s != "\n":
	s=ser.read(1)
	

def Stationary():
	DISPLAYSURF = pygame.display.set_mode((1360, 768), pygame.FULLSCREEN)
	pygame.display.set_caption('Virtual Dunk Tank')
	WHITE = (255, 255, 255)
	DISPLAYSURF.fill(WHITE)
	personImg = pygame.image.load('stick_figure_sitting_on_ledge.png')
	tankImg = pygame.image.load('tankdepth-web-flash.png')
	persX = 500
	persY = 10
	tankX = 500
	tankY = 450
	DISPLAYSURF.blit(personImg, (persX, persY))
	DISPLAYSURF.blit(tankImg, (tankX, tankY))
	pygame.display.update()
	fpsClock.tick(FPS)
	#for event in pygame.event.get():	
	#	if event.type == QUIT:
	#		pygame.quit()
	#		sys.exit()	
	return 0


def Dunk():
	DISPLAYSURF = pygame.display.set_mode((1360, 768), pygame.FULLSCREEN)
	pygame.display.set_caption('Animation')
	WHITE = (255, 255, 255)
	BLUE = (  0,  0, 128)
	personImg = pygame.image.load('stick_figure_sitting_on_ledge.png')
	persX = 500
	persY = 10


	for i in range(1, 100): # man moves down

	   DISPLAYSURF.fill(BLUE)
	   persY+=10

	   DISPLAYSURF.blit(personImg, (persX, persY)) # put person on screen in middle
	  
	   #for event in pygame.event.get():	
		#   if event.type == QUIT:
		#	   pygame.quit()
		#	   sys.exit()
		
	   pygame.display.update()
	   fpsClock.tick(FPS)
	for i in range(1, 100): #man moves back up

	   DISPLAYSURF.fill(BLUE)
	   persY-=10
	  
	   DISPLAYSURF.blit(personImg, (persX, persY))
	   #for event in pygame.event.get():
		#if event.type == QUIT:
		#	pygame.quit()
		#	sys.exit()
	   pygame.display.update()
	   fpsClock.tick(FPS)
	   
	return 0


	
while True:

	Stationary()

	i=1
	while i<=7:

		s=ser.read(1)
		ser.read(15)
		if s=='1' and pending<2:
			pending = pending +1
		elif s=='1' and pending == 2:
			score = score + 1
			pending = 0
			Dunk()
		elif s=='2':
			score = score +1
			pending = 0
			Dunk()
			
		if i ==6:
			break
		i = i+1
	print score
