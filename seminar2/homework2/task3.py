# Задание 3.
# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions
import fractions

def short(n, m):
    if n > m:
        k = n
    else:
        k = m
    while k != 1:
        if n % k == 0 and m % k == 0:
            return n // k, m // k
        else:
            k -= 1
    return n, m


num1 = input("Введите дробь 1: ")
num2 = input("Введите дробь 2: ")

c1, z1 = (int(i) for i in num1.split('/'))
c2, z2 = (int(i) for i in num2.split('/'))

csum = c1*z2+c2*z1
zsum = z1*z2
csum, zsum = short(csum, zsum)
summa = str(csum)+'/'+str(zsum)

cmult = c1*c2
zmult = z1*z2
cmult, zmult = short(cmult, zmult)
mult= str(cmult)+'/'+str(zmult)

print(f'Сумма {summa}\nПроизведение {mult}')

print(f'Сумма {fractions.Fraction(c1,z1)+fractions.Fraction(c2,z2)}')
print(f'Произведение {fractions.Fraction(c1,z1)*fractions.Fraction(c2,z2)}')


