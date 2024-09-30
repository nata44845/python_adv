# Задание 2
# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.

def var_dict(**kwargs):
    result = dict()
    for k, v in kwargs.items():
        try:
            _ = hash(v)
            result[v] = k
        except TypeError:
            result[str(v)] = k
    return result

print("Исх. параметры: first=\"one\", second=2, third=3, fourth=\"four\", fifth=[2, 3]")
print(var_dict(first="one", second=2, third=3, fourth="four", fifth=[2, 3]))