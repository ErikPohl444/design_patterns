import abc
"""
Created on Dec 11, 2018

@author: Erik Pohl
"""

"""
Create algorithm classes using encapsulation and make their handles
interchangeable. The Strategy Design Pattern lets the client class
-- the Context -- leverage a common handle to address
any of the algorithm classes 
"""


class LunchContext:
    """
    This is the interface which all the clients 
    need to handshake with.
    Reference the strategy algorithm class here.
    """

    def __init__(self, lunch_strategy):
        self._lunch_strategy = lunch_strategy

    def lunch_context_interface(self):
        self._lunch_strategy.lunch_algorithm_interface()


class LunchStrategy(metaclass=abc.ABCMeta):
    """
    This interface is the contract for all strategy algorithms. 
    The context uses this interface as a model to 
    call the concrete strategies [algorithms] defined below
    """

    @abc.abstractmethod
    def lunch_algorithm_interface(self):
        pass


class EatAtDeskConcreteStrategy(LunchStrategy):
    """
    Implement the eat at desk strategy using the Strategy interface.
    """

    def lunch_algorithm_interface(self):
        print("zap! you heated it in the microwave and ate it at your desk")


class JoinFriendsAtRestaurantConcreteStrategy(LunchStrategy):
    """
    Implement the join friends at restaurant strategy using the Strategy interface.
    """

    def lunch_algorithm_interface(self):
        print("you went out with friends and ate at a restaurant")


class GoToCafeteriaConcreteStrategy(LunchStrategy):
    """
    Implement the go to cafeteria strategy using the Strategy interface.
    """

    def lunch_algorithm_interface(self):
        print("a quiet hour at the cafeteria")


def main():
    caf_concrete_strategy = GoToCafeteriaConcreteStrategy()
    join_concrete_strategy = JoinFriendsAtRestaurantConcreteStrategy()
    zap_concrete_strategy = EatAtDeskConcreteStrategy()
    context = LunchContext(caf_concrete_strategy)
    context.lunch_context_interface()
    context = LunchContext(join_concrete_strategy)
    context.lunch_context_interface()
    context = LunchContext(zap_concrete_strategy)
    context.lunch_context_interface()


if __name__ == "__main__":
    main()
