import pygame
import settings


# Textures
main_menu_background = pygame.image.load("assets\\main menu.png")
placing_menu_background = pygame.image.load("assets\\placing menu.png")
shoot_menu_background = pygame.image.load("assets\\shoot menu.png")
end_screen_p_background = pygame.image.load("assets\\end screen player.png")
end_screen_ai_background = pygame.image.load("assets\\end screen ai.png")

fish_l2 = pygame.image.load("assets\\fish l2.png")
fish_l3 = pygame.image.load("assets\\fish l3.png")
fish_l4 = pygame.image.load("assets\\fish l4.png")
fish_l5 = pygame.image.load("assets\\fish l5.png")

shot_hit = pygame.image.load("assets\\shot_hit.png")
shot_miss = pygame.image.load("assets\\shot_miss.png")

fish_count_on = pygame.image.load("assets\\fish count on.png")
fish_count_off = pygame.image.load("assets\\fish count off.png")

main_menu_font = pygame.font.Font("assets\\impact.ttf", 64)
exit_button_font = pygame.font.Font("assets\\impact.ttf", 32)
fish_count_font = pygame.font.Font("assets\\impact.ttf", 50)
start_game_font = pygame.font.Font("assets\\impact.ttf", 58)
ai_status_font = pygame.font.Font("assets\\impact.ttf", 20)


def render_mainmenu(display, button1, button2):
    display.blit(main_menu_background, (0, 0))
    
    # Play button
    # 744, 410 - 855, 489
    text_color = "#69c7bf"
    if button1: text_color = "#c4e5e9"
    text_texture = main_menu_font.render("Start", True, text_color)
    display.blit(
        text_texture,
        (
            800 - (text_texture.get_width() / 2),
            450 - (text_texture.get_height() / 2)
        )
    )

    # Exit button
    # 735, 410 - 864, 489
    text_color = "#5e88ae"
    if button2: text_color = "#96c1f2"
    text_texture = exit_button_font.render("Piss dich", True, text_color)
    display.blit(
        text_texture,
        (
            1472,
            858
        )
    )


def show_fish_count(display, pos, count):
    text_color = "#CCCCCC"
    if count == 0: text_color = "#999999"
    text_texture = fish_count_font.render(f"{count}x", True, text_color)
    display.blit(
        text_texture,
        pos
    )


def render_placing_menu(display, field_x, field_y, fish_left, selected, button1, button2, mouse_in_field):
    display.blit(placing_menu_background, (0, 0))
    if mouse_in_field:
        pygame.draw.rect(display, "#8b5555",
            pygame.Rect(field_x * 50 + 541, field_y * 50 + 242, 50, 50),
            5, 3)
    
    # White selection box
    if selected == 2: # 2x1 Fish
        pygame.draw.rect(display, "#EEEEEE",
        pygame.Rect(198, 262, 244, 165),
        5, 3)
    if selected == 3: # 3x1 Fish
        pygame.draw.rect(display, "#EEEEEE",
        pygame.Rect(198, 427, 276, 159),
        5, 3)
    if selected == 4: # 4x1 Fish
        pygame.draw.rect(display, "#EEEEEE",
        pygame.Rect(1087, 268, 381, 152),
        5, 3)
    if selected == 5: # 5x1 Fish
        pygame.draw.rect(display, "#EEEEEE",
        pygame.Rect(1087, 420, 455, 142),
        5, 3)
    
    # Fish count text
    show_fish_count(display, (358, 269), fish_left.count(2))
    show_fish_count(display, (380, 436), fish_left.count(3))
    show_fish_count(display, (1266, 273), fish_left.count(4))
    show_fish_count(display, (1278, 420), fish_left.count(5))

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


def render_end_screen(display, button1, whoWon):
    if whoWon == "player":
        display.blit(end_screen_p_background, (0, 0))
    else:
        display.blit(end_screen_ai_background, (0, 0))
    
    # Exit button 110, 40
    text_color = "#7c6784"
    if button1: text_color = "#ffffff"
    text_texture = main_menu_font.render("Amen", True, text_color)
    display.blit(
        text_texture,
        (
            269,
            138
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


def render_fish(display, offsetX, offsetY, fish_list, preview):
    for fish in fish_list:
        fish_texture = fish_l2
        if fish.length == 2: fish_texture = fish_l2
        if fish.length == 3: fish_texture = fish_l3
        if fish.length == 4: fish_texture = fish_l4
        if fish.length == 5: fish_texture = fish_l5
        if preview:
            fish_texture.set_alpha(120)
        else:
            fish_texture.set_alpha(255)

        if fish.direction == 0:
            fish_texture = pygame.transform.rotate(fish_texture, 90)
            position = (fish.posXY[0] * 50 + offsetX, (fish.posXY[1] - fish.length + 1) * 50 + offsetY)
            display.blit(fish_texture, position)
        if fish.direction == 1:
            position = (fish.posXY[0] * 50 + offsetX, fish.posXY[1] * 50 + offsetY)
            display.blit(fish_texture, position)
        if fish.direction == 2:
            fish_texture = pygame.transform.rotate(fish_texture, -90)
            position = (fish.posXY[0] * 50 + offsetX, fish.posXY[1] * 50 + offsetY)
            display.blit(fish_texture, position)
        if fish.direction == 3:
            fish_texture = pygame.transform.flip(fish_texture, True, False)
            position = ((fish.posXY[0] - fish.length + 1) * 50 + offsetX, fish.posXY[1] * 50 + offsetY)
            display.blit(fish_texture, position)


def transition(display, transition_time, loading_bar, bar_direction,t_time):
    if transition_time > (t_time-30):
        overlay = pygame.Surface((1600, 900))
        overlay.set_alpha(255 / 30 * (t_time-transition_time))
        overlay.fill((15, 48, 66))

        display.blit(overlay, (0, 0))
    else:
        display.fill((15, 48, 66))

        pygame.draw.rect(
            display, "#aecfe3",
            pygame.Rect(800 - 300, 450 - 20, 600, 40),
            5
        )
        if bar_direction == 0:
            if 1090 / 650 * loading_bar + 800 - 290 >= 1600:
                pygame.draw.rect(
                    display, "#aecfe3",
                    pygame.Rect(0, 450 - 10,
                    (1090 / 650 * loading_bar) - 1090,
                    20)
                )
            if 1090 / 650 * loading_bar + 800 - 290-1090 >= 510:
                pygame.draw.rect(
                    display, "#aecfe3",
                    pygame.Rect(490, 450 - 10,20,
                    (1090 / 650 * loading_bar) - 1090-510)
                )
                if ((1090 / 650 * loading_bar) - 1090-510>900):
                    pygame.draw.rect(
                    display, "#aecfe3",
                    pygame.Rect(900, 0,20,
                    min((1090 / 650 * loading_bar) - 1090-510-900,450))
                )
                

            pygame.draw.rect(
                display, "#aecfe3",
                pygame.Rect(800 - 290, 450 - 10,
                1090 / 650 * loading_bar,
                20)
            )
        #rect(x-mitte - x-offset, y-Mitte - Y-Offset, Länge-x, länge-Y)
        else:
            pygame.draw.rect(
                display, "#aecfe3",
                pygame.Rect(800 - 290, 450 - 10,
                1090 - 1090 / 650 * loading_bar,
                20)
            )
            if (1090 - 1090 / 650 * loading_bar) <= 0:
                pygame.draw.rect(
                display, "#aecfe3",
                pygame.Rect(800 - 290+1090 - 1090 / 650 * loading_bar, 450 - 10,
                -(1090 - 1090 / 650 * loading_bar),
                20)
                )
           # 1600x900

        loading_text = "Angel Fische"
        if 400 >= loading_bar > 200: loading_text = "Rotte Wale aus"
        if 600 >= loading_bar > 400: loading_text = "Starte Atomreaktor"
        if 800 >= loading_bar > 600: loading_text = "Trainiere KI"
        if loading_bar > 800: loading_text = "Kompiliere Shader"

        if bar_direction == -1: loading_text = "Entlade Shader"

        dot_text = "."
        dot_timer = transition_time % 40
        if 10 <= dot_timer < 20: dot_text = ".."
        if 20 <= dot_timer < 30: dot_text = "..."
        if 30 <= dot_timer < 40: dot_text = ".."
        loading_text += dot_text

        text_texture = exit_button_font.render(loading_text, True, "#aecfe3")
        display.blit(
            text_texture,
            (
                500,
                380
            )
        )