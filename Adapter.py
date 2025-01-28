import abc

"""
Created on Dec 11, 2018

@author: Erik Pohl
"""


"""
Adapter changes the interface of a class into the interface a client expects.
Adapter adapts the interface so that classes can work together which otherwise
wouldn't.
"""


class LandTarget(metaclass=abc.ABCMeta):
    """
    Define the interface that Client expects based on its domain.
    """

    def __init__(self):
        self._fish_adaptee = FishAdaptee()

    @abc.abstractmethod
    def move_on_land_request(self):
        pass


class LegsSpiraclesAdapter(LandTarget):
    """
    Adopt the Target interface for the interface of Adaptee
    """

    def move_on_land_request(self):
        self._fish_adaptee.move_in_water_specific_request()


class FishAdaptee:
    """
    This interface needs to adapt to work in a different domain
    """

    def move_in_water_specific_request(self):
        print("I can adapt to new environments")


def main():
    adapter = LegsSpiraclesAdapter()
    adapter.move_on_land_request()


if __name__ == "__main__":
    main()
