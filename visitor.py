import abc
"""
Created on Dec 10, 2018

@author: Erik Pohl
"""

"""
An abstract class represents an action to perform on another class. 
The visitor class visits the element and the behavior changes
of the element class without changing the class itself.
"""


class HotelRoomElement(metaclass=abc.ABCMeta):
    """
    A visitor class is accommodated with this abstract method
    """

    @abc.abstractmethod
    def accommodate(self, visitor):
        pass


class WaldorfAstoriaConcreteElement(HotelRoomElement):
    """
    A visitor class is accommodated with this method
    """

    def accommodate(self, visitor):
        visitor.visit_waldorf_astoria_concrete_element(self)


class NoTellMotelConcreteElement(HotelRoomElement):
    """
    A visitor class is accommodated with this method
    """

    def accommodate(self, visitor):
        visitor.visit_no_tell_motel_concrete_element(self)


class HotelVisitor(metaclass=abc.ABCMeta):
    """
    For each concrete class of the element, define a visit.
    The operation's name and signature is enough to specify
    theclass that sends the Visit request to the visitor. 
    The visitor responds with a concrete class of the element 
    being visited.
    The visitor accesses the instance for that class.
    """

    @abc.abstractmethod
    def visit_waldorf_astoria_concrete_element(self, waldorf_astoria_concrete_element):
        pass

    @abc.abstractmethod
    def visit_no_tell_motel_concrete_element(self, no_tell_motel_concrete_element):
        pass


class BusinessVisitorConcreteVisitor(HotelVisitor):
    """
    Implement Visitor declared operations. Each operation
    implements a fragment of the algorithm for the corresponding class. 
    The concrete visitor provides the
    context for the algorithm and stores its local state. 
    """

    def visit_waldorf_astoria_concrete_element(self, waldorf_astoria_concrete_element):
        print("Wow.  I don't even want to check out my credit card bill.")

    def visit_no_tell_motel_concrete_element(self, no_tell_motel_concrete_element):
        print("Just another day travelling on business.")


class LuxuryVisitorConcreteVisitor(HotelVisitor):
    """
    Implement Visitor declared operations. Each operation
    implements a fragment of the algorithm for the corresponding class. 
    The concrete visitor provides the
    context for the algorithm and stores its local state. 
    """

    def visit_waldorf_astoria_concrete_element(self, waldorf_astoria_concrete_element):
        print("This is where my I stay when visiting friends in New York.")

    def visit_no_tell_motel_concrete_element(self, no_tell_motel_concrete_element):
        print("I can afford better, but there's a reason I'm here")


def main():
    luxury_visitor_concretevisitor = LuxuryVisitorConcreteVisitor()
    waldorf_concrete_element = WaldorfAstoriaConcreteElement()
    waldorf_concrete_element.accommodate(luxury_visitor_concretevisitor)

    business_visitor_concretevisitor = BusinessVisitorConcreteVisitor()
    no_tell_concrete_element = NoTellMotelConcreteElement()
    no_tell_concrete_element.accommodate(business_visitor_concretevisitor)
    
    waldorf_concrete_element.accommodate(business_visitor_concretevisitor)
    no_tell_concrete_element.accommodate(luxury_visitor_concretevisitor)


if __name__ == "__main__":
    main()
