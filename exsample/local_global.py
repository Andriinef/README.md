global_result = "Hello, Python"


class MyClass:
    global_var = "I am global"  # объявление глобальной переменной в классе

    def __init__(self):
        self.local_var = "I am local"  # объявление локальной переменной в классе

    def print_vars(self):
        print(global_result)  # вывод глобальной переменной в не класса
        print(self.local_var)  # вывод локальной переменной
        print(self.global_var)  # вывод глобальной переменной


print(MyClass.global_var)  # вывод глобальной переменной за пределами класса
my_class = MyClass()  # создание экземпляра класса
my_class.print_vars()  # вызов метода класса для вывода переменных
