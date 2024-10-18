import pygame


main_menu_background = pygame.image.load("assets\\main menu.png")
placing_menu_background = pygame.image.load("assets\\placing menu.png")

fish_l2 = pygame.image.load("assets\\fish l2.png")
fish_l3 = pygame.image.load("assets\\fish l3.png")
fish_l4 = pygame.image.load("assets\\fish l4.png")
fish_l5 = pygame.image.load("assets\\fish l5.png")

main_menu_font = pygame.font.Font("assets\\impact.ttf", 64)
exit_button_font = pygame.font.Font("assets\\impact.ttf", 32)
fish_count_font = pygame.font.Font("assets\\impact.ttf", 50)


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


def render_placing_menu(display, field_x, field_y, fish_left, selected):
    display.blit(placing_menu_background, (0, 0))
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


def render_fish(display, offsetX, offsetY, fish_list, preview):
    for fish in fish_list:
        fish_texture = fish_l2
        if fish.length == 2: fish_texture = fish_l2
        if fish.length == 3: fish_texture = fish_l3
        if fish.length == 4: fish_texture = fish_l4
        if fish.length == 5: fish_texture = fish_l5
        if preview:
            fish_texture.set_alpha(150)
        else:
            fish_texture.set_alpha(255)

        if fish.direction == 0:
            fish_texture = pygame.transform.rotate(fish_texture, 90)
            position = (fish.posX * 50 + offsetX, (fish.posY - fish.length + 1) * 50 + offsetY)
            display.blit(fish_texture, position)
        if fish.direction == 1:
            position = (fish.posX * 50 + offsetX, fish.posY * 50 + offsetY)
            display.blit(fish_texture, position)
        if fish.direction == 2:
            fish_texture = pygame.transform.rotate(fish_texture, -90)
            position = (fish.posX * 50 + offsetX, fish.posY * 50 + offsetY)
            display.blit(fish_texture, position)
        if fish.direction == 3:
            fish_texture = pygame.transform.flip(fish_texture, True, False)
            position = ((fish.posX - fish.length + 1) * 50 + offsetX, fish.posY * 50 + offsetY)
            display.blit(fish_texture, position)


def transition(display, transition_time, loading_bar):
    if transition_time > 180:
        overlay = pygame.Surface((1600, 900))
        overlay.set_alpha(255 / 30 * (30 - (transition_time - 180)))
        overlay.fill((15, 48, 66))

        display.blit(overlay, (0, 0))
    else:
        display.fill((15, 48, 66))

        pygame.draw.rect(
            display, "#aecfe3",
            pygame.Rect(800 - 300, 450 - 20, 600, 40),
            5
        )
        pygame.draw.rect(
            display, "#aecfe3",
            pygame.Rect(800 - 290, 450 - 10,
            1090 / 650 * loading_bar,
            20)
        )