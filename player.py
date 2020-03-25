import pygame
from pygame.sprite import Sprite
from pygame import Vector2, Surface, Rect, Color


class BasePlayer(Sprite):
    NORMAL = 0

    def __init__(self, x: int, y: int):
        self.position = Vector2(x, y)
        self.size = Vector2(50, 50)
        self.canvas_position = Vector2(x * 50, y * 50)
        self.state = Player.NORMAL
        self.image = Surface(self.size).convert_alpha()
        self.rect = Rect(self.canvas_position, self.size)

    def update_position(self, x: int, y: int):
        self.position = Vector2(x, y)
        sx, sy = self.size.x, self.size.y
        self.canvas_position = Vector2(x * sx, y * sy)
        self.rect = Rect(self.canvas_position, self.size)

    def on_create(self):
        pass

    def on_move(self):
        pass

    def draw(self, area: Surface):
        area.blit(self.image, self.rect)


class Player(BasePlayer):
    def __init__(self, x: int, y: int):
        BasePlayer.__init__(self, x, y)
        self.on_create()

    def on_create(self):
        pygame.draw.circle(self.image, Color(255, 128, 0),
                           self.canvas_position + self.size / 2, self.size.x / 2)
