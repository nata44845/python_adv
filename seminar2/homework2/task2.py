# Задание 2.
# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

HEX = 16
HEX_ARRAY = [i for i in range(10)] +['а','b','c','d','e','f']


num = int(input("Введите число: "))
x = num
result: str = ''
while x>0:
    result = str(HEX_ARRAY[x%HEX])+result
    x //= HEX
print(f'{HEX=} {result=}')

print(f'{hex(num)=}')


