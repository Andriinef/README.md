# Python Interview Questions

1. Как вы улучшите производительность программы в Python?

2. Каковы преимущества использования Python?

3. Как вы указате кодирование исходного кода в исходном файле Python?

4. Каково использование PEP 8 в Python?

5. Что такое маринован в питоне?

6. Как работает управление памятью в Python?

7. Как вы будете выполнять статический анализ на сценарии Python?

8. В чем разница между кортежом и списком в Python?

9. Что такое декоратор Python?

10. Как аргументы передаются методом Python?По значению или по ссылке?

11. В чем разница между типами данных списка и словаря в Python?

12. Какие различные встроенные типы данных доступны в Python?

13. Что такое пространство имен в Python?

14. Как вы будете объединять несколько строк вместе в Python?

15. Как использовать оператор Pass в Python?

16. Для чего используется Slicing в Python?

17. В чем разница между Docstring в Python и Javadoc в Java?

18. Как выполнять модульное тестирование для кода на Python?

19. В чем разница между итератором и итерируемым объектом в Python?

20. Для чего используется генератор в Python?

21. Каково значение функций, которые начинаются и заканчиваются символом "_" в Python?

22. В чем разница между xrange и range в Python?

23. Что такое лямбда-выражение в Python?

24. Как скопировать объект в Python?

25. Каковы основные преимущества использования Python?

26. Что такое метакласс в Python?

27. Для чего используется frozenset в Python?

28. Что такое Python Flask?

29. Что такое None в Python?

30. Для чего используется функция zip() в Python?

31. Для чего используется оператор // в Python?

32. Что такое модуль в Python?

33. Как создать словарь с упорядоченным набором ключей в Python?

34. Python - это объектно-ориентированный язык программирования или функциональный язык программирования?

35. Как можно извлечь данные из базы данных MySQL в скрипте Python?

36. В чем разница между функциями append() и extend() для списка в Python?

37. Как обрабатывать ошибочные ситуации в коде Python?

38. В чем разница между функцией split() и срезами (slicing) в Python?

39. Как проверить в Python, является ли класс подклассом другого класса?

40. Как отлаживать код в Python?

41. Как профилировать скрипт на Python?

42. В чем разница между операторами "is" и "==" в Python?

43. Как можно передавать переменные между модулями в Python?

44. Как можно использовать функциональное программирование в Python?

45. В чем улучшение функции enumerate() в Python?

46. Как выполнить скрипт Python в Unix?

47. Какие популярные библиотеки Python используются для анализа данных?

48. Какой будет вывод следующего кода на Python?

49. Какой будет вывод следующего кода на Python?

50. Если у вас есть данные с именами клиентов и их местоположением, какой тип данных вы будете использовать для хранения этой информации в Python?

## Questions Python Interview

### 1. **Как можно улучшить производительность программы на Python?**

Существует множество способов улучшения производительности программы на Python. Некоторые из них перечислены ниже:

* **Структура данных**: Необходимо выбрать правильную структуру данных для нашей цели в программе на Python.

* **Стандартная библиотека**: Везде, где это возможно, следует использовать методы из стандартной библиотеки. Методы, реализованные в стандартной библиотеке, имеют гораздо более высокую производительность, чем пользовательские реализации.

* **Абстракция**: Иногда излишняя абстракция и косвенность могут привести к медленной производительности программы. Мы должны удалить ненужную абстракцию в коде.

* **Алгоритм**: Использование правильного алгоритма может сделать большую разницу в программе. Нам нужно найти и выбрать подходящий алгоритм для решения нашей проблемы с высокой производительностью.

### 2. Каковы преимущества использования Python?

Python настолько мощный, что даже Google его использует. Некоторые из преимуществ использования Python следующие:

* **Эффективность**: Python очень эффективен в управлении памятью. Для больших наборов данных, таких как Big Data, гораздо проще программировать на Python.

* **Быстрота**: хотя код Python интерпретируется, он все равно имеет очень быстрое выполнение.

* **Широкое применение**: Python широко используется в разных организациях для различных проектов. Благодаря этому широкому использованию, для Python доступно тысячи дополнений.

* **Легко изучаем**: Python довольно прост в изучении. Это самое большое преимущество использования Python. Сложные задачи могут быть очень легко реализованы на Python.

### 3. Как вы будете указывать кодировку исходного кода в файле исходного кода Python?

По умолчанию каждый файл исходного кода в Python находится в кодировке UTF-8. Но мы также можем указать свою собственную кодировку для исходных файлов. Это можно сделать, добавив следующую строку после строки #! в исходном файле.

```code
# -*- coding: encoding -*-
```

В приведенной выше строке мы можем заменить encoding на кодировку, которую мы хотим использовать.

### 4. Каково назначение PEP 8 в Python?

**PEP 8** - это руководство по стилю для кода на языке Python. Данный документ содержит рекомендации по стилю написания кода на Python. Конвенции оформления касаются отступов, форматирования, табуляции, максимальной длины строки, организации импортов, промежутков между строками и т.д. Мы используем PEP 8, чтобы обеспечить единообразие в нашем коде. Благодаря этому другим разработчикам будет проще читать наш код.

### 5. Что такое Pickling (пиклирование) в Python?

**Pickling** (пиклирование) - это процесс, с помощью которого иерархия объектов Python может быть преобразована в байтовый поток. Обратная операция Pickling - это Unpickling. В Python есть модуль с именем pickle. Этот модуль имеет реализацию мощного алгоритма для сериализации и десериализации структуры объекта Python. Некоторые люди также называют Pickling сериализацией или маршалингом. С помощью сериализации мы можем передавать объекты Python через сеть. Он также используется для сохранения состояния объекта Python. Мы можем записать его в файл или базу данных.

### 6. Как работает управление памятью в Python?

В Python есть частное кучное пространство (private heap space), которое содержит все объекты Python и структуры данных. В CPython есть менеджер памяти, который отвечает за управление кучей.

В менеджере памяти Python есть различные компоненты, которые обрабатывают сегментацию, совместное использование, кэширование, предварительное выделение памяти и т.д.

Менеджер памяти Python также заботится об уборке мусора с помощью алгоритма подсчета ссылок.

### 7. Как выполнить статический анализ Python-скрипта?

Для этой цели мы можем использовать инструмент статического анализа, называемый **PyChecker**. **PyChecker** может обнаруживать ошибки в Python-коде и предупреждать о стилевых проблемах.

Некоторые другие инструменты для поиска ошибок в Python-коде - это pylint и pyflakes.

### 8. Чем отличается Tuple от List в Python?

В Python, Tuple и List являются встроенными структурами данных.

Некоторые из различий между Tuple и List:

* **Синтаксис**: Tuple заключается в круглые скобки: например, myTuple = (10, 20, "apple"); List заключается в квадратные скобки: например, myList = [10, 20, 30];

* **Изменяемость**: Tuple является неизменяемой структурой данных, тогда как List является изменяемой;

* **Размер**: Tuple занимает гораздо меньше места, чем List в Python;

* **Производительность**: Tuple быстрее, чем List в Python, что обеспечивает хорошую производительность;

* **Сфера применения**: так как Tuple неизменяемый, мы можем использовать его, например, для создания словаря. List предпочтительнее в случае, когда данные могут изменяться.

### 9. Что такое декоратор Python?

**Python Decorator** - это механизм, который позволяет обернуть функцию Python и изменить ее поведение, добавив к ней дополнительную функциональность. Мы можем использовать символ @ для вызова функции Python Decorator.

**Python Decorator** - это способ изменения поведения функции путем обертывания ее другой функцией. Это функция высшего порядка, которая принимает функцию в качестве входных данных и возвращает измененную функцию в качестве выходных данных. Функция-декоратор определяется с помощью символа "@" с последующим именем функции, которую нужно декорировать.

Например, рассмотрим следующий код:

```python
def my_decorator(func):
    def wrapper():
        print("Before the function is called.")
        func()
        print("After the function is called.")
    return wrapper

@my_decorator
def my_function():
    print("Hello World!")


if __name__ == "__main__":
    my_function()
```

Здесь функция my_decorator определяется для изменения поведения функции my_function. Функция my_function декорируется функцией my_decorator с помощью символа "@". Теперь, когда мы вызываем функцию my_function, она сначала вызывает функцию my_decorator, которая выводит "Before the function is called.", затем вызывает функцию my_function, которая выводит "Hello World!", и, наконец, выводит "After the function is called.".

Таким образом, декораторы предоставляют способ добавления функциональности к функции без изменения ее исходного кода. Они обычно используются для добавления журналирования, профилирования и кэширования функций, среди прочего.

### 10. Как передаются аргументы в методе Python? По значению или по ссылке?

Каждый аргумент в методе Python является объектом. Все переменные в Python имеют ссылку на объект. Поэтому аргументы в методе Python передаются по ссылке. Так как некоторые объекты, переданные как ссылки, являются изменяемыми, мы можем изменять эти объекты в методе. Однако для неизменяемого объекта, такого как строка, любые изменения, сделанные внутри метода, не отражаются снаружи.

В Python аргументы передаются по ссылке. Это означает, что при вызове метода создается ссылка на объект, который передается в качестве аргумента, и этот объект доступен из метода через эту ссылку.

Если аргументом является неизменяемый объект, то метод не может изменить его значение в вызывающей части программы. Например, если аргументом является число, то метод не может изменить его значение в вызывающей части программы.

Если же аргументом является изменяемый объект, то метод может изменить его состояние. Например, если аргументом является список, то метод может изменить содержимое списка в вызывающей части программы.

Важно понимать, что при передаче изменяемых объектов по ссылке можно неожиданно изменить состояние объекта внутри метода, что может привести к ошибкам в программе. Поэтому важно быть осторожным при работе с изменяемыми объектами в методах Python.

### 11. Чем отличаются типы данных List (список) и Dictionary (словарь) в Python?

Основные отличия между типами данных List и Dictionary в Python следующие:

* **Синтаксис**: В списке мы храним объекты в последовательности, а в словаре мы храним объекты в парах ключ-значение.

* **Обращение**: В списке мы обращаемся к объектам по номеру индекса, начиная с индекса 0. В словаре мы обращаемся к объектам по ключу, указанному при создании словаря.

* **Упорядоченность**: В списке объекты хранятся в упорядоченной последовательности. В словаре объекты не хранятся в упорядоченной последовательности.

* **Хеширование**: В словаре ключи должны быть хешируемыми. В списке хеширование не требуется.

### 12. Какие существуют встроенные типы данных в Python?

Некоторые из встроенных типов данных в Python следующие:

* **Числовые типы**: Это типы данных, используемые для представления чисел в Python.
  * **int**: Используется для целых чисел.
  * **long**: Используется для очень больших целых чисел неограниченной длины.
  * **float**: Используется для десятичных чисел.
  * **complex**: Используется для представления комплексных чисел.

* **Типы последовательностей**: Эти типы данных используются для представления последовательности символов или объектов.
  * **str**: Это аналог String в Java. Он может представлять последовательность символов.
  * **bytes**: Это последовательность целых чисел в диапазоне от 0 до 255.
  * **bytearray**: Подобно bytes, но изменяемый (см. ниже); доступен только в Python 3.x.
  * **list**: Это последовательность объектов.
  * **tuple**: Это последовательность неизменяемых объектов.

* **Множества (Sets)**: Это неупорядоченные коллекции.
  * **set**: Это коллекция уникальных объектов.
  * **frozenset:** Это коллекция уникальных неизменяемых объектов.

* **Mappings**: Это аналог Map в Java.
  * **dict**: Это также называется хеш-таблицей. Он имеет пары **ключ-значение** для хранения информации с использованием хеширования.

### 13. Что такое пространство имен (Namespace) в Python?

**Пространство имен (Namespace)** в Python - это соответствие между именем и объектом. В настоящее время оно реализовано как словарь Python. Например, множество имен исключений, множество встроенных имен, локальные имена в функции. В различные моменты времени в Python создаются разные пространства имен. Каждое пространство имен в Python может иметь разный срок жизни. Для списка встроенных имен создается пространство имен, когда интерпретатор Python запускается. Когда интерпретатор Python считывает определение модуля, он создает глобальное пространство имен для этого модуля. Когда интерпретатор Python вызывает функцию, он создает локальное пространство имен для этой функции.

### 14. Как объединить несколько строк вместе в Python?

Мы можем использовать следующие способы, чтобы объединить несколько строк вместе в Python:

* использовать оператор **+**:

Например:

```python
fname = "John"
lname = "Ray"
print(fname + lname)
JohnRay
```

* использовать функцию **join**:

Например:

```python
''.join(['John', 'Ray'])
'JohnRay'
```

### 15. Для чего используется оператор Pass в Python?

Оператор **Pass** в Python используется для выполнения ничего. Это всего лишь заполнитель для оператора, который необходим для синтаксических целей. Он не выполняет никакого кода или команды.

Некоторые случаи использования оператора Pass:

* Для целей синтаксиса:

```python
while True:
    pass # Ждем, пока пользователь введет что-то
```

* Для создания минимальных классов:

```python
class MyMinimalClass:
    pass
```

* В качестве заполнителя для работы TODO:
Также мы можем использовать его в качестве заполнителя для работы TODO в функции или коде, который должен быть реализован позже.

```python
def initialization():
    pass # TODO
```