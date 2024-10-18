import pygame
import game
from classFish import Fish

pygame.init()

import settings
import render
import random


class GUI:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

        self.mouse_pos = (0, 0)
        self.mouse_button = 0
        self.key = ""

        self.next_state = ""
        self.transition_time = 0
        self.loading_bar = 0

        self.field_x = 0
        self.field_y = 0
        self.current_fish_selected = 2
        self.current_rotation = 1

        self.current_lengths = [2, 3, 3, 4, 5]


    def initialize(self):
        self.running = True
        self.state = "main menu"

        self.game = game.Game()

        pygame.display.set_caption("Fischeversenken")
        self.display = pygame.display.set_mode(
            (self.width, self.height)
        )

        self.clock = pygame.time.Clock()

        self.main()


    def main(self):
        while self.running:
            self.handle_events() # Handle input events

            self.button1 = False
            self.button2 = False

            if self.state == "main menu":
                self.main_menu() # Execute all main menu functions
                render.render_mainmenu(self.display, self.button1, self.button2)

            if self.transition_time > 0: # Transition animation
                self.transition_time -= 1
                if self.transition_time < 180: # Speedup the progress bar
                    self.loading_bar += int(self.transition_time / (random.randrange(1, 30)) / 3)
                render.transition(self.display, self.transition_time, self.loading_bar)
                if self.transition_time == 0: # Switch to next stage after done
                    self.state = self.next_state
                    self.next_state = ""
            
            if self.state == "placing":
                self.placing_menu()
                render.render_placing_menu(self.display, self.field_x, self.field_y,
                    self.current_lengths, self.current_fish_selected)
                
                # Preview fish
                preview_fish = Fish(
                    self.field_x, self.field_y,
                    self.current_rotation,
                    self.current_fish_selected,
                    None
                )
                if self.current_fish_selected != 0:
                    render.render_fish(
                        self.display, 541, 242,
                        [preview_fish], True
                        )

                render.render_fish(
                    self.display, 541, 242,
                    self.game.getPlayerFish("player1"), False)

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
            check_pos[0] <= rect_pos[0] + rect_size[0] and
            check_pos[1] <= rect_pos[1] + rect_size[1]):
            return True
        return False
    

    def main_menu(self):
        # Play button
        if self.is_in_rect(self.mouse_pos, (735, 410), (129, 79)):
            self.button1 = True
        else:
            self.button1 = False
        
        # Play button click function
        if self.mouse_button == 1 and self.button1:
            self.next_state = "placing"
            self.transition_time = 30 * 2 #7 Seconds
            self.loading_bar = 0

            self.current_fish_selected = 2
            self.current_rotation = 1
            self.current_lengths = [2, 3, 3, 4, 5]


        # Exit button
        if self.mouse_pos[0] > 1472 and self.mouse_pos[1] > 858:
            self.button2 = True
        else:
            self.button2 = False
        
        # Exit button click function
        if self.mouse_button == 1 and self.button2:
            self.running = False


    def placing_menu(self):
        # Check in field position once hovering over it
        if self.is_in_rect(self.mouse_pos, (541, 242), (500, 500)):
            self.field_x = int((self.mouse_pos[0] - 541) / 50)
            self.field_y = int((self.mouse_pos[1] - 242) / 50)
            pygame.display.set_caption(f"Fischeversenken {self.field_x} {self.field_y}")
        
        # Selecting fish sizes
        if self.mouse_button == 1: # Left mouse button check
            if self.is_in_rect(self.mouse_pos, (198, 262), (204, 165)):
                if self.current_lengths.count(2) > 0:
                    self.current_fish_selected = 2 # 2x1 Fish
            if self.is_in_rect(self.mouse_pos, (198, 427), (276, 159)):
                if self.current_lengths.count(3) > 0:
                    self.current_fish_selected = 3 # 3x1 Fish
            if self.is_in_rect(self.mouse_pos, (1087, 268), (381, 152)):
                if self.current_lengths.count(4) > 0:
                    self.current_fish_selected = 4 # 4x1 Fish
            if self.is_in_rect(self.mouse_pos, (1087, 420), (455, 142)):
                if self.current_lengths.count(5) > 0:
                    self.current_fish_selected = 5 # 5x1 Fish
        
        # Rotation fish with mouse wheel (Mouse button 4 + 5)
        if self.mouse_button == 4:
            self.current_rotation -= 1
            if self.current_rotation < 0: self.current_rotation = 3
        if self.mouse_button == 5:
            self.current_rotation += 1
            if self.current_rotation > 3: self.current_rotation = 0
        
        # shooting
        if self.mouse_button == 1 and self.current_fish_selected != 0:
            if self.is_in_rect(self.mouse_pos, (541, 242), (500, 500)):
                success = self.game.placeFish(
                    self.field_x, self.field_y,
                    self.current_rotation, self.current_fish_selected
                )
                if success:
                    if self.current_lengths.count(self.current_fish_selected) > 0:
                        self.current_lengths.remove(self.current_fish_selected)
                    if (self.current_lengths.count(self.current_fish_selected) == 0):
                        if len(self.current_lengths) > 0:
                            self.current_fish_selected = self.current_lengths[0]
                        else:
                            self.current_fish_selected = 0
        
        # Removing fish
        if self.mouse_button == 3:
            if self.is_in_rect(self.mouse_pos, (541, 242), (500, 500)):
                removed_fish_length = self.game.removeFish(self.field_x, self.field_y)
                if removed_fish_length > 0:
                    self.current_lengths.append(removed_fish_length)
                    self.current_fish_selected = removed_fish_length




gui = GUI(settings.width, settings.height)
guiasdr = GUI(settings.width, settings.height)
gui.initialize()