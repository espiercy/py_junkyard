#First Pygame sample - I have skipped coding practice for the earlier chapters of this book because I am very familiar with the constructions included and wanted to make headway
#6.11.2017 epiercy

"""
Simple graphics demo
Sample Python/Pygame Programs
adapted from http://programarcadegames.com
"""

#import pygame
import pygame

#import math for shape drawing rather than define pi
import math

#initialize game engine
pygame.init()

#define colors

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)

#build window size
size = (700,500)

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Professor Piercy\'s Cool Game')

#Loop until user clicks close button
done = False

#Used to manage how fast the screen updates
clock = pygame.time.Clock()

#Main Program Loop

while not done:
    #Main event loop
    for event in pygame.event.get(): #user did something
        if event.type == pygame.QUIT: #if user clicked close
            done = True #time to exit loop
    #game logic, drawing code should go here.
    screen.fill(WHITE) #fill screen with white - if you wait to fill screen with white, everything you draw will get painted over
    pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5) #start coords, end coords, thickness...

    for y_offset in range(0,100,10):
        pygame.draw.line(screen,RED,[0,10+y_offset],[100,110+y_offset],5) #lines are drawn until y_offset reaches 100

    #this one is really nifty. It uses sin/cos for waves
    for i in range(200):
        radians_x = i/20
        radians_y = i/6
        x = int(75 * math.sin(radians_x)) + 200
        y = int(75 * math.sin(radians_y)) + 200
        pygame.draw.line(screen,BLACK,[x,y],[x+5,y],5)

    for x_offset in range(30,300,30): #draws black x's
        pygame.draw.line(screen,BLACK,[x_offset,100],[x_offset-10,90],2)

    for x_offset in range(30,300,30):
        pygame.draw.line(screen,BLACK,[x_offset,90],[x_offset-10,100],2)

    #rectangle
    pygame.draw.rect(screen,BLACK,[20,20,250,100],2)

    #ellipse in rectangle
    pygame.draw.ellipse(screen,BLACK,[20,20,250,100],2)

    #arcs
    pygame.draw.arc(screen,GREEN,[100,100,250,200],math.pi/2,math.pi,2)
    pygame.draw.arc(screen, BLACK, [100, 100, 250, 200], 0, math.pi/2, 2)
    pygame.draw.arc(screen, RED, [100, 100, 250, 200], 3*math.pi/2, 2*math.pi, 2)
    pygame.draw.arc(screen, BLUE, [100, 100, 250, 200], math.pi, 3*math.pi/2, 2)

    #triangle/polygon
    pygame.draw.polygon(screen,BLACK,[[100,100],[0,200],[200,200]],5) #<--3 raw coords. No offset

    #text
    #select font
    font = pygame.font.SysFont('Calibri',25,True,False)
    #render text (not pushed to screen obj yet)
    text = font.render("This demonstrates basic drawing in pygame",True,BLACK)
    #this pushes to screen obj
    screen.blit(text,[200,300])

    pygame.display.flip() #update screen with what we've drawn
    clock.tick(60) # 60 fps

pygame.quit()