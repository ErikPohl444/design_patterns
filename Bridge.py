import abc

"""
Decouple the implementation from its abstract class
so that the abstraction can only be loosely coupled to an otherwise independent implementation
"""


class DinnerAbstraction:
    """
    Define the abstraction's interface
    with reference to the implementation.
    """

    def __init__(self, dinner_impl):
        self._dinner_impl = dinner_impl

    def operation(self):
        self._dinner_impl.dinner_operation_impl()


class DinnerImplementor(object, metaclass=abc.ABCMeta):
    """
    This is the decoupled implementation
    with primitive methods which match to the higher
    level abstraction definition only fuzzily.
    """

    @abc.abstractmethod
    def dinner_operation_impl(self):
        pass


class DinnerConcreteImplementorPizza(DinnerImplementor):
    """
    The implementor is implemented with a concrete implementation
    """

    def dinner_operation_impl(self):
        print("A spinach and walnuts pie is served!")


class DinnerConcreteImplementorSushi(DinnerImplementor):
    """
    The implementor is implemented with a concrete implementation
    """

    def dinner_operation_impl(self):
        print("You get 3 avocado maki, a sweet potato maki, and 2 tamago sushi!")


def main():
    concrete_implementor_pizza = DinnerConcreteImplementorPizza()
    abstraction = DinnerAbstraction(concrete_implementor_pizza)
    abstraction.operation()


if __name__ == "__main__":
    main()
