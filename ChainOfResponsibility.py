"""
Class design benefits from decoupling senders of requests from receivers
This pattern allows you to do this by designing a series
"if this doesn't work, try this" objects to handle the request.
The request gets passed along until an object handles it.
"""

import abc


class Handler(metaclass=abc.ABCMeta):
    """
    This is the request handling interface.  It contains an abstract method for handling
    and a successor definition.
    """

    def __init__(self, successor=None):
        self._successor = successor

    @abc.abstractmethod
    def handle_request(self, speed_mph):
        pass


class AirBagConcreteHandler(Handler):
    """
    The airbag handles it or passes it along if a successor exists
    """

    def handle_request(self, speed_mph):
        if speed_mph <= 35:  # if can_handle:
            print("Airbag handled it as it is under 36 mph")
        elif self._successor is not None:
            self._successor.handle_request(speed_mph)
        elif self._successor is None:
            print("No successor safety feature")


class SeatBeltConcreteHandler(Handler):
    """
    The seatbelt handles it or passes it along if a successor exists
    """

    def handle_request(self, speed_mph):
        if speed_mph < 16:  # if can_handle:
            print("Seat belt handled it as it is under 16 mph")
        elif self._successor is not None:
            self._successor.handle_request(speed_mph)


def main():
    concrete_handler_1 = AirBagConcreteHandler()
    concrete_handler_2 = SeatBeltConcreteHandler(concrete_handler_1)
    concrete_handler_2.handle_request(8)
    concrete_handler_2.handle_request(12)
    concrete_handler_2.handle_request(18)
    concrete_handler_2.handle_request(35)
    concrete_handler_2.handle_request(40)


if __name__ == "__main__":
    main()
