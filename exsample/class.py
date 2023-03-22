class MyClass:
    def __init__(self, attribute1: str, attribute2: int):
        self.attribute1 = attribute1
        self.attribute2 = attribute2

    def method1(self):
        return print(f"method1: {self.attribute1}")

    def method2(self):
        self.method1()
        MyClass("Piter", 30).method1()
        return print(f"method2: {self.attribute2}")


"""Далее мы можем создать объект этого класса и использовать его **методы**:"""

my_object = MyClass("Meri", 25)
my_object.method1()
my_object.method2()

"""Также мы можем обращаться к **атрибутам** объекта:"""

print(my_object.attribute1)
print(my_object.attribute2)
