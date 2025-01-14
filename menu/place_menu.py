import settings
import pygame
import random
from classFish import Fish
from menu.show_fish import render_fish


placing_menu_background = pygame.image.load("assets\\placing menu.png")
touch_placing_menu_background = pygame.image.load("assets\\placing menu touch.png")
shot_hit = pygame.image.load("assets\\shot_hit.png")
shot_miss = pygame.image.load("assets\\shot_miss.png")
square_block = pygame.image.load("assets\\block.png")

rotate_fish = pygame.image.load("assets\\rotate fish.png")
delete_fish = pygame.image.load("assets\\delete fish.png")

exit_button_font = pygame.font.Font("assets\\impact.ttf", 32)
start_game_font = pygame.font.Font("assets\\impact.ttf", 58)
fish_count_font = pygame.font.Font("assets\\impact.ttf", 50)



def place_menu(main):
    # Start fight button
    if main.is_in_rect(main.mouse_pos, (1100, 590), (235, 128)):
        main.button1 = True
    else:
        main.button1 = False
    
    # AI testing
    if main.ai_mode:
        if main.transition_time == 0:
            main.current_lengths = []
            main.button1 = True
            main.mouse_button = 1
    
    # Start fight button click function
    if (main.mouse_button == 1 and main.button1 and
        main.transition_time == 0 and len(main.current_lengths) == 0):
        main.next_state = "shoot menu"
        main.transition_time = 30 * 4 #4 Seconds
        main.t_time = main.transition_time
        main.loading_bar = 0
        main.bar_direction = 0

        main.ai_fish_preview = False
        
        main.game.placeAiFish(main.fish_preset)
        main.ai_timer = settings.ai_processing_time
        
        if main.ai_mode:
            from aiPlace import aiPlace
            aiPlace(main.game.player1, main.fish_preset,main.game.blockList)
            main.ai_fish_preview = True
            if random.choice([True, False]): # Either AI 1 or AI 2 starts the shooting
                success = 1
                while success > 0:
                    success = main.game.aiShoot()[0]




    # Exit button
    if main.is_in_rect(main.mouse_pos, (20, 30), (110, 40)):
        main.button2 = True
    else:
        main.button2 = False
    
    # Exit button click function
    if main.mouse_button == 1 and main.button2 and main.transition_time == 0:
        main.next_state = "main menu"
        main.transition_time = 30 * 7 #7 Seconds
        main.t_time = main.transition_time
        main.loading_bar = 0
        main.bar_direction = -1


    # Check in field position once hovering over it
    if main.is_in_rect(main.mouse_pos, (541, 242), (500, 500)):
        main.field_x = int((main.mouse_pos[0] - 541) / 50)
        main.field_y = int((main.mouse_pos[1] - 242) / 50)
        main.mouse_in_field = True

    # delete fish button for touch mode
    if main.is_in_rect(main.mouse_pos, (423, 512), (100, 100)) and main.mouse_button == 1:
        main.delete_fish_mode = not main.delete_fish_mode
    
    # Rotate fish button for touch mode
    if main.is_in_rect(main.mouse_pos, (423, 642), (100, 100)) and main.mouse_button == 1:
        main.mouse_button = 5

    # Rotation fish with mouse wheel (Mouse button 4 + 5)
    if main.mouse_button == 4:
        main.current_rotation -= 1
        if main.current_rotation < 0: main.current_rotation = 3
    if main.mouse_button == 5:
        main.current_rotation += 1
        if main.current_rotation > 3: main.current_rotation = 0
    
    # Placing fish
    if main.mouse_button == 1 and main.current_fish_selected != 0 and not main.ai_mode and not main.delete_fish_mode:
        if main.is_in_rect(main.mouse_pos, (541, 242), (500, 500)):
            success = main.game.placeFish(
                (main.field_x, main.field_y),
                main.current_rotation, main.current_fish_selected
            )
            if success:
                if main.current_lengths.count(main.current_fish_selected) > 0:
                    main.current_lengths.remove(main.current_fish_selected)
                if (main.current_lengths.count(main.current_fish_selected) == 0):
                    if len(main.current_lengths) > 0:
                        main.current_fish_selected = main.current_lengths[0]
                    else:
                        main.current_fish_selected = 0
    
    # Removing fish
    if main.mouse_button == 3 or (main.mouse_button == 1 and main.delete_fish_mode):
        if main.is_in_rect(main.mouse_pos, (541, 242), (500, 500)):
            removed_fish_length = main.game.removeFish((main.field_x, main.field_y))
            if removed_fish_length > 0:
                main.current_lengths.append(removed_fish_length)
                main.current_fish_selected = removed_fish_length
                if main.delete_fish_mode:
                    main.delete_fish_mode = False
    

    if not main.ai_mode:
        render_placing_menu(main.display, main.field_x, main.field_y,
            main.current_lengths, main.current_fish_selected,
            main.button1, main.button2, main.mouse_in_field, main.touch_mode)
        render_blocks(
            main.display, 541, 242,
            main.game.getShotList("player1"))

        # touch mode deleting mode
        if main.delete_fish_mode:
            pygame.draw.rect(main.display, "#8b5555",
                        pygame.Rect(541, 242, 500, 500),
                        5, 3)
            text_texture = exit_button_font.render("Tippe auf Fisch", True, "#8b5555")
            main.display.blit(
                text_texture,
                (
                    692,
                    200
                )
            )
        
        # Preview of placing a new fish
        if main.current_fish_selected != 0 and not main.delete_fish_mode:

            if main.touch_mode:
                preview_fish = Fish(
                    (0, 0),
                    1,
                    main.current_fish_selected,
                    None
                )
                render_fish(
                    main.display, 678, 750,
                    [preview_fish], True
                    )
            
            preview_fish = Fish(
                (main.field_x, main.field_y),
                main.current_rotation,
                main.current_fish_selected,
                None
            )
            render_fish(
                main.display, 541, 242,
                [preview_fish], True
                )

        # Render player's fishies
        render_fish(
            main.display, 541, 242,
            main.game.getPlayerFish("player1"), False)



def render_placing_menu(display, field_x, field_y, fish_left, selected, button1, button2, mouse_in_field, touch_mode):
    if not touch_mode:
        display.blit(placing_menu_background, (0, 0))
    else:
        display.blit(touch_placing_menu_background, (0, 0))

        display.blit(rotate_fish, (423, 642))
        display.blit(delete_fish, (423, 512))


    if mouse_in_field and not touch_mode:
        pygame.draw.rect(display, "#8b5555",
            pygame.Rect(field_x * 50 + 541, field_y * 50 + 242, 50, 50),
            5, 3)

    # Exit button 110, 40
    text_color = "#b86145"
    if button2: text_color = "#ca8a75"
    text_texture = exit_button_font.render("Rückzug", True, text_color)
    display.blit(
        text_texture,
        (
            20,
            30
        )
    )

    # current fish text
    if touch_mode:
        text_texture = exit_button_font.render("Platziere: ", True, "#609fe0")
        display.blit(
            text_texture,
            (
                550,
                750
            )
        )

    # Start fight button
    text_color = "#69c7bf"
    if button1: text_color = "#c4e5e9"
    if len(fish_left) > 0: text_color = "#223143"
    text_texture = start_game_font.render("Hans! Get", True, text_color)
    display.blit(
        text_texture,
        (
            1100,
            590
        )
    )
    # Start fight button 2
    text_color = "#69c7bf"
    if button1: text_color = "#c4e5e9"
    if len(fish_left) > 0: text_color = "#223143"
    text_texture = start_game_font.render("the Angel!", True, text_color)
    display.blit(
        text_texture,
        (
            1100,
            645
        )
    )

def render_blocks(display, offsetX, offsetY, shot_list):
    for shot in shot_list:
        position = (
            shot[0][0] * 50 + offsetX,
            shot[0][1] * 50 + offsetY
        )
        if shot[1] == "miss":
            display.blit(shot_miss, position)
        elif not shot[1] == "block":
            display.blit(shot_hit, position)
        else:
            display.blit(square_block,position)
