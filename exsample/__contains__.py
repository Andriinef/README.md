class EvenNumbers:
    def __init__(self, limit):
        self.limit = limit

    def __contains__(self, num):
        return num % 2 == 0 and num <= self.limit

    def __iter__(self):
        self.current = 0
        return self

    def __next__(self):
        if self.current <= self.limit:
            result = self.current
            self.current += 2
            return result
        else:
            raise StopIteration


even_numbers = EvenNumbers(10)

print(4 in even_numbers)  # Output: True
print(5 in even_numbers)  # Output: False

for num in even_numbers:
    print(num, end=" ")  # Output: 0 2 4 6 8 10
