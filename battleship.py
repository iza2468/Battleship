from pygame import *


class UNIT:
    def __init__(self, coord: tuple, size: tuple, side: int, type: str):
        self.coord = coord  # Coordinate of top left corner on list (may be bottom left in pygame)
        self.size = size
        self.side = side
        self.name = f'{type}{side}'

    def rotate(self):
        self.size = (self.size[1], self.size[0])
        print(self.size)

    def drawDrag(self, pos):
        x = pos[0]//70
        y = pos[1]//70
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                win.blit(text.render(self.name,True,(255,255,255)),((x+i)*70 + 10,(y+j)*70 + 10))

    def place(self):
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                GRIDS[self.side][j + self.coord[1]][i + self.coord[0]] = self

    def __str__(self):
        return self.name

    __repr__ = __str__

    def ability(self):
        return None


class WT(UNIT):
    def __init__(self, coord: tuple, side: int):
        UNIT.__init__(self, coord, (1, 5), side, 'wt')


def drawGrid(grid):
    for i in range(9):
        draw.line(win, (255, 255, 255), ((i + 1) * 70, 0), ((i + 1) * 70, 700), 2)
        draw.line(win, (200, 200, 200), (0, (i + 1) * 70), (700, (i + 1) * 70), 2)
    draw.line(win, (255, 255, 255), (700, 0), (700, 1000), 2)

# INITIALIZATION
init()
win = display.set_mode((1000, 700))
# creates two grids, 10 by 10, completely filled with None.
GRIDS = [[[None for i in range(10)] for j in range(10)] for k in range(2)]
text = font.Font('INVASION2000.TTF', 20)

ships = [WT((1, 5), 0), WT((3, 3), 1)]


# PLACING PHASE
for i in range(2):
    while True:
        win.fill((0,0,0))
        drawGrid(i)
        ships[i].drawDrag(mouse.get_pos())
        for Event in event.get():
            if Event.type == QUIT:
                quit()
        display.update()



for i in GRIDS:
    for j in i:
        print(j)
    print('\n')

# GRID TEST
player = 0
while True:
    win.fill((0,0,0))


    #DRAW GRID
    for ROW, ITEMS in enumerate(GRIDS[player]):
        for COL, SHIP in enumerate(ITEMS):
            if SHIP:
                win.blit(text.render(SHIP.name, True, (255,255,255)), ((COL+0.1)*70, (ROW+0.1)*70))

    for Event in event.get():
        if Event.type == QUIT:
            quit()
        if Event.type == MOUSEBUTTONUP:
            player = 1-player
            print(player)
    display.update()
