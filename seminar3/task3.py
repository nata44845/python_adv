# Задание 3
# Создайте вручную кортеж, содержащий элементы разных типов
# Получите из него словарь списков, где ключ тип элемента, значение список элементов типа

data = (42, 73, 3.14, 'Hello world!', None, True, 'Text', 100500.2, False)

my_dict = {}
for item in data:
    my_dict.setdefault(type(item),[])
    my_dict[type(item)].append(item)

print(my_dict)