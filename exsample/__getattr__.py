class MyClass:
    def __init__(self, name):
        self.name = name

    def __getattr__(self, attr):
        return f"{attr} does not exist"

    def __getattribute__(self, attr):
        return f"getting attribute {attr} for {self.name}"


my_obj = MyClass("example")

# используем метод getattr
print(getattr(my_obj, "name"))  # Output: example
print(getattr(my_obj, "age", 25))  # Output: 25
print(getattr(my_obj, "invalid"))  # Output: invalid does not exist

# используем метод getattribute
print(my_obj.name)  # Output: getting attribute name for example
print(my_obj.age)  # вызовет AttributeError
