import random

"""
I am using mediator to represent a simplified board game version of the Game of Life
This LifeCellGridMediator defines an object that encapsulates how a set of mediated objects interact.
"Mediator promotes loose coupling by keeping objects from referring to
each other explicitly, and it lets you vary their interaction independently."
"""


class Cell:
    def __init__(self):
        self.status = random.randint(0, 1)

    def am_i_alive(self):
        return self.status

    def set_status(self, x):
        self.status = x


class LifeCellGridMediator:
    """
    Cooperative behavior is permitted by coordinating Colleague cell objects.
    The mediator knows and maintains all Colleague cell objects.
    """

    def __init__(self, xbound, ybound):
        print("creating grid mediator")
        self.maxx = xbound
        self.maxy = ybound
        self.cells = [[Cell() for _ in range(self.maxx)] for _ in range(self.maxy)]
        self.clock = 0

    def clock_tick(self):
        print("clock tick!")
        self.clock += 1
        x = random.randint(0, self.maxx-1)
        y = random.randint(0, self.maxy-1)
        above = 0
        if y > 0:
            above = self.cells[x][y - 1].am_i_alive()
        below = 0
        if y < self.maxy-1:
            below = self.cells[x][y + 1].am_i_alive()
        left = 0
        if x > 0:
            left = self.cells[x - 1][y].am_i_alive()
        right = 0
        if x < self.maxx-1:
            right = self.cells[x + 1][y].am_i_alive()

        self.cells[x][y].set_status(int(above + below + left + right))

    def print_out(self):
        print("clock at ", self.clock, " seconds")
        for y in range(self.maxy):
            line = ""
            for x in range(self.maxx):
                line += str(self.cells[x][y].am_i_alive())
            print(line)


def main():
    mediator = LifeCellGridMediator(3, 3)
    mediator.print_out()
    for i in range(10):
        mediator.clock_tick()
        mediator.print_out()


if __name__ == '__main__':
    main()
