import settings
import pygame


end_screen_p_background = pygame.image.load("assets\\end screen player.png")
end_screen_ai_background = pygame.image.load("assets\\end screen ai.png")
end_screen_test_background = pygame.image.load("assets\\end screen testing.png")

main_menu_font = pygame.font.Font("assets\\impact.ttf", 64)
result_font = pygame.font.Font("assets\\impact.ttf", 50)


def end_menu(main):
    # Exit button
    if main.is_in_rect(main.mouse_pos, (269, 138), (149, 79)):
        main.button1 = True
    else:
        main.button1 = False

    # AI testing
    if main.ai_mode:
        if main.transition_time == 0:
            main.button1 = True
            main.mouse_button = 1
            if main.whoWon == "player":
                main.player_win += 1
                main.player_turns += main.current_turns
            else:
                main.ai_win += 1
                main.ai_turns += main.current_turns
            main.current_turns = 0

    # Exit button click function
    if main.mouse_button == 1 and main.button1 and main.transition_time == 0:
        if not main.ai_mode:
            main.pick_splash()
        main.next_state = "main menu"
        main.transition_time = 30 * 7 #7 Seconds
        main.t_time = main.transition_time
        main.loading_bar = 0
        main.bar_direction = -1


    if not main.ai_mode:
        render_end_screen(main.display, main.button1, main.whoWon)
    

    if main.whoWon == "ai testing":
        players_text = " vs. "
        vs_text_texture = result_font.render(players_text, True, "#bbecf3")
        main.display.blit(
            vs_text_texture,
            (
                780 - vs_text_texture.get_width() / 2,
                350
            )
        )
        players_text = settings.get_ai_name(main.selected_ai[0])
        text_texture = result_font.render(players_text, True, "#bbecf3")
        main.display.blit(
            text_texture,
            (
                780 - vs_text_texture.get_width() / 2 - text_texture.get_width(),
                350
            )
        )
        players_text = settings.get_ai_name(main.selected_player[0])
        text_texture = result_font.render(players_text, True, "#bbecf3")
        main.display.blit(
            text_texture,
            (
                780 + vs_text_texture.get_width() / 2,
                350
            )
        )


        text_texture = result_font.render(f"Spiele: {main.ai_win + main.player_win}", True, "#bbecf3")
        main.display.blit(
            text_texture,
            (
                780 - text_texture.get_width() / 2,
                450
            )
        )
        text_texture = result_font.render(f"{main.ai_win} | {main.player_win}", True, "#bbecf3")
        main.display.blit(
            text_texture,
            (
                780 - text_texture.get_width() / 2,
                520
            )
        )

        if main.ai_win > 0:
            ai_avg_turns = main.ai_turns / main.ai_win
        else:
            ai_avg_turns = 0
        if main.player_win > 0:
            player_avg_turns = main.player_turns / main.player_win
        else:
            player_avg_turns = 0
        
        text_texture = result_font.render("Durchschnitt Schüsse/Sieg", True, "#bbecf3")
        main.display.blit(
            text_texture,
            (
                780 - text_texture.get_width() / 2,
                640
            )
        )
        text_texture = result_font.render(f"{ai_avg_turns:.2f} | {player_avg_turns:.2f}", True, "#bbecf3")
        main.display.blit(
            text_texture,
            (
                780 - text_texture.get_width() / 2,
                700
            )
        )



def render_end_screen(display, button1, whoWon):
    if whoWon == "player":
        display.blit(end_screen_p_background, (0, 0))
    elif whoWon == "ai testing":
        display.blit(end_screen_test_background, (0, 0))
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