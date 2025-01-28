import abc

"""
Created on Dec 11, 2018

@author: Erik Pohl
"""

"""
cake := frosting |  layer | filling 
layer := strawberry cake | chocolate cake | vanilla cake
frosting := coconut icing | cream cheese icing | fudge icing
filling := walnuts | peanut butter | sprinkles
"""

"""
The interpreter uses a grammar representation to interpret "sentences" in the language 
"""


class CakePartAbstractExpression(metaclass=abc.ABCMeta):
    """
    Here we define an abstract interpret operation valid for every node
    in the syntax tree
    """

    @abc.abstractmethod
    def interpret(self):
        pass

    
class CakeFillingAbstractExpression(CakePartAbstractExpression):
    """
    Here we define an abstract interpret operation valid for every node
    in the syntax tree
    """

    
class CakeLayerAbstractExpression(CakePartAbstractExpression):
    """
    Here we define an abstract interpret operation valid for every node
    in the syntax tree
    """


class CakeFrostingAbstractExpression(CakePartAbstractExpression):
    """
    Here we define an abstract interpret operation valid for every node
    in the syntax tree
    """


class CakeNonterminalExpression(CakePartAbstractExpression):
    """
    We implement a nonterminal symbol interpret operation
    """

    def __init__(self, expression):
        self._expression = expression

    def interpret(self):        
        self._expression.interpret()


class LayerNonterminalExpression(CakeLayerAbstractExpression):
    """
    We implement a terminal symbol interpret operation
    """

    def __init__(self, expression):
        self._expression = expression

    def interpret(self):        
        self._expression.interpret()


class LayerStrawberryCakeTerminalExpression(CakeLayerAbstractExpression):
    """
    We implement a terminal symbol interpret operation
    """

    def interpret(self):
        print("strawberry cake layer")    


class LayerChocolateCakeTerminalExpression(CakeLayerAbstractExpression):
    """
    We implement a terminal symbol interpret operation
    """

    def interpret(self):
        print("chocolate cake layer")

        
class LayerVanillaCakeTerminalExpression(CakeLayerAbstractExpression):
    """
    We implement a terminal symbol interpret operation
    """    

    def interpret(self):
        print("vanilla cake layer")   


class FrostingTerminalExpression(CakeFrostingAbstractExpression):
    """
    We implement a terminal symbol interpret operation
    """

    def interpret(self):
        print("frosting")


class FrostingCherryTerminalExpression(CakeFrostingAbstractExpression):
    """
    We implement a terminal symbol interpret operation
    """

    def interpret(self):
        print("cherry frosting")


class FrostingCreamCheeseTerminalExpression(CakeFrostingAbstractExpression):
    """
    We implement a terminal symbol interpret operation
    """

    def interpret(self):
        print("Cream Cheese frosting")


class FrostingFudgeTerminalExpression(CakeFrostingAbstractExpression):
    """
    We implement a terminal symbol interpret operation
    """

    def interpret(self):
        print("Fudge frosting")

            
class FillingNonterminalExpression(CakeFillingAbstractExpression):
    """
    We implement a nonterminal symbol interpret operation
    """

    def __init__(self, expression):
        self._expression = expression

    def interpret(self):        
        self._expression.interpret()


class FillingSprinklesTerminalExpression(CakeFillingAbstractExpression):
    """
    We implement a terminal symbol interpret operation
    """    

    def interpret(self):
        print("sprinkles filling")


class FillingPeanutButterTerminalExpression(CakeFillingAbstractExpression):
    """
    We implement a terminal symbol interpret operation
    """        

    def interpret(self):
        print("peanut butter filling")


class FillingWalnutsTerminalExpression(CakeFillingAbstractExpression):
    """
    We implement a terminal symbol interpret operation
    """    
    
    def interpret(self):
        print("walnuts filling")
        

def main():
    abstract_syntax_tree = CakeNonterminalExpression(FrostingFudgeTerminalExpression())
    abstract_syntax_tree.interpret()
    abstract_syntax_tree = CakeNonterminalExpression(LayerNonterminalExpression(LayerChocolateCakeTerminalExpression()))
    abstract_syntax_tree.interpret()
    abstract_syntax_tree = CakeNonterminalExpression(FillingNonterminalExpression(FillingSprinklesTerminalExpression()))
    abstract_syntax_tree.interpret()
    abstract_syntax_tree = CakeNonterminalExpression(
        LayerNonterminalExpression(LayerStrawberryCakeTerminalExpression())
    )
    abstract_syntax_tree.interpret()
    abstract_syntax_tree = CakeNonterminalExpression(FrostingCherryTerminalExpression())
    abstract_syntax_tree.interpret()    


if __name__ == "__main__":
    main()
