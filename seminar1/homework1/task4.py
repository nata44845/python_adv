# Задание 4.
# Программа загадывает число от 0 до 1000.
# Необходимо угадать число за 10 попыток.
# Программа должна подсказывать “больше” или “меньше” после каждой попытки.

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
COUNT = 10

num = randint(LOWER_LIMIT, UPPER_LIMIT)

i = 0

x = LOWER_LIMIT - 1
print("Угадайте число от 0 до 1000 за 10 попыток")
while i<COUNT and x!=num:
    print(f"\nПопытка {i+1}")
    x = LOWER_LIMIT - 1
    while x<LOWER_LIMIT or x>UPPER_LIMIT:
        x = int(input("Введите число: "))
    if num>x:
        print(f"Загаданное число больше {x}")
    elif num<x:
        print(f"Загаданное число меньше {x}")
    i += 1

if x==num:
    print(f"Вы угадали, ваше число {x}, загадано число {num}")
else:
    print(f"Вы не угадали за 10 попыток, загадано число {num} ")

