import settings
import ai_model
import pygame


main_menu_background = pygame.image.load("assets\\main menu.png")
main_menu_font = pygame.font.Font("assets\\impact.ttf", 64)
exit_button_font = pygame.font.Font("assets\\impact.ttf", 32)

def main_menu(main):
    # Play button
    if main.is_in_rect(main.mouse_pos, (735, 410), (129, 79)):
        main.button1 = True
    else:
        main.button1 = False
    
    # AI testing
    if settings.ai_mode:
        if main.transition_time == 0:
            main.button1 = True
            main.mouse_button = 1
    
    # Play button click function
    if main.mouse_button == 1 and main.button1 and main.transition_time == 0:
        main.next_state = "placing"
        main.transition_time = 30 * 10 #15 Seconds
        main.t_time = main.transition_time
        main.loading_bar = 0
        main.bar_direction = 0

        main.game.reset()
        ai_model.resetAI()
        main.last_ai_shot = 0
        main.current_fish_selected = 2
        main.current_rotation = 1
        main.current_lengths = settings.fish_lengths.copy().copy()


    # Exit button
    if main.mouse_pos[0] > 1472 and main.mouse_pos[1] > 858:
        main.button2 = True
    else:
        main.button2 = False
    
    # Exit button click function
    if main.mouse_button == 1 and main.button2 and main.transition_time == 0:
        main.running = False
    

    render_mainmenu(main.display, main.button1, main.button2)


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