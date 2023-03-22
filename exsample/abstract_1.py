from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


rect = Rectangle(5, 10)
print(rect.area())  # выводит 50
print(rect.perimeter())  # выводит 30
