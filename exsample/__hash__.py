class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __hash__(self):
        return hash((self.name, self.age))

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age


person1 = Person("Alice", 25)
person2 = Person("Bob", 30)
person3 = Person("Alice", 25)

print(hash(person1))
print(hash(person2))
print(hash(person3))
