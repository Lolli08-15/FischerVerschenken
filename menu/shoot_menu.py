import settings
import pygame
import ai_model

from menu.show_fish import render_fish


shoot_menu_background = pygame.image.load("assets\\shoot menu.png")
shot_hit = pygame.image.load("assets\\shot_hit.png")
shot_miss = pygame.image.load("assets\\shot_miss.png")
fish_count_on = pygame.image.load("assets\\fish count on.png")
fish_count_off = pygame.image.load("assets\\fish count off.png")

exit_button_font = pygame.font.Font("assets\\impact.ttf", 32)
ai_status_font = pygame.font.Font("assets\\impact.ttf", 20)


def shoot_menu(main):
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
    
    # Shooting
    if main.mouse_button == 1 and main.ai_timer == settings.ai_processing_time:
        if main.is_in_rect(main.mouse_pos, (887, 285), (500, 500)) and main.transition_time == 0:
            success = main.game.playerShoot((main.field_x, main.field_y))
            if success != False:
                if success == "miss":
                    main.ai_timer -= 1

    # AI testing
    if settings.ai_mode:
        if main.ai_timer == settings.ai_processing_time and main.transition_time == 0:
            position = ai_model.shootAI(main.last_ai_shot)
            success = main.game.playerShoot(position)
            if success == "hit": main.last_ai_shot = 1
            elif success == "sunk": main.last_ai_shot = 2
            else:
                main.last_ai_shot = 0
                main.ai_timer -= 1
    
    # Preview AI fishes
    if main.key == "m": main.ai_fish_preview = not main.ai_fish_preview
    if main.key == "n": main.game.ai.fishes[0].hits += 1000

    render_shoot_menu(main.display, main.field_x, main.field_y,
        main.button2, main.ai_timer, main.transition_time,
        main.mouse_in_field)

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
        main.game.getSunkenFish("player1")
        )
    # And for the player
    render_fish_count(main.display,
        210, 785,
        main.game.getSunkenFish("ai")
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



def render_shoot_menu(display, field_x, field_y, button2, ai_timer, transition_time, mouse_in_field):
    display.blit(shoot_menu_background, (0, 0))
    if (ai_timer == settings.ai_processing_time and
        transition_time == 0 and
        mouse_in_field):
        pygame.draw.rect(display, "#8bbfc8",
            pygame.Rect(field_x * 50 + 887, field_y * 50 + 285, 50, 50),
            5, 3)
    
    # Exit button 110, 40
    text_color = "#b86145"
    if button2: text_color = "#ffb9b9"
    text_texture = exit_button_font.render("Rückzug", True, text_color)
    display.blit(
        text_texture,
        (
            20,
            30
        )
    )

    if ai_timer > settings.ai_processing_time * 0.35 and ai_timer < settings.ai_processing_time:
        text_texture = ai_status_font.render("Der Feind denkt!", True, "#f2282f")
        display.blit(
            text_texture,
            (
                460 - text_texture.get_width() / 2,
                260
            )
        )
    if ai_timer <= settings.ai_processing_time * 0.35:
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
        else:
            display.blit(shot_hit, position)


def render_fish_count(display, offsetX, offsetY, count):
    for i in range(1, 6):
        position = (
            (i - 1) * 50 + offsetX,
            offsetY
        )
        if i > 5 - count:
            display.blit(fish_count_off, position)
        else:
            display.blit(fish_count_on, position)