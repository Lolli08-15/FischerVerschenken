import settings
import pygame


end_screen_p_background = pygame.image.load("assets\\end screen player.png")
end_screen_ai_background = pygame.image.load("assets\\end screen ai.png")

main_menu_font = pygame.font.Font("assets\\impact.ttf", 64)


def end_menu(main):
    # Play button
    if main.is_in_rect(main.mouse_pos, (269, 138), (149, 79)):
        main.button1 = True
    else:
        main.button1 = False

    # AI testing
    if settings.ai_mode:
        if main.transition_time == 0:
            main.button1 = True
            main.mouse_button = 1
            if main.whoWon == "player":
                main.player_win += 1
            else:
                main.ai_win += 1
            print("--------")
            print(f"AI Testing Model: {main.player_win}")
            print(f"AI Enemy: {main.ai_win}")
    
    # Play button click function
    if main.mouse_button == 1 and main.button1 and main.transition_time == 0:
        main.next_state = "main menu"
        main.transition_time = 30 * 7 #7 Seconds
        main.t_time = main.transition_time
        main.loading_bar = 0
        main.bar_direction = -1
    


    render_end_screen(main.display, main.button1, main.whoWon)



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