from core import ForestGraph
import numpy


class Forest:
    def __init__(self, width: int, height: int):
        self.width, self.height = width, height
        self.graph = ForestGraph(width, height)
        self.position = [0, 0]
        self.approachables = self.graph.get_direct_accessible(0, 0)

    def go_to(self, x: int, y: int):
        if self.graph.check_accessible(self.position[0], self.position[1], x, y):
            self.position = [x, y]
            self.approachables = self.graph.get_direct_accessible(x, y)
            print(f"Walked past. You're now at Cell({x}, {y})")
        elif (x, y) in self.approachables:
            # If successfullly opened the tile
            self.graph.make_accessible(
                self.position[0], self.position[1], x, y)
            self.position = [x, y]
            self.approachables = self.graph.get_direct_accessible(x, y)
            print(f"Opened. You're now at Cell({x}, {y})")
        else:
            print(f"You can't go to Cell({x}, {y})")
