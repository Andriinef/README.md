""" Создать свою версию такого класса,
    который бы поддерживал интерфейс стандартного range,
    но работал при этом с float.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class FloatRange:
    start: float
    stop: Optional[float] = None
    step: float = 1.0

    def __post_init__(self):
        if self.stop is None:
            self.start, self.stop = 0.0, self.start
        if self.step > 0 and self.start >= self.stop:
            self.current = None
        elif self.step < 0 and self.start <= self.stop:
            self.current = None
        else:
            self.current = self.start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        result = self.current
        self.current += self.step
        if self.step > 0 and self.current >= self.stop:
            self.current = None
        elif self.step < 0 and self.current <= self.stop:
            self.current = None
        return result


frange = FloatRange(1, 10, 3.5)
for i in frange:
    print(i)

assert list(FloatRange(5)) == [0, 1, 2, 3, 4]
assert list(FloatRange(2, 5)) == [2, 3, 4]
assert list(FloatRange(2, 10, 2)) == [2, 4, 6, 8]
assert list(FloatRange(10, 2, -2)) == [10, 8, 6, 4]
assert list(FloatRange(2, 5.5, 1.5)) == [2, 3.5, 5]
assert list(FloatRange(1, 5)) == [1, 2, 3, 4]
assert list(FloatRange(0, 5)) == [0, 1, 2, 3, 4]
assert list(FloatRange(0, 0)) == []
assert list(FloatRange(100, 0)) == []

print("SUCCESS!")
