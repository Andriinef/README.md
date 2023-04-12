def my_decorator(func):
    def wrapper():
        print("My name, Ahdrii.")
        func()
        print("Word!")

    return wrapper


@my_decorator
def say_hello():
    print("Hello")


def my_decorator_(func):
    def wrapper():
        print("Before the function is called.")
        func()
        print("After the function is called.")

    return wrapper


@my_decorator_
def my_function():
    print("Hello World!")


if __name__ == "__main__":
    say_hello()
    my_function()
