import settings
import pygame

from menu.show_fish import render_fish


shoot_menu_background = pygame.image.load("assets\\shoot menu.png")
shoot_menu_ai_background = pygame.image.load("assets\\shoot menu ai.png")

shot_hit = pygame.image.load("assets\\shot_hit.png")
shot_miss = pygame.image.load("assets\\shot_miss.png")
square_block = pygame.image.load("assets\\block.png")
fish_count_on = pygame.image.load("assets\\fish count on.png")
fish_count_off = pygame.image.load("assets\\fish count off.png")

exit_button_font = pygame.font.Font("assets\\impact.ttf", 32)
ai_status_font = pygame.font.Font("assets\\impact.ttf", 20)


def shoot_menu(main):
    # Exit button
    if main.is_in_rect(main.mouse_pos, (20, 30), (110, 40)):
        main.button2 = True
    else:
        main.button2 = False
    
    # Exit button click function
    if main.mouse_button == 1 and main.button2 and main.transition_time == 0:
        main.pick_splash()
        main.next_state = "main menu"
        main.transition_time = 30 * 7 #7 Seconds
        main.t_time = main.transition_time
        main.loading_bar = 0
        main.bar_direction = -1

    if main.ai_mode and (main.button2 and main.last_mouse_button == 1):
        main.pick_splash()
        main.next_state = "main menu"
        main.transition_time = 30 * 7 #7 Seconds
        main.t_time = main.transition_time
        main.loading_bar = 0
        main.bar_direction = -1

        main.ai_mode = False
        main.next_state = "end screen"
        main.whoWon = "ai testing"


    if main.ai_mode:
        isRunning = True
        while isRunning:
            success = "hit"
            while success != "miss":
                position = main.game.aiModelShoot(main.selected_player[0], main.last_ai_shot)
                success = main.game.playerShoot(position)
                main.current_p_turns += 1
                if success == "hit":
                    main.last_ai_shot = 1
                elif success == "sunk":
                    main.last_ai_shot = 2
                else:
                    main.last_ai_shot = 0
                    success = "miss"

            success = 1
            while success > 0:
                success = main.game.aiShoot()
                main.current_a_turns += 1

            whoWon = main.game.detectWin()
            if whoWon != False and main.transition_time == 0:
                main.whoWon = whoWon
                main.ai_timer = settings.ai_processing_time

                main.next_state = "end screen"
                main.transition_time = 30 * 3 #3 Seconds
                main.t_time = main.transition_time-50
                main.loading_bar = 0
                main.bar_direction = 0
                
                main.ai_fish_preview = True
                isRunning = False
        
    else: 
        if main.ai_timer < settings.ai_processing_time:
            main.ai_timer -= 1
            
            if main.ai_timer == int(settings.ai_processing_time * 0.35):
                success = main.game.aiShoot()
                if success > 0:
                    main.ai_timer = settings.ai_processing_time - 1

            if main.ai_timer < 1:
                main.ai_timer = settings.ai_processing_time


        # Check in field position once hovering over it
        if main.is_in_rect(main.mouse_pos, (887, 285), (500, 500)):
            main.field_x = int((main.mouse_pos[0] - 887) / 50)
            main.field_y = int((main.mouse_pos[1] - 285) / 50)
            main.mouse_in_field = True
        

        
        # Shooting
        if main.mouse_button == 1 and main.ai_timer == settings.ai_processing_time:
            if main.is_in_rect(main.mouse_pos, (887, 285), (500, 500)) and main.transition_time == 0:
                success = main.game.playerShoot((main.field_x, main.field_y))
                if success != False:
                    if success == "miss":
                        main.ai_timer -= 1

        
        # Preview AI fishes
        if main.key == "m": main.ai_fish_preview = not main.ai_fish_preview

    render_shoot_menu(main.display, main.field_x, main.field_y,
        main.button2, main.ai_timer, main.transition_time,
        main.mouse_in_field, main.ai_mode)

    if main.ai_mode:
        player_name = settings.get_ai_name(main.selected_ai[0]) # Show AI name above board
        text_texture = exit_button_font.render(player_name, True, "#67b1d7")
        main.display.blit(
            text_texture,
            (
                460 - text_texture.get_width() / 2,
                224
            )
        )

        player_name = settings.get_ai_name(main.selected_player[0]) # Show other AI name above board
        text_texture = exit_button_font.render(player_name, True, "#67b1d7")
        main.display.blit(
            text_texture,
            (
                1137 - text_texture.get_width() / 2,
                224
            )
        )

        # Show current wins for both AIs
        text_texture = exit_button_font.render(f"{main.ai_win} : {main.player_win}", True, "#67b1d7")
        main.display.blit(
            text_texture,
            (
                800 - text_texture.get_width() / 2,
                480
            )
        )
    if not main.ai_mode:
        render_fish(
            main.display, 210, 285,
            main.game.getPlayerFish("player1"), True)

        if main.ai_fish_preview:
            render_fish(
                main.display, 885, 285,
                main.game.getPlayerFish("ai"), True)
        
        # Render player + ai shots
        render_shots(
            main.display, 885, 285,
            main.game.getShotList("player1")
        )
        render_shots(
            main.display, 210, 285,
            main.game.getShotList("ai")
        )

        # Render sunk fish count for enemy field
        render_fish_count(main.display,
            887, 785,
            main.game.getSunkenFish("player1"),
            main.fish_preset
            )
        # And for the player
        render_fish_count(main.display,
            210, 785,
            main.game.getSunkenFish("ai"),
            main.fish_preset
            )
    
    whoWon = main.game.detectWin()
    if whoWon != False and main.transition_time == 0:
        main.whoWon = whoWon
        main.ai_timer = settings.ai_processing_time

        main.next_state = "end screen"
        main.transition_time = 30 * 3 #3 Seconds
        main.t_time = main.transition_time-50
        main.loading_bar = 0
        main.bar_direction = 0
        
        main.ai_fish_preview = True



def render_shoot_menu(display, field_x, field_y, button2, ai_timer, transition_time, mouse_in_field, ai_mode):
    if ai_mode:
        display.blit(shoot_menu_ai_background, (0, 0))
    else:
        display.blit(shoot_menu_background, (0, 0))


    if (ai_timer == settings.ai_processing_time and
        transition_time == 0 and
        mouse_in_field and not ai_mode):
        pygame.draw.rect(display, "#8bbfc8",
            pygame.Rect(field_x * 50 + 887, field_y * 50 + 285, 50, 50),
            5, 3)
    
    # Exit button 110, 40
    text_color = "#b86145"
    if button2: text_color = "#ffb9b9"
    text_texture = exit_button_font.render("Ruckzüg", True, text_color)
    display.blit(
        text_texture,
        (
            20,
            30
        )
    )

    if ai_timer > settings.ai_processing_time * 0.35 and ai_timer < settings.ai_processing_time and not ai_mode:
        text_texture = ai_status_font.render("Der Feind denkt!", True, "#f2282f")
        display.blit(
            text_texture,
            (
                460 - text_texture.get_width() / 2,
                260
            )
        )
    if ai_timer <= settings.ai_processing_time * 0.35 and not ai_mode:
        text_texture = ai_status_font.render("Der Feind schießt!", True, "#f2282f")
        display.blit(
            text_texture,
            (
                460 - text_texture.get_width() / 2,
                260
            )
        )




def render_shots(display, offsetX, offsetY, shot_list):
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


def render_fish_count(display, offsetX, offsetY, count, preset):
    for i in range(1, len(settings.get_fish_preset(preset)) + 1):
        position = (
            (i - 1) * 50 + offsetX,
            offsetY
        )
        if i > len(settings.get_fish_preset(preset)) - count:
            display.blit(fish_count_off, position)
        else:
            display.blit(fish_count_on, position)