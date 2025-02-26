# Interpreter design pattern

from abc import ABC, abstractmethod

# Interface
class Expression(ABC):
    @abstractmethod
    def interpret(self, context):
        pass

# Terminal Expression
class Number(Expression):
    def __init__(self, number):
        self.number = number

    def interpret(self, context):
        return self.number
    
# NonTerminal Expression for addition
class Add(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def interpret(self, context):
        return self.left.interpret(context) + self.right.interpret(context)
    
# NonTerminal Expression for subtraction
class Subtract(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def interpret(self, context):
        return self.left.interpret(context) - self.right.interpret(context)

# Context
class Context:
    def __init__(self):
        self.variables = {}

# Client
context = Context()

# syntaxt tree
expr = Subtract(
    Add(Number(5), Number(3)),
    Add(Number(2), Number(1))
    )

# Interpreting the expression
result = expr.interpret(context)
print(f'The result of expression is: {result}')
