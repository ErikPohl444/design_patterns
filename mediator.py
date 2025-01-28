import random

"""
I am using mediator to represent a simplified board game version of the Game of Life
This LifeCellGridMediator defines an object that encapsulates how a set of mediated objects interact.
"Mediator promotes loose coupling by keeping objects from referring to
each other explicitly, and it lets you vary their interaction independently."
"""


class LifeCellGridMediator:
    """
    Cooperative behavior is permitted by coordinating Colleague cell objects.
    The mediator knows and maintains all Colleague cell objects.
    """

    def __init__(self):
        print("creating grid mediator")
        self.maxx = 3
        self.maxy = 3
        self.cell = [[0 for _ in range(self.maxx)] for _ in range(self.maxy)]
        self.clock = 0
        for y in range(self.maxy):
            for x in range(self.maxx):
                self.cell[x][y] = Cell(self)

    def clock_tick(self):
        print("clock tick!")
        self.clock += 1
        x = random.randint(0, self.maxx-1)
        y = random.randint(0, self.maxy-1)
        above = 0
        if y > 0:
            abovecell = self.cell[x][y-1]
            above = abovecell.amialive()
        below = 0
        if y < self.maxy-1:
            belowcell = self.cell[x][y+1]
            below = belowcell.amialive()
        left = 0
        if x > 0:
            leftcell = self.cell[x-1][y]
            left = leftcell.amialive()
        right = 0
        if x < self.maxx-1:
            rightcell = self.cell[x+1][y]
            right = rightcell.amialive()

        self.cell[x][y].setstatus(int(above+below+left+right))

    def print_out(self):
        print("clock at ", self.clock, " seconds")
        for y in range(self.maxy):
            line = ""
            for x in range(self.maxx):
                line += str(self.cell[x][y].amialive())
            print(line)


class Cell:
    def __init__(self, mediator):
        self._mediator = mediator
        self.status = random.randint(0, 1)

    def amialive(self):
        return self.status

    def setstatus(self, x):
        self.status = x


def main():
    mediator = LifeCellGridMediator()
    mediator.print_out()
    for i in range(10):
        mediator.clock_tick()
        mediator.print_out()


if __name__ == '__main__':
    main()
