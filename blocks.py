from player import Player
from world import Forest

import pygame
from pygame.locals import *
from pygame.sprite import Sprite
from pygame import Vector2, Rect, Surface
from random import randint


class Block(Sprite):
    UNKNOWN = 0
    REVEALED = 1
    PASSED = 2

    def __init__(self, x: int, y: int):
        Sprite.__init__(self)
        self.position = Vector2(x, y)
        self.size = Vector2(50, 50)
        self.canvas_position = Vector2(50 * x, 50 * y)
        self.image = Surface(self.size).convert_alpha()
        self.rect = Rect(self.canvas_position, self.size)
        self.state = Block.UNKNOWN

    def on_create(self, forest):
        pass

    def on_reveal(self, forest):
        pass

    def on_open(self, forest):
        pass

    def on_enter(self, forest):
        pass

    def on_leave(self, forest):
        pass

    def set_state(self, state):
        self.state = state

    def draw(self, area: Surface):
        area.blit(self.image, self.rect)


class PassBlock(Block):
    def __init__(self, x: int, y: int):
        Block.__init__(self, x, y)
        self.primaryColour = Color(0, 0, 0, 0)
        self.state = Block.PASSED

    def on_create(self, forest):
        pygame.draw.rect(self.image,  self.primaryColour, Rect(
            Vector2(2, 2), self.size - Vector2(4, 4)))

    def on_enter(self, forest):
        x, y = self.position.x, self.position.y
        forest.move_player_to(self.position.x, self.position.y)
        print(f"You've entered block ({x}, {y})")

    def on_leave(self, forest):
        x, y = self.position.x, self.position.y
        print(f"You've left block ({x}, {y})")


class NormalBlock(Block):
    def __init__(self, x: int, y: int):
        Block.__init__(self, x, y)
        self.primaryColour = Color(128, 128, 128)
        self.revealColour = Color(255, 200, 0)

    def on_create(self, forest):
        pygame.draw.rect(self.image,  self.primaryColour, Rect(
            Vector2(2, 2), self.size - Vector2(4, 4)))

    def on_reveal(self, forest):
        x, y = self.position.x, self.position.y
        pygame.draw.rect(self.image,  self.revealColour, Rect(
            Vector2(2, 2), self.size - Vector2(4, 4)))
        print(f"You've revealed block ({x}, {y})")
        self.state = Block.REVEALED

    def on_open(self, forest):
        x, y = self.position.x, self.position.y
        print(f"You've opened block ({x}, {y})")
        a, b = randint(0, 100), randint(0, 100)
        answer = input(f"Here's a question: what is {a} + {b}?")
        if int(answer) == a + b:
            pygame.draw.rect(self.image, Color(0, 0, 0, 0), Rect(
                Vector2(0, 0), self.size))
            print(f"Good. You can now pass block ({x}, {y})")
            self.state = Block.PASSED
            forest.make_accessible(x, y)
            forest.move_player_to(self.position.x, self.position.y)
        else:
            print("Roar! You can't pass")

    def on_leave(self, forest):
        x, y = self.position.x, self.position.y
        print(f"You've left block ({x}, {y})")

    def on_enter(self, forest):
        x, y = self.position.x, self.position.y
        forest.move_player_to(self.position.x, self.position.y)
        print(f"You've entered block ({x}, {y})")
