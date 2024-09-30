# Задание 2.
# Создайте модуль с функцией внутри
# Функция принимает на вход три целых числа: нижнюю, верхнюю границы и количество попыток
# Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за количество попыток
# Функция выводит подсказки больше и меньше
# Если число угадано возвращается истина, если попытки исчерпаны ложь

__all__ = ['guess']

from random import randint

def guess(lower: int = 0, upper: int = 100, count: int = 10):
    number = randint(lower, upper)
    for i in range(1, count+1):
        num = lower - 1
        while num < lower or num > upper:
            num = int(input(f"Попытка {i}. Введите число ({lower},{upper}): "))
        if number<num:
            print(f"{num} больше загаданного")
        elif number>num:
            print(f"{num} меньше загаданного")
        else:
            print("вы угадали")
            return True
    return False


if __name__ == '__main__':
    print(guess(1,4,3))