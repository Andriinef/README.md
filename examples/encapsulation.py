class Person:
    def __init__(self, name: str, sex: str, age: int):
        self.name = name  # public
        self._sex = sex  # protected
        self.__age = age  # private

    def get_age(self) -> int:
        return self.__age

    def _set_age(self, age) -> None:  # protected method
        if age < 0:
            print("Age cannot be negative.")
        else:
            self.__age = age

    def __private_method(self) -> float:  # private method
        return 2000.00

    def get_currency(self, ratio: float) -> float:
        currency = self.__private_method()
        sum = currency * ratio
        return sum


if __name__ == "__main__":
    # создаем экземпляр класса BankAccount
    users = Person("John", "men", 25)

    # попытка получить доступ к защещенным и закрытым атрибутам
    print(users._sex)  # women
    # print(users.__age)         # ошибка!

    # получаем доступ к закрытым атрибутам через методы класса
    print(users.get_age())  # 25

    # попытка изменить закрытый атрибут напрямую
    users.__age = 26  # не изменяет атрибут, а создает новый открытый атрибут!
    print(users.get_age())  # 25

    # изменяем закрытый атрибут через защещенный метод класса
    users._set_age(26)
    print(users.get_age())  # 26

    # начисление зарплаты
    sum = users.get_currency(39)
    print(f"{users.name}: {sum}")
