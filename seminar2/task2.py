# Создайте в переменной data  список значений различных типов, перечисли их через запятую внутри квадратных скобок
# Порядковый номер - Значение - Адрес в памяти - Размер в памяти - Хэш объекта
# Результат проверки на число, если положительный
# Результат проверки на строку, если положительный
# Добавьте в список повторяющиеся элементы и проверьте на результаты

import sys

data = [42, 73.0, 'Hello, world!', True, 42, 'Hello, world!', 256, 2**8, 1, 'Привет,  мир!']


for i, val in enumerate(data, 1):
    check_int = 'Целое число' if isinstance(val, int) else ""
    check_str = 'Строка' if isinstance(val, str) else ""
    print(f'{i}, {val}, {id(val)}, \n Адрес в памяти: {sys.getsizeof(val)}, {hash(val)} {check_int}{check_str}')