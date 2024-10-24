import pygame
import random
import settings


exit_button_font = pygame.font.Font("assets\\impact.ttf", 32)




def transition(main):
    main.transition_time -= 1

    # Skip
    if settings.ai_mode: main.transition_time = 0
    if main.key == " ": main.transition_time = 0

    if main.transition_time < (main.t_time-30): # Speedup the progress bar
        main.loading_bar += int((random.randrange(1, 30)) / (main.t_time/89))
    
    render_transition(main.display, main.transition_time, main.loading_bar, main.bar_direction,main.t_time)

    if main.transition_time == 0: # Switch to next stage after done
        main.state = main.next_state
        main.next_state = ""


def render_transition(display, transition_time, loading_bar, bar_direction,t_time):
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