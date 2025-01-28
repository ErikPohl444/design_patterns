import abc
"""
This pattern permits an object to alter its behavior when its internal state changes.
The object will appear to change its class.
"""


class TrafficLight:
    """
    This is an interface which can have multiple states.
    Use a ConcreteState subclass to change states.
    """

    def __init__(self, state):
        self._state = state

    def drive(self):
        self._state.handle()

    def check(self):
        print("the light is ", self._state)
        print("the light is ", self._state.output())


class State(metaclass=abc.ABCMeta):
    """
    This interface encapsulates behavior associated with a particular state
    given a context
    """

    @abc.abstractmethod
    def handle(self):
        pass

    @abc.abstractmethod
    def output(self):
        pass


class RedLight(State):
    """
    Implement a behavior associated with red light state
    """

    def handle(self):
        print("You can't drive through a red light.")

    def output(self):
        return "Red"


class GreenLight(State):
    """
    Implement a behavior associated with a a green light state
    """

    def handle(self):
        print("You can keep driving because it is green.")

    def output(self):
        return "Green"


class YellowLight(State):
    """
    Implement a behavior associated with a a green light state
    """

    def handle(self):
        print("You need to calculate very carefully if you can make it through this yellow light in time.")

    def output(self):
        return "Yellow"


def main():
    concrete_state_redlight = RedLight()
    concrete_state_greenlight = GreenLight()
    concrete_state_yellowlight = YellowLight()
    context = TrafficLight(concrete_state_greenlight)
    context.check()
    context.drive()
    context = TrafficLight(concrete_state_yellowlight)
    context.check()
    context.drive()
    context = TrafficLight(concrete_state_redlight)
    context.check()
    context.drive()


if __name__ == "__main__":
    main()
