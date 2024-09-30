# Задание 2
# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.
from itertools import count

COUNT = 2

data = [42, 73, 5, 42, 42, 2, 3, 5, 7, 73, 42]

list1 = []
for item in set(data):
    if data.count(item) == COUNT:
        list1.append(item)

print(list1)