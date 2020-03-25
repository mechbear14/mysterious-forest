import pygame
from pygame.locals import *
from pygame import Vector2

from world import Forest
from player import Player

pygame.init()
screen = pygame.display.set_mode((640, 360))

player = Player(0, 0)
world = Forest(6, 5, player)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            raise SystemExit
        elif event.type == MOUSEBUTTONUP:
            mouse_position = Vector2(pygame.mouse.get_pos())
            x = mouse_position.x // 50
            y = mouse_position.y // 50
            if -1 < x < world.width and -1 < y < world.height:
                world.go_to(x, y)
    screen.fill((0, 0, 0))
    world.render(screen)
    player.draw(screen)
    pygame.display.update()
