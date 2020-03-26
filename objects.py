from pygame import Surface, Vector2, Rect
from pygame.sprite import Sprite
from components import Message
from core import ForestGraph


class Block(Sprite):
    SIZE = Vector2(50, 50)
    UNKNOWN = 0
    REVEALED = 1
    PASSED = 2

    def __init__(self, x: int, y: int):
        Sprite.__init__(self)
        self.location = (x, y)
        self.canvas_location = Vector2(x * Block.SIZE.x, y * Block.SIZE.y)
        self.costumes = []
        self.image = Surface(Block.SIZE).convert_alpha()
        self.rect = Rect(self.canvas_location, Block.SIZE)
        self.state = Block.UNKNOWN

    def on_reveal(self):
        pass

    def on_open(self):
        pass

    def on_pass(self):
        pass

    def on_leave(self):
        pass

    def on_receive(self, message: Message):
        pass


class Forest:
    def __init__(self, width: int, height: int, blocks: list):
        self.width, self.height = width, height
        self.graph = ForestGraph(width, height)
        self.blocks = blocks
        if not len(blocks) == width * height:
            raise IndexError("Inconsistent number of blocks with forest size")
        self.canvas = Surface(width * Block.SIZE.x,
                              height * Block.SIZE.y).convert_alpha()

    def on_reset(self):
        pass

    def on_receive(self, message: Message):
        pass

    def render(self, area: Surface):
        area.blit(self.canvas)


class Player(Sprite):
    def __init__(self, x: int, y: int):
        Sprite.__init__(self)
        self.location = (x, y)
        self.canvas_location = Vector2(x * Block.SIZE.x, y * Block.SIZE.y)
        self.costumes = []
        self.image = Surface(Block.SIZE).convert_alpha()
        self.rect = Rect(self.canvas_location, Block.SIZE)

    def on_move(self):
        pass

    def on_walk(self):
        pass

    def on_receive(self, message: Message):
        pass
