import pygame

fish_l1 = pygame.image.load("assets\\fish l1.png")
fish_l2 = pygame.image.load("assets\\fish l2.png")
fish_l3 = pygame.image.load("assets\\fish l3.png")
fish_l4 = pygame.image.load("assets\\fish l4.png")
fish_l5 = pygame.image.load("assets\\fish l5.png")
fish_l6 = pygame.image.load("assets\\fish l6.png")

def render_fish(display, offsetX, offsetY, fish_list, preview):
    for fish in fish_list:
        fish_texture = fish_l2
        if fish.length == 1: fish_texture = fish_l1
        if fish.length == 2: fish_texture = fish_l2
        if fish.length == 3: fish_texture = fish_l3
        if fish.length == 4: fish_texture = fish_l4
        if fish.length == 5: fish_texture = fish_l5
        if fish.length == 6: fish_texture = fish_l6
        if preview:
            fish_texture.set_alpha(120)
        else:
            fish_texture.set_alpha(255)

        if fish.direction == 0:
            fish_texture = pygame.transform.rotate(fish_texture, 90)
            position = (fish.posXY[0] * 50 + offsetX, (fish.posXY[1] - fish.length + 1) * 50 + offsetY)

            if fish.length == 1: position = (position[0], position[1] - 50)
            if fish.length == 6: position = (position[0], position[1] + 150)

            display.blit(fish_texture, position)
        if fish.direction == 1:
            position = (fish.posXY[0] * 50 + offsetX, fish.posXY[1] * 50 + offsetY)
            display.blit(fish_texture, position)
        if fish.direction == 2:
            fish_texture = pygame.transform.rotate(fish_texture, -90)
            position = (fish.posXY[0] * 50 + offsetX, fish.posXY[1] * 50 + offsetY)

            if fish.length == 1: position = (position[0] - 50, position[1])
            if fish.length == 6: position = (position[0] - 50, position[1])

            display.blit(fish_texture, position)
        if fish.direction == 3:
            fish_texture = pygame.transform.flip(fish_texture, True, False)
            position = ((fish.posXY[0] - fish.length + 1) * 50 + offsetX, fish.posXY[1] * 50 + offsetY)

            if fish.length == 1:
                position = (position[0] - 50, position[1] - 50)
                fish_texture = pygame.transform.flip(fish_texture, False, True)
            if fish.length == 6:
                position = (position[0] + 150, position[1] - 50)
                fish_texture = pygame.transform.flip(fish_texture, False, True)

            display.blit(fish_texture, position)