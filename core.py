import numpy
from collections import namedtuple, deque


class ForestGraph:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.size = width * height
        self.graph = numpy.zeros([self.size, self.size], dtype=bool)
        for cell in range(self.size):
            self.graph[cell][cell] = True

    def check_accessible(self, src_x: int, src_y: int, dest_x: int, dest_y: int) -> bool:
        row_allowed = -1 < dest_x < self.width
        column_allowed = -1 < dest_y < self.height
        if all([row_allowed, column_allowed]):
            accessed = numpy.zeros([self.size, 1])
            queue = deque([])
            src = self.rowcol_2_index(src_y, src_x)
            dest = self.rowcol_2_index(dest_y, dest_x)
            accessible = False
            queue.append(src)
            while True:
                try:
                    current = queue.popleft()
                except IndexError:
                    break
                else:
                    if not accessed[current]:
                        accessed[current] = True
                        for possible_dest, is_possible in enumerate(self.graph[current][:]):
                            if is_possible:
                                if possible_dest == dest:
                                    accessible = True
                                    break
                                else:
                                    queue.append(possible_dest)
        else:
            accessible = False
        return accessible

    def get_direct_accessible(self, src_x: int, src_y: int) -> list:
        direct_accessibles = []
        if -1 < src_x + 1 < self.width:
            direct_accessibles.append((src_x + 1, src_y))
        if -1 < src_x - 1 < self.width:
            direct_accessibles.append((src_x - 1, src_y))
        if -1 < src_y + 1 < self.height:
            direct_accessibles.append((src_x, src_y + 1))
        if -1 < src_y - 1 < self.height:
            direct_accessibles.append((src_x, src_y - 1))
        return direct_accessibles

    def make_accessible(self, src_x: int, src_y: int, dest_x: int, dest_y: int):
        row_allowed = -1 < dest_x < self.width
        column_allowed = -1 < dest_y < self.height
        if all([row_allowed, column_allowed]):
            src = self.rowcol_2_index(src_y, src_x)
            dest = self.rowcol_2_index(dest_y, dest_x)
            self.graph[src][dest] = True
            self.graph[dest][src] = True

    def clear_accessible(self, src_x: int, src_y: int):
        src = self.rowcol_2_index(src_y, src_x)
        self.graph[src][:] = False
        self.graph[:][src]

    def rowcol_2_index(self, row: int, col: int) -> int:
        return self.width * row + col
