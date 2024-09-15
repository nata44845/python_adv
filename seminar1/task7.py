LOWER_LIMIT = 1
UPPER_LIMIT = 999
ONE = 1
TEN = 10
HUNDRED = 100
SQUARE = 2

num = LOWER_LIMIT - 1

while num < LOWER_LIMIT or num > UPPER_LIMIT:
    num = int(input(f"Введите число от {LOWER_LIMIT} до {UPPER_LIMIT}: "))
if num < TEN:
    res = f"Число {num} цифра, квадрат {num**SQUARE}"
elif num < HUNDRED:
    first_num = num//TEN
    second_num = num%TEN
    res = f"Число {num} двузначное, произведение {first_num*second_num}"
else:
    num1 = num//HUNDRED
    num2 = num%HUNDRED//TEN
    num3 = num%TEN
    mirror = num3*HUNDRED+num2*TEN+num1
    res = f"Число {num} трехзначное, переворот {mirror}"
print(res)
