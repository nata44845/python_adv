# Напишите программу, которая запрашивает год и проверяет его на високосность
# Напишите проверки в цепочке elif
# Откажитесь от магических чисел
# Учтите год ввода Григорианского календаря
# В коде один input и один print

REFORM = 1584
BIG_LEAP_YEAR = 400
SMALL_LEAP_YEAR = 4
LARGE_NON_LEAP_YEAR = 100
MULTIPLE = 0

year = int(input("Введите год: "))

if year<REFORM:
    res = "Григорианский календарь не введен"
elif year % BIG_LEAP_YEAR == MULTIPLE:
    res = f"{year} високосный год"
elif year % LARGE_NON_LEAP_YEAR == MULTIPLE:
    res = f"{year} невисокосный год"
elif year % SMALL_LEAP_YEAR == MULTIPLE:
    res = f"{year} високосный год"
else:
    res = f"{year} невисокосный год"

print(res)
