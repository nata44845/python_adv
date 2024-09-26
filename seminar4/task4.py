# Задание 4
# Функция получет на вход список чисел
# Отсортируйте его элементы in place без использования встроенных сортировок
# Как вариант напишите сортировку пузырьком

def bubble_sort(my_list: list[int]):
    for i in range(len(my_list)):
        for j in range(i+1, len(my_list)):
            if my_list[i]>my_list[j]:
                my_list[i], my_list[j] = my_list[j], my_list[i]
    return my_list

data = [42, 73, 5, 42, 42, 2, 3, 7, 73, 42]

print(data)
print(bubble_sort(data))
