# Задание 7.
# Функция получает на вход словарь с названием компании в качестве ключа и списком с доходами и расходами
# Вычислите итоговую прибыль или убыток каждой компании, если все компании прибыльные верните истину, иначе ложь

def final_income_lambda(my_dict: dict[str, list[int|float]]) -> bool:
    return all(map(lambda x: sum(x)>0, my_dict.values()))

def final_income(my_dict: dict[str, list[int|float]]) -> bool:
    return all(sum(x)>0 for x in my_dict.values())

data = {
    "Рога": [42, -73, 12, 85, -15, 2],
    "Копыта": [45, 25, -100, 22, 1],
    "Хвосты": [-500, 123, 52, 45, 93],
}

print(final_income_lambda(data))
print(final_income(data))
