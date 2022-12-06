from abc import ABC, abstractmethod
from enum import Enum

class FigureType(Enum):
    Square = 'square'
    Triangle = 'triangle'

class Figure(ABC):

    @abstractmethod
    def __init__(self, name):
        self.name = name
        self.kind = FigureType.Square.value
        print('You created "{}" which is {}'.format(name, self.kind))

    @abstractmethod
    def calc_pole(self, *args):
        pass

    @abstractmethod
    def calc_obwod(self, *args):
        pass

class Square(Figure):
    def __init__(self, name):
        self.name = name 
        self.kind = FigureType.Square.value
        print('You created "{}" which is {}'.format(name, self.kind))
    
    def calc_pole(self, a):
        pole = a * a
        return pole
    
    def calc_obwod(self, a):
        obwod = a * 4
        return obwod

class Triangle(Figure):
    def __init__(self, name):
        self.name = name 
        self.kind = FigureType.Triangle.value
        print('You created "{}" which is {}'.format(name, self.kind))
    
    def calc_pole(self, a, h = None):
        pole = 0
        if a and h:
            pole = (a * h)/2
        return pole
    
    def calc_obwod(self, a, b = None, c = None):
        obwod = 0
        if a and b and c:
            obwod = a + b + c
        return obwod



#vehicle = Vehicle()
square = Square('kwadrat 1')
print(square.calc_obwod(5))

square = Triangle('trojkat 1')
print(square.calc_obwod(5))