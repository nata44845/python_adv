# Задание 2
# Самостоятельно сохраните в переменной строку текста
# Создайте из строки словарь, где ключ - буква, а значение - код буквы.

text = 'Создайте из строки словарь, где ключ - буква, а значение - код буквы.'

my_dict =dict(sorted({i: ord(i) for i in set(text)}.items()))

print(my_dict)