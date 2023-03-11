import pygame
from pygame import *
import sys
import math

class Ball:
    def __init__(self, x, y, colour):
        self.mass = Vector2(x, y)
        self.length = ((origin.x - x) ** 2 + (origin.y - y) ** 2) ** (1/2)
        self.angle = math.atan((x - origin.x) / (y - origin.y))
        self.vel = 0
        self.colour = colour
    
    def move(self):
        self.vel -= GRAVITY * math.sin(self.angle) / self.length
        self.angle += self.vel

        self.vel = self.vel * RETURN_PERCENTAGE

        self.mass.x = self.length * math.sin(self.angle) + origin.x
        self.mass.y = self.length * math.cos(self.angle) + origin.y
        
    def draw(self):
        pygame.draw.lines(screen, self.colour, False, [(origin.x, origin.y), (self.mass.x, self.mass.y)], 1)
        pygame.draw.circle(screen, self.colour, (self.mass.x, self.mass.y), RADIUS, RADIUS)

# class Ball2:
#     def __init__(self, ball, x, y):
#         self.mass = Vect
#         self.length = ((self.ball.mass.x - x) ** 2 + (self.ball.mass.y - y) ** 2) ** (1/2)
#         self.angle = math.atan((x - self.ball.mass.x) / (y - self.ball.mass.y))
#         self.vel = 0or2(x, y)
#         self.ball = ball

    # def move(self):
    #     self.vel -= GRAVITY * math.sin(self.angle) / self.length
    #     self.angle += self.vel

    #     self.vel = self.vel * RETURN_PERCENTAGE

    #     self.mass.x = self.length * math.sin(self.angle) + origin.x
    #     self.mass.y = self.length * math.cos(self.angle) + origin.y

    # def draw(self):
    #     pygame.draw.lines(screen, (255, 255, 255), False, [(self.ball.mass.x, self.ball.mass.y), (self.mass.x, self.mass.y)], 1)
    #     pygame.draw.circle(screen, (255, 255, 255), (self.mass.x, self.mass.y), RADIUS, RADIUS)

GRAVITY = 0.001
RETURN_PERCENTAGE = 0.9999
RADIUS = 15
SCREEN_SIZE = 1000

pygame.init()
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption('Pendulum')
clock = pygame.time.Clock()

origin = Vector2(SCREEN_SIZE // 2,0)
balls = []
i = 0
colours = [(152, 239, 245), (109, 227, 246), (46, 215, 250), (0, 201, 255), (0, 187, 255), (0, 171, 255), (0, 155, 255), (0, 137, 255), (0, 117, 255),(17, 93, 247)] + [(0, 117, 255), (0, 137, 255), (0, 155, 255), (0, 171, 255), (0, 187, 255), (0, 201, 255), (46, 215, 250), (109, 227, 246)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        if event.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()
            balls.append(Ball(x, y, colours[i % len(colours)]))
            i += 1

    screen.fill("black")

    for ball in balls:
        ball.move()
        ball.draw()

    pygame.display.update()