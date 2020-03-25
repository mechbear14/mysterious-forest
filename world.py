from core import ForestGraph
from player import Player
from blocks import Block, NormalBlock, PassBlock
from pygame import Surface


class Forest:
    def __init__(self, width: int, height: int, player_info: Player):
        self.width, self.height = width, height
        self.graph = ForestGraph(width, height)
        self.player = player_info
        px, py = self.player.position.x, self.player.position.y
        self.approachables = self.graph.get_direct_accessible(px, py)
        self.blocks = []
        for block_index in range(width * height):
            y, x = divmod(block_index, width)
            block = PassBlock(
                x, y) if x == px and y == py else NormalBlock(x, y)
            self.blocks.append(block)
            block.on_create(self)

    def get_player(self) -> Player:
        return self.player

    def go_to(self, x: int, y: int):
        prev_block = self.blocks[self.xy_2_index(*self.player.position)]
        block = self.blocks[self.xy_2_index(x, y)]
        player_position = self.player.position

        if self.graph.check_accessible(player_position[0], player_position[1], x, y):
            prev_block.on_leave(self)
            block.on_enter(self)
        elif (x, y) in self.approachables:
            if block.state == Block.UNKNOWN:
                prev_block.on_leave(self)
                block.on_reveal(self)
            elif block.state == Block.REVEALED:
                prev_block.on_leave(self)
                block.on_open(self)
            elif block.state == Block.PASSED:
                prev_block.on_leave(self)
                block.on_enter(self)

    def make_accessible(self, x: int, y: int):
        src_x, src_y = self.player.position.x, self.player.position.y
        self.graph.make_accessible(src_x, src_y, x, y)

    def make_inaccessible(self, x: int, y: int):
        self.graph.clear_accessible(x, y)

    def move_player_to(self, x: int, y: int):
        self.player.update_position(x, y)
        self.approachables = self.graph.get_direct_accessible(x, y)

    def render(self, area: Surface):
        for block in self.blocks:
            block.draw(area)

    def xy_2_index(self, x: int, y: int) -> int:
        return int(y * self.width + x)
