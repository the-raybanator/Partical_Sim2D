import pygame   # this is the "pygame-ce" version
import pygame_gui
from sys import exit
import time

pygame.init()   # initialize pygame

SCREEN_LENGTH = 1200
SCREEN_WIDTH = 750
screen = pygame.display.set_mode((SCREEN_LENGTH, SCREEN_WIDTH)) # set screen size
pygame.display.set_caption("2D Particle Simulator")
clock = pygame.time.Clock()

manager = pygame_gui.UIManager((SCREEN_LENGTH, SCREEN_WIDTH))
manager.get_theme().load_theme('theme.json')

dt = 1/60       # Period, i.e the time each frame takes

class Particle():
    def __init__(self, x, y, radius, mass, vx, vy, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.diameter = 2 * radius
        self.mass = mass # used for particle collision
        self.vx = vx
        self.vy = vy
        self.sprite = pygame.Surface((self.diameter, self.diameter), pygame.SRCALPHA)
        pygame.draw.circle(self.sprite, color, (radius,radius), radius)    # radius is 10

# the velocity is in px/sec

p1 = Particle(200, 200, 10, -10, -150, 90, "white")  # posx, posy, vx, vy, color
p2 = Particle(600, 250, 10, 10, 120, -70, "green")   # velocities are in pixels/sec
# p3 = Particle(100, 50, -4, 3, "red")
# p4 = Particle(300, 50, -4, 3, "blue")

particles = [p1, p2]

# Creating the UI for controlling particles

PANEL_WIDTH = 300
layout = pygame.Rect(0, 0, PANEL_WIDTH, SCREEN_WIDTH)   # width = 750 in your script = screen height
layout.topright = (0, 0) 

frame = pygame_gui.elements.UIPanel(
    starting_height=1,                                 # Layer depth
    relative_rect=layout,
    manager=manager,
    object_id="#sidebar",         # Matches the ID in our theme string above
    anchors={
        'top': 'top',
        'bottom': 'bottom',
        'left': 'right',
        'right': 'right'
    }
)

layout = pygame.Rect(0, 10, PANEL_WIDTH, 30)

title = pygame_gui.elements.UILabel(relative_rect=layout,
                                    text="Particle Simulator 2D",
                                    manager=manager,
                                    container=frame,
                                    anchors={
                                        "centerx": "centerx",
                                        "top":"top",
                                    }

)

layout = pygame.Rect(0, 0, 120, 30)
layout.bottomright = (0,0)

hello_button = pygame_gui.elements.UIButton(relative_rect=layout,
                                             text='Say Hello',
                                             manager=manager,
                                             container=frame,
                                             anchors={'right': 'right',
                                            'bottom': 'bottom'})

time.sleep(0.5)   # short delay before sim starts

is_running = True

while is_running:
    time_delta = clock.tick(60)
    screen.fill((0, 0, 0))

    for i in particles:
        i.x += i.vx * dt    # multiplying with frame rate converts velocity from px/frame -> px/second
        i.y += i.vy * dt

        # wall collisions
        if i.x < 0 or (i.x + i.diameter) > (SCREEN_LENGTH - PANEL_WIDTH):
            i.vx = -i.vx
            if i.x < 0:     # manually setting the ball in the frame so it doesn't stick at the edge
                i.x = 0
            elif (i.x + i.diameter) > SCREEN_LENGTH:
                i.x = SCREEN_LENGTH - i.diameter

        if i.y < 0 or (i.y + i.diameter) > SCREEN_WIDTH:
            i.vy = -i.vy
            if i.y < 0:     # manually setting the ball in the frame so it doesn't stick at the edge
                i.y = 0
            elif (i.y + i.diameter) > SCREEN_WIDTH:
                i.y = SCREEN_WIDTH - i.diameter
    
        i.vector = pygame.Vector2(i.x, i.y)    # converts the numerical coordinates into pygame vectors

    # particle collisions
    if p1.vector.distance_to(p2.vector) < (p1.radius + p2.radius):
        p1.vx, p2.vx = p2.vx, p1.vx
        p1.vy, p2.vy = p2.vy, p1.vy

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == hello_button:
                print('Hello World!')

        manager.process_events(event)

    manager.update(time_delta)

    for i in particles:
        screen.blit(i.sprite, (i.x,i.y))   # updates the position of particle in screen

    manager.draw_ui(screen)

    pygame.display.update()

pygame.quit()
exit()
print("Particle Sim 2D is closed.")
