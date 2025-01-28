import abc
"""
Created on Dec 11, 2018

@author: Erik Pohl
"""

"""
The composite creates a recursive tree structure of 
leaf and composite components.
Each type of component is treated uniformly
whether it is a leaf or a composite.
"""


class PaintedDollComponent(metaclass=abc.ABCMeta):
    """
    This is the interface for component objects
    whether they are leaf or composite.
    Default behavior can be implemented here.
    There's an interface to handle child objects.
    You can also create an interface for parent objects,
    but that is not part of this design.
    """

    @abc.abstractmethod
    def operation(self):
        pass


class FilledMatryoshkaDollComposite(PaintedDollComponent):
    """
    This sets the behavior for components having children
    and records child components.
    """

    def __init__(self, name):
        self._children = set()
        self.name = name

    def operation(self):
        print("My name is " + self.name + " and I am a composite")
        for child in self._children:
            child.operation()

    def add(self, component):
        self._children.add(component)

    def remove(self, component):
        self._children.discard(component)


class EmptyMatryoshkaDollComposite(PaintedDollComponent):
    """
    This is a leaf -- no children.
    It defines the behavior of leaf components.
    """

    def operation(self):
        print("My name is " + self.name + " and I don't have any dolls inside me")
        
    def __init__(self, name):
        self.name = name


def main():
    sasha_leaf = EmptyMatryoshkaDollComposite("Sasha")
    natasha_composite = FilledMatryoshkaDollComposite("Natasha")
    natasha_composite.add(sasha_leaf)
    tanya_composite = FilledMatryoshkaDollComposite("Tanya")
    natasha_composite.add(tanya_composite)
    misha_leaf = EmptyMatryoshkaDollComposite("Misha")
    anichka_leaf = EmptyMatryoshkaDollComposite("Anichka")
    tanya_composite.add(anichka_leaf)
    tanya_composite.add(misha_leaf)
    natasha_composite.operation()


if __name__ == "__main__":
    main()
