from pygame import *


class UNIT:
    def __init__(self, size: tuple, side: int, tp: str, coord: tuple, img: str):
        self.coord = coord
        self.size = size
        self.side = side
        self.name = f'{tp}{side}'
        self.img = image.load('images/' + img)
        self.img = [self.img, transform.rotate(self.img,90)]
        self.rotate = 0
        self.hitbox = self.img[0].get_rect(topleft=(self.coord[0]*70,self.coord[1]*70))
        self.drag = False

    def checkClick(self, click):
        # Rotate on right click
        if click.button == 3 and self.drag:
            self.size = (self.size[1], self.size[0])
            self.rotate = 1-self.rotate

        elif click.button == 1:
            if self.drag:
                available = True
                for i in range(self.size[0]):
                    for j in range(self.size[1]):
                        if GRIDS[self.side][j+self.draw()[1]][i+self.draw()[0]] != self and GRIDS[self.side][j+self.draw()[1]][i+self.draw()[0]] is not None:
                            available = False
                if available:
                    self.place(self.draw())
                    return None
                else:
                    return self

            elif self.hitbox.collidepoint(click.pos):
                self.pickup()
                return self

    def draw(self):
        if self.drag:
            x, y = mouse.get_pos()
            x //= 70
            y //= 70

            if x + self.size[0] > 9:
                x = 10 - self.size[0]
            if y + self.size[1] > 9:
                y = 10 - self.size[1]

            for i in range(self.size[0]):
                for j in range(self.size[1]):
                    win.blit(text.render(self.name, True, (255, 255, 255)), ((x + i) * 70 + 10, (y + j) * 70 + 10))
            win.blit(self.img[self.rotate], (x * 70, y * 70))

            return x, y

        else:
            win.blit(self.img[self.rotate], (self.coord[0] * 70, self.coord[1] * 70))

    def place(self, coord):
        self.coord = coord
        self.hitbox = self.img[self.rotate].get_rect(topleft=(self.coord[0]*70, self.coord[1]*70))
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                GRIDS[self.side][j + self.coord[1]][i + self.coord[0]] = self
        self.drag = False

    def pickup(self):
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                try:
                    GRIDS[self.side][j + self.coord[1]][i + self.coord[0]] = None
                except IndexError:
                    pass
        self.drag = True

    def __str__(self):
        return self.name

    __repr__ = __str__


# Finish Later - War Train - 1x5
class WT(UNIT):
    def __init__(self, side: int):
        UNIT.__init__(self, (1, 5), side, 'wt', (14, 3), 'train.png')


# Platoon - 1x3
class PT(UNIT):
    def __init__(self, side: int):
        UNIT.__init__(self, (1, 3), side, 'pt', (13, 0), 'platoon.png')


class AT(UNIT):
    def __init__(self, side: int):
        UNIT.__init__(self, (1, 3), side, 'at', (12, 0), 'artillery.png')


def drawGrid(grid):
    for i in range(9):
        draw.line(win, (255, 255, 255), ((i + 1) * 70, 0), ((i + 1) * 70, 700), 2)
        draw.line(win, (200, 200, 200), (0, (i + 1) * 70), (700, (i + 1) * 70), 2)
    draw.line(win, (255, 255, 255), (700, 0), (700, 1000), 2)

    for ROW, ITEMS in enumerate(GRIDS[grid]):
        for COL, SHIP in enumerate(ITEMS):
            if SHIP:
                win.blit(text.render(SHIP.name, True, (255, 255, 255)), ((COL + 0.1) * 70, (ROW + 0.1) * 70))


# INITIALIZATION
init()
win = display.set_mode((1000, 700))
# creates two grids, 10 by 10, completely filled with None.
GRIDS = [[[None for i in range(10)] for j in range(10)] for k in range(2)]
text = font.Font('INVASION2000.TTF', 20)

ALL_UNITS = [[PT(0), AT(0)], [PT(1), AT(1)]]

# PLACING PHASE
for player, units in enumerate(ALL_UNITS):
    Dragging = None
    while True:

        win.fill((0, 0, 0))
        drawGrid(player)
        for u in units:
            u.draw()

        Leave = False
        for Event in event.get():
            if Event.type == QUIT:
                quit()
            if Event.type == MOUSEBUTTONUP:
                if Dragging is None:
                    for u in units:
                        Dragging = u.checkClick(Event)
                        if Dragging is not None:
                            break

                else:
                    Dragging = Dragging.checkClick(Event)

            if Event.type == KEYUP:
                if Event.key == K_RETURN:
                    Leave = True
                    break
        if Leave:
            break
        display.update()


# GRID TEST
player = 0
while True:
    win.fill((0, 0, 0))
    drawGrid(player)

    for Event in event.get():
        if Event.type == QUIT:
            quit()
        if Event.type == MOUSEBUTTONUP:
            player = 1 - player
    display.update()
