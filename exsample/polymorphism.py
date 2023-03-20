from dataclasses import dataclass


@dataclass
class Figure:
    color: str

    def area(self):
        pass


@dataclass
class Rectangle(Figure):
    color: str
    length: int
    width: int

    def area(self):
        return self.length * self.width


@dataclass
class Circle(Figure):
    color: str
    circle: int

    def area(self):
        return 3.14 * self.circle**2


figures = [Rectangle("red", 5, 3), Circle("blue", 4)]

for figure in figures:
    print(f"Площадь {type(figure).__name__}: {figure.area()}")
