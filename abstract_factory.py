"""
This is an interface to make dependent or logically related objects
without the need up-front to specify the classes,
so you can make multiple grouping of classes with this one abstract
factory

"""

import abc


class DayScheduleAbstractFactory(metaclass=abc.ABCMeta):
    """
    Declare an interface for operations that create abstract calendar reminder objects.
    """

    @abc.abstractmethod
    def create_calendar_reminder_10am(self):
        pass

    @abc.abstractmethod
    def create_calendar_reminder_noon(self):
        pass


class ConcreteFactoryMonday(DayScheduleAbstractFactory):
    """
    Declare an interface for operations that create abstract calendar reminder objects.
    """

    def create_calendar_reminder_10am(self):
        return ConcreteProduct10amMon()

    def create_calendar_reminder_noon(self):
        return ConcreteProductnoonMon()


class ConcreteFactoryWednesday(DayScheduleAbstractFactory):
    """
    Implement the creation of concrete calendar reminder objects
    """

    def create_calendar_reminder_10am(self):
        return ConcreteProduct10amWed()

    def create_calendar_reminder_noon(self):
        return ConcreteProductnoonWed()


class AbstractProductMonday(metaclass=abc.ABCMeta):
    """
    This is a product type interface for Monday
    """

    @abc.abstractmethod
    def schedule_meeting(self):
        pass


class ConcreteProduct10amMon(AbstractProductMonday):
    """
    Define a 10am Monday calendar concrete product object to be created by the corresponding concrete
    factory.
    Implement the abstract product type interface for Monday interface.
    """

    def schedule_meeting(self):
        print("Monday at 10am, we discuss design patterns")


class ConcreteProductnoonMon(AbstractProductMonday):
    """
    Define a noon Monday calendar concrete product object to be created by the corresponding concrete
    factory.
    Implement the abstract product type interface for Monday interface.
    """

    def schedule_meeting(self):
        print("Monday at noon, we eat lunch at our desks")


class AbstractProductWednesday(metaclass=abc.ABCMeta):
    """
    This is a product type interface for Wednesday    
    """

    @abc.abstractmethod
    def schedule_meeting(self):
        pass


class ConcreteProduct10amWed(AbstractProductWednesday):
    """
    Define a 10am Wednesday calendar concrete product object to be created by the corresponding concrete
    factory.
    Implement the abstract product type interface for Wednesday interface.
    """

    def schedule_meeting(self):
        print("Wednesday at 10am, we look at the top priority backlog item")


class ConcreteProductnoonWed(AbstractProductWednesday):
    """
    Define a noon Wednesday calendar concrete product object to be created by the corresponding concrete
    factory.
    Implement the abstract product type interface for Wednesday interface.
    """

    def schedule_meeting(self):
        print("Wednesday at noon, we go to lunch at the diner")


def main():
    for factory in (ConcreteFactoryMonday(), ConcreteFactoryWednesday()):
        print("next one")
        product_a = factory.create_calendar_reminder_10am()
        product_b = factory.create_calendar_reminder_noon()
        product_a.schedule_meeting()
        product_b.schedule_meeting()


if __name__ == "__main__":
    main()
