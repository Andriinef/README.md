def my_decorator(func):
    def wrapper():
        print("My name, Ahdrii.")
        func()
        print("Word!")

    return wrapper


@my_decorator
def say_hello():
    print("Hello")


say_hello()
