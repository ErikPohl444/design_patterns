from abc import ABCMeta, abstractmethod


class Chair(object):
    def __init__(self, legs=3, material='Wood', color='Oak'):
        self.legs = legs
        self.material = material
        self.color = color

    def __str__(self):
        return "This is a {0} chair with {1} legs made out of {2}.".format(
            self.color, self.legs, self.material
        )


class Table(object):
    def __init__(self, legs=4, material='Plastic', color='Black'):
        self.legs = legs
        self.material = material
        self.color = color

    def __str__(self):
        return "This is a {0} table with {1} legs made out of {2}.".format(
            self.color, self.legs, self.material
        )


class Builder:
    __metaclass__ = ABCMeta

    @abstractmethod
    def set_legs(self, value):
        pass

    @abstractmethod
    def set_material(self, value):
        pass

    @abstractmethod
    def set_color(self, value):
        pass

    @abstractmethod
    def get_result(self):
        pass


class TableBuilder(Builder):
    def __init__(self):
        self.table = Table()

    def set_legs(self, value):
        self.table.legs = value
        return self

    def set_material(self, value):
        self.table.material = value
        return self

    def set_color(self, value):
        self.table.color = value
        return self

    def get_result(self):
        return self.table


class ChairBuilder(Builder):
    def __init__(self):
        self.chair = Chair()

    def set_legs(self, value):
        self.chair.legs = value
        return self

    def set_material(self, value):
        self.chair.material = value
        return self

    def set_color(self, value):
        self.chair.color = value
        return self

    def get_result(self):
        return self.chair


class TableBuilderDirector(object):
    @staticmethod
    def construct():
        return TableBuilder().set_legs(8).set_material('Metal').set_color("Silver").get_result()


class ChairBuilderDirector(object):
    @staticmethod
    def construct():
        return ChairBuilder().set_legs(3).set_material('Canvas').set_color("Tan").get_result()


chair = ChairBuilderDirector.construct()
print(chair)
table = TableBuilderDirector.construct()
print(table)
