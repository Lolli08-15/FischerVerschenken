import pygame
import game


pygame.init()

import settings

from menu.main_menu import main_menu
from menu.place_menu import place_menu
from menu.shoot_menu import shoot_menu
from menu.end_menu import end_menu

from menu.transition import transition


class GUI:
    def __init__(self, width, height) -> None:
        # Initializinh attributes
        self.width = width
        self.height = height

        self.mouse_pos = (0, 0)
        self.mouse_button = 0
        self.key = ""

        self.next_state = ""
        self.transition_time = 0
        self.t_time = 0
        self.loading_bar = 0
        self.bar_direction = 0

        self.ai_timer = settings.ai_processing_time

        self.field_x = 0
        self.field_y = 0
        self.current_fish_selected = 2
        self.current_rotation = 1

        self.ai_win = 0
        self.player_win = 0

        self.current_lengths = settings.fish_lengths.copy()
        self.ai_fish_preview = False


    def initialize(self):
        self.running = True

        """
        The current state of the programm

        "main menu" - The main menu of the game
        "placing" - The placing fish phase
        "shoot menu" - Main loop of the game. Player and enemy are shooting
        "end screen" - The game is over and someone won

        """
        self.state = "main menu"

        self.game = game.Game() # Game object for handling the gameplay logic

        pygame.display.set_caption("Fischeversenken") # Set title

        # Initialize Window
        self.display = pygame.display.set_mode(
            (self.width, self.height)
        )

        icon = pygame.image.load("assets\\icon.png")

        pygame.display.set_icon(icon)

        self.clock = pygame.time.Clock()

        self.main() # Start the main loop


    def main(self):
        while self.running:
            self.handle_events() # Handle all input events

            # "Hovering over a button" variables reset back to False
            self.button1 = False
            self.button2 = False
            self.mouse_in_field = False

            if self.state == "main menu":
                main_menu(self)
            

            if self.state == "placing":
                place_menu(self)
            

            if self.state == "shoot menu":
                shoot_menu(self)
            

            if self.state == "end screen":
                end_menu(self)
            

            if self.transition_time > 0: # Transition animation
                transition(self)


            pygame.display.flip()
            self.clock.tick(30)
    

    def handle_events(self):
        self.mouse_button = 0
        self.key = ""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_button = event.dict["button"]
                self.mouse_pos = event.dict["pos"]
            if event.type == pygame.MOUSEMOTION:
                self.mouse_pos = event.dict["pos"]
            if event.type == pygame.KEYDOWN:
                self.key = event.dict["unicode"]


    def is_in_rect(self, check_pos, rect_pos, rect_size):
        if (check_pos[0] >= rect_pos[0] and
            check_pos[1] >= rect_pos[1] and
            check_pos[0] < rect_pos[0] + rect_size[0] and
            check_pos[1] < rect_pos[1] + rect_size[1]):
            return True
        return False








gui = GUI(settings.width, settings.height)
gui.initialize()