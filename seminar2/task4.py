# Напишите программу, которая вычисляет площадь круга и длину окружности по введенному диаметру
# Диаметр не превышает 1000
# Точность вычислений не менее 42 знаков после запятой
import math
import decimal

decimal.getcontext().prec = 42

LOWER_LIMIT = 1
UPPER_LIMIT = 1000
PI = decimal.Decimal(math.pi)

diam = LOWER_LIMIT - 1

while diam < LOWER_LIMIT or diam > UPPER_LIMIT:
    diam = int(input(f"Введите диаметр от {LOWER_LIMIT} до {UPPER_LIMIT}: "))

sqr = decimal.Decimal(PI*diam**2/4)
okr = decimal.Decimal(PI*diam)
print(f'Площадь круга: {sqr}\nДлина окружности: {okr}')