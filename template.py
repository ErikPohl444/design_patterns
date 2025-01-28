import abc
"""
Created on Dec 10, 2018

@author:  Erik Pohl
"""


"""
The template design pattern defines a generalized
algorithm, asking the subclasses to fill in some 
of the steps.  The algorithm stays the same
for all subclasses, but the subclasses redefine 
some steps.
"""


class HungryAnimalAbstractClass(metaclass=abc.ABCMeta):
    """
    Define a abstract primitive operations for a Hungry animal
    Concrete hungry animal subclasses complete the definition
    with concrete operation steps.
    The template method calls abstract methods which will be
    expressed by the subclasses.
    """

    def eat_dinner(self):
        self._express_hunger()
        self._find_food()
        self._eat()

    @abc.abstractmethod
    def _express_hunger(self):
        pass

    @abc.abstractmethod
    def _find_food(self):
        pass

    @abc.abstractmethod
    def _eat(self):
        pass


class HungryHogConcreteClass(HungryAnimalAbstractClass):
    """
    Implement the primitive Hungry Animal operations to carry out
    steps specific to the concrete actions of a Hungry Hog
    """

    def _express_hunger(self):
        print("Oink oink! ")
        
    def _find_food(self):
        print("Go to trough ")

    def _eat(self):
        print("Submerge face in food trough")


class HungryLionConcreteClass(HungryAnimalAbstractClass):
    """
    Implement the primitive Hungry Animal operations to carry out
    steps specific to the concrete actions of a Hungry Lion
    """

    def _express_hunger(self):
        print("RRRRrrrroarrr! ")
        
    def _find_food(self):
        print("Hunt")

    def _eat(self):
        print("Gnaw fresh prey")


def main():
    first_concrete_class = HungryHogConcreteClass()
    first_concrete_class.eat_dinner()
    
    second_concrete_class = HungryLionConcreteClass()
    second_concrete_class.eat_dinner()


if __name__ == "__main__":
    main()
