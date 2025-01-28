import abc

"""
Created on Dec 10, 2018

@author: Erik Pohl
"""


"""
Define an object creation interface
, and let subclasses decide
which product object class to instantiate / create. Factory Method lets a class defer
instantiation to subclasses.
"""


class WaterLightSoilCreator(metaclass=abc.ABCMeta):
    """
    Declare a factory method named water light soil creator
    returning a product type object.
    In this case the creator also defines a default implementation of 
    the factory method which returns a default concrete product object.
    Creator may also define a default implementation of the factory
    When you call the factory method, you get a product object.
    """

    def __init__(self):
        self.plant_product = self._factory_method()

    @abc.abstractmethod
    def _factory_method(self):
        pass

    def some_operation(self):
        self.plant_product.interface()


class RoseConcreteCreator(WaterLightSoilCreator):
    """
    Override the water light soil factory method to return an instance of a
    rose
    """

    def _factory_method(self):
        return RoseConcreteProduct()


class CornConcreteCreator(WaterLightSoilCreator):
    """
    Override the factory method to return an instance of an 
    ear of corn
    """

    def _factory_method(self):
        return CornConcreteProduct()


class PlantProduct(metaclass=abc.ABCMeta):
    """
    This is an interface for plant products the factory method creates
    """

    @abc.abstractmethod
    def interface(self):
        pass


class RoseConcreteProduct(PlantProduct):
    """
    Implement a product interface for roses
    """

    def interface(self):
        print("the beautiful rose is growing")


class CornConcreteProduct(PlantProduct):
    """
    Implement a product interface for corn
    """

    def interface(self):
        print("the delicious corn is growing")


def main():
    rose_concrete_creator = RoseConcreteCreator()
    rose_concrete_creator.plant_product.interface()
    rose_concrete_creator.some_operation()
    
    corn_concrete_creator = CornConcreteCreator()
    corn_concrete_creator.plant_product.interface()
    corn_concrete_creator.some_operation()


if __name__ == "__main__":
    main()
