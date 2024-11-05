import settings
import pygame
from math import sin, pi


main_menu_background = pygame.image.load("assets\\main menu.png")
main_menu_font = pygame.font.Font("assets\\impact.ttf", 64)
exit_button_font = pygame.font.Font("assets\\impact.ttf", 32)

splash_font = pygame.font.Font("assets\\Minecraft.otf", 50)

def main_menu(main):
    # Switch splash texts
    if main.key == "s":
        main.pick_splash()

    # Play button
    if main.is_in_rect(main.mouse_pos, (735, 410), (129, 79)):
        main.button1 = True
    else:
        main.button1 = False
    
    # AI testing
    if main.ai_mode:
        if main.transition_time == 0:
            main.button1 = True
            main.mouse_button = 1
    
    # Play button click function
    if main.mouse_button == 1 and main.button1 and main.transition_time == 0:
        if not main.ai_mode and main.selected_player[0] >= 0:
            main.ai_mode = True
            main.ai_win = 0
            main.player_win = 0
            main.ai_turns = 0
            main.player_turns = 0
            main.current_turns = 0

        main.next_state = "placing"
        main.transition_time = 30 * 10 #10 Seconds
        main.t_time = main.transition_time
        main.loading_bar = 0
        main.bar_direction = 0

        main.game.setAI(main.selected_ai[0])

        main.game.reset()
        if main.selected_player[0] >= 0:
            main.game.aiModelReset(main.selected_player[0])
        main.last_ai_shot = 0
        main.current_rotation = 1
        main.current_lengths = settings.get_fish_preset(main.fish_preset)
        main.current_fish_selected = main.current_lengths[0]


    # Exit button
    if main.mouse_pos[0] > 1472 and main.mouse_pos[1] > 858:
        main.button2 = True
    else:
        main.button2 = False
    
    # Exit button click function
    if main.mouse_button == 1 and main.button2 and main.transition_time == 0:
        main.running = False
    
    # Settings button
    if main.mouse_pos[0] < 170 and main.mouse_pos[1] > 858:
        main.button3 = True
    else:
        main.button3 = False
    
    # Settings button click function
    if main.mouse_button == 1 and main.button3 and main.transition_time == 0:
        main.next_state = "settings menu"
        main.transition_time = 30 * 3 #3 Seconds
        main.t_time = main.transition_time
        main.loading_bar = 0
        main.bar_direction = 0
    

    if not main.ai_mode:
        render_mainmenu(main.display, main.button1, main.button2, main.button3)
        render_splash(main, main.current_splash)


def render_mainmenu(display, button1, button2, button3):
    display.blit(main_menu_background, (0, 0))
    
    # Play button
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


    # Exit button
    # 735, 410 - 864, 489
    text_color = "#5e88ae"
    if button3: text_color = "#96c1f2"
    text_texture = exit_button_font.render("Ausstellung", True, text_color)
    display.blit(
        text_texture,
        (
            10,
            858
        )
    )

def render_splash(main, text):
    main.splash_timer += 1
    if main.splash_timer > 60:
        main.splash_timer = 0
    scale = sin(360 / 60 * main.splash_timer * pi / 180 * 2)
    scale = (scale + 45) / 80

    text_texture = splash_font.render(text, True, "#111111")
    text_texture = pygame.transform.rotate(text_texture, 18)
    text_texture = pygame.transform.smoothscale(text_texture, (
            text_texture.get_width() * scale,
            text_texture.get_height() * scale
        ))

    main.display.blit(
        text_texture,
        (
            1244 - text_texture.get_width() / 2,
            222 - text_texture.get_height() / 2
        )
    )

    text_texture = splash_font.render(text, True, "#f2f22f")
    text_texture = pygame.transform.rotate(text_texture, 18)
    text_texture = pygame.transform.smoothscale(text_texture, (
            text_texture.get_width() * scale,
            text_texture.get_height() * scale
        ))

    main.display.blit(
        text_texture,
        (
            1242 - text_texture.get_width() / 2,
            220 - text_texture.get_height() / 2
        )
    )