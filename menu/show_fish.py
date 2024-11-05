import pygame

fish_l2 = pygame.image.load("assets\\fish l2.png")
fish_l3 = pygame.image.load("assets\\fish l3.png")
fish_l4 = pygame.image.load("assets\\fish l4.png")
fish_l5 = pygame.image.load("assets\\fish l5.png")

def render_fish(display, offsetX, offsetY, fish_list, preview):
    for fish in fish_list:
        fish_texture = fish_l2
        if fish.length == 2: fish_texture = fish_l2
        if fish.length == 3: fish_texture = fish_l3
        if fish.length == 4: fish_texture = fish_l4
        if fish.length == 5: fish_texture = fish_l5
        if preview:
            fish_texture.set_alpha(20)
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