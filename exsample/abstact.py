from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Shape(ABC):
    color: str

    @abstractmethod
    def area(self):
        pass


@dataclass
class Rectangle(Shape):
    width: int
    height: int

    def area(self):
        return self.width * self.height


@dataclass
class Circle(Shape):
    radius: int

    def area(self):
        return 3.14 * self.radius * self.radius


figures = [Rectangle("red", 5, 3), Circle("blue", 4)]

for figure in figures:
    print(f"Площадь {type(figure).__name__}: {figure.area()}")
