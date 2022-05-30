from pygame import *


class Ship:
    def __init__(self, coord: tuple, size: tuple, side: int):
        self.coord = coord  # Coordinate of top left corner on list (may be bottom left in pygame)
        self.size = size
        self.side = side

        for i in range(self.size[0]):
            for j in range(self.size[1]):
                GRIDS[self.side][i+self.coord[0]][j+self.coord[1]] = self

    def __str__(self):
        return 'SHIP'
    __repr__ = __str__



# INITIALIZATION
init()
win = display.set_mode((1000, 1000))
# creates two grids, 10 by 10, completely filled with None.
GRIDS = [[[None for i in range(10)] for j in range(10)] for k in range(2)]

test = Ship((5,5), (3,4), 0)

for i in GRIDS:
    for j in i:
        print(j)
    print('\n')
