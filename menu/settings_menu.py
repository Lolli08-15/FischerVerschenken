import pygame


settings_menu_background = pygame.image.load("assets\\settings menu.png")

settings_font = pygame.font.Font("assets\\impact.ttf", 64)
exit_button_font = pygame.font.Font("assets\\impact.ttf", 32)

fish_preset_0 = pygame.image.load("assets\\fish preset 0.png")
fish_preset_1 = pygame.image.load("assets\\fish preset 1.png")
fish_preset_2 = pygame.image.load("assets\\fish preset 2.png")
fish_preset_3 = pygame.image.load("assets\\fish preset 3.png")
fish_preset_4 = pygame.image.load("assets\\fish preset 4.png")
fish_preset_5 = pygame.image.load("assets\\fish preset 5.png")
fish_preset_6 = pygame.image.load("assets\\fish preset 6.png")

def settings_menu(main):
    # Exit button
    if main.is_in_rect(main.mouse_pos, (20, 30), (90, 40)):
        main.button1 = True
    else:
        main.button1 = False
    
    # Exit button click function
    if main.mouse_button == 1 and main.button1 and main.transition_time == 0:
        main.next_state = "main menu"
        main.transition_time = 30 * 3 #3 Seconds
        main.t_time = main.transition_time
        main.loading_bar = 0
        main.bar_direction = 0

    # AI button
    if main.is_in_rect(main.mouse_pos, (420, 360), (644, 79)):
        main.button2 = True
    else:
        main.button2 = False
    
    # AI button click function
    if main.mouse_button == 1 and main.button2 and main.transition_time == 0:
        main.selected_ai += 1
        if main.selected_ai > 5:
            main.selected_ai = 0
    

    # Fish button
    if main.is_in_rect(main.mouse_pos, (420, 480), (644, 79)):
        main.button3 = True
    else:
        main.button3 = False
    
    # Fish button click function
    if main.mouse_button == 1 and main.button3 and main.transition_time == 0:
        main.fish_preset += 1
        if main.fish_preset > 6:
            main.fish_preset = 0


    render_settings(main.display, main.button1, main.button2, main.button3, main.selected_ai, main.fish_preset)


def render_settings(display, button1, button2, button3, selected_ai, fish_preset):
    display.blit(settings_menu_background, (0, 0))
    
    # Exit button 110, 40
    text_color = "#b86145"
    if button1: text_color = "#ffb9b9"
    text_texture = exit_button_font.render("Zürich", True, text_color)
    display.blit(
        text_texture,
        (
            20,
            30
        )
    )

    # AI Button
    text = "Ki: Dummheit Persönlich"
    text_color = "#397927"
    if selected_ai == 1:
        text = "Ki: Chad GPT"
        text_color = "#a6b235"
    if selected_ai == 2:
        text = "Ki: Medium"
        text_color = "#efd035"
    if selected_ai == 3:
        text = "Ki: AIQ"
        text_color = "#ea541a"
    if selected_ai == 4:
        text = "Ki: Hart wie Hartmut"
        text_color = "#ea1a1a"
    if selected_ai == 5:
        text = "Ki: Unmöglich"
        text_color = "#000000"

    if button2: text_color = "#a1e9e9"
    text_texture = settings_font.render(text, True, text_color)
    display.blit(
        text_texture,
        (
            420,
            360
        )
    )

    # FISH Button
    text = "Fish: Normen"
    text_color = "#67b1d7"
    if fish_preset == 1:
        text = "Fish: Quickie"
    if fish_preset == 2:
        text = "Fish: Long John"
    if fish_preset == 3:
        text = "Fish: Double Trouble"
    if fish_preset == 4:
        text = "Fish: Roberts Dreier"
    if fish_preset == 5:
        text = "Fish: Das Große Fechten"
    if fish_preset == 6:
        text = "Fish: Aal die Fische"

    if button3: text_color = "#a1e9e9"
    text_texture = settings_font.render(text, True, text_color)
    display.blit(
        text_texture,
        (
            420,
            480
        )
    )


    # Show preview for fishes used in selected fish preset
    fish_preset_texture = fish_preset_0
    if fish_preset == 1: fish_preset_texture = fish_preset_1
    if fish_preset == 2: fish_preset_texture = fish_preset_2
    if fish_preset == 3: fish_preset_texture = fish_preset_3
    if fish_preset == 4: fish_preset_texture = fish_preset_4
    if fish_preset == 5: fish_preset_texture = fish_preset_5
    if fish_preset == 6: fish_preset_texture = fish_preset_6
    display.blit(fish_preset_texture, (420, 570))