# Задание 6.
# Функция получает на вход список чисел и два индекса
# Вернуть сумму чисел между переданными индексами
# Если индекс выходит за пределы списка, сумма считается до конца или начала списка


def sum_between_idx(my_list: list[int | float], ind1: int, ind2: int) -> int | float:
    i_max = max(ind1, ind2)
    i_max = min(i_max, len(my_list))
    i_min = min(ind1, ind2)
    i_min = max(i_min, 0)
    sum = 0
    for i in range(i_min, i_max):
            sum += my_list[i]
    return sum

print(sum_between_idx([1,2,3,4,5,6], 4, 35))