import abc
"""
Created on Dec 11, 2018

@author: Erik Pohl
"""


"""
With the flyweight, a factor method uses a shared pool to create large numbers of fine-grained objects
efficiently in memory
"""


class DowelFlyweightFactory:
    """
    Create and manage Dowel flyweight objects.
    Ensure that flyweights are shared properly without creating duplicates. 
    This means when a new dowel is requested, it either creates one
    if it doesn't exist or provides an already created one if the one 
    requested is a match
    """

    def __init__(self):
        self._flyweights = {}

    def get_flyweight(self, key):
        try:
            flyweight = self._flyweights[key]
        except KeyError:
            flyweight = DowelConcreteFlyweight(key)
            self._flyweights[key] = flyweight
        return flyweight


class DowelFlyweight(metaclass=abc.ABCMeta):
    """
    Here is an interface via which a flyweight can act on an 
    extrinsic state
    """

    def __init__(self, name):
        print("creating new dowel for " + name)
        self.intrinsic_state = name

    @abc.abstractmethod
    def operation(self, extrinsic_state):
        pass


class DowelConcreteFlyweight(DowelFlyweight):
    """
    The flyweight interface is implemented here
    with storage for the intrinsic state.
    A ConcreteFlyweight object must be sharable. Any
    state it stores must be intrinsic; that is, it must be independent
    of the ConcreteFlyweight object's context.
    """

    def operation(self, extrinsic_state):
        print(self.intrinsic_state + ' ' + extrinsic_state)


def main():
    flyweight_factory = DowelFlyweightFactory()
    concrete_flyweight = flyweight_factory.get_flyweight("first_slot_dowel")
    concrete_flyweight.operation('Inserted')
    concrete_flyweight = flyweight_factory.get_flyweight("second_slot_dowel")
    concrete_flyweight.operation('Hammered in')
    concrete_flyweight = flyweight_factory.get_flyweight("first_slot_dowel")
    concrete_flyweight.operation('Fitted')


if __name__ == "__main__":
    main()
