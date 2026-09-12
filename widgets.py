import pygame
import pygame_gui

class Widget:
    @classmethod    # used to setup manager, frame
    def initialize(cls, SCREEN_LENGTH, SCREEN_WIDTH, PANEL_WIDTH):
        cls.manager = pygame_gui.UIManager((SCREEN_LENGTH, SCREEN_WIDTH))
        cls.manager.get_theme().load_theme('theme.json')

        layout = pygame.Rect(0, 0, PANEL_WIDTH, SCREEN_WIDTH)
        layout.topright(0,0)

        cls.frame = pygame_gui.elements.UIPanel(starting_height=1,                                 # Layer depth
                                            relative_rect=layout,
                                            manager=cls.manager,
                                            object_id="#sidebar",         # Matches the ID in our theme string above
                                            anchors={
                                                'top': 'top',
                                                'bottom': 'bottom',
                                                'left': 'right',
                                                'right': 'right'
                                            }
                                            )

    def __init__(self, id, type):
        self.id = id
        self.type = type
        print(f"Widget {id} has been initialized.")

    def create_label(self, coordinates_tuple=(0, 0, 20, 30)):
        layout = pygame.rect(*coordinates_tuple)
        self.widget = pygame_gui.elements.UILabel(relative_rect=layout,
                                    text="Particle Simulator 2D",
                                    manager=Widget.manager,
                                    container=Widget.frame,
                                    object_id="#title",
                                    anchors={
                                        "centerx": "centerx",
                                        "top":"top",
                                    }
                                    )