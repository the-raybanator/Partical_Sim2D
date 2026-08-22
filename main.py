import pygame
from sys import exit
import time

length = 400
width = 400
pygame.init()   # initialize pygame
screen = pygame.display.set_mode((length,width)) # set screen size
pygame.display.set_caption("Particle Sim")
clock = pygame.time.Clock()
font = pygame.font.SysFont("jetbrainsmonothin", 20, bold=True)
dt = 1/60       # Period, i.e the time each frame takes

heading = font.render('Particle Simulator', True, (255, 255, 255))
heading_rect = heading.get_rect(midtop=(length/2,0))

class Particle():
    def __init__(self, x, y, radius, mass, vx, vy, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.diameter = 2 * radius
        self.mass = mass # used for particle collision
        self.vx = vx
        self.vy = vy
        self.surface = pygame.Surface((self.diameter, self.diameter), pygame.SRCALPHA)
        pygame.draw.circle(self.surface, color, (radius,radius), radius)    # radius is 10

p1 = Particle(200, 200, 10, -10, -150, 90, "white")  # posx, posy, vx, vy, color
p2 = Particle(600, 250, 10, 10, 120, -70, "green")   # velocities are in pixels/sec
# p3 = Particle(100, 50, -4, 3, "red")
# p4 = Particle(300, 50, -4, 3, "blue")

particles = [p1, p2]

time.sleep(1)   # short delay before sim starts

while True:
    for i in particles:
        i.x += i.vx * dt    # multiplying speed by rate to calibrate
        i.y += i.vy * dt

        # wall collisions
        if i.x < 0 or (i.x + i.diameter) > length:
            i.vx = -i.vx
            if i.x < 0:     # manually setting the ball in the frame so it doesn't stick at the edge
                i.x = 0
            elif (i.x + i.diameter) > length:
                i.x = length - i.diameter

        if i.y < 0 or (i.y + i.diameter) > width:
            i.vy = -i.vy
            if i.y < 0:     # manually setting the ball in the frame so it doesn't stick at the edge
                i.y = 0
            elif (i.y + i.diameter) > width:
                i.y = width - i.diameter
    
    vector1 = pygame.Vector2(p1.x, p1.y)
    vector2 = pygame.Vector2(p2.x, p2.y)

    # particle collisions
    if vector1.distance_to(vector2) < (p1.radius + p2.radius):
        p1.vx, p2.vx = p2.vx, p1.vx
        p1.vy, p2.vy = p2.vy, p1.vy

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((0, 0, 0))

    screen.blit(heading, heading_rect)
    for i in particles:
        screen.blit(i.surface, (i.x,i.y))

    pygame.display.update()
    clock.tick(60)
