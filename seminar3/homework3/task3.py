# Задание 3.
# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.
import re

text = 'The first version requires that numerator and denominator are instances \
of numbers.Rational and returns a new Fraction instance with value numerator/denominator. \
If denominator is 0, it raises a ZeroDivisionError. The second version requires that other_fraction \
is an instance of numbers.Rational and returns a Fraction instance with the same value. \
The next two versions accept either a float or a decimal.Decimal instance, and return a Fraction \
instance with exactly the same value. Note that due to the usual issues with binary floating point \
(see Floating-Point Arithmetic: Issues and Limitations), the argument to Fraction(1.1) is not exactly \
equal to 11/10, and so Fraction(1.1) does not return Fraction(11, 10) as one might expect. \
(But see the documentation for the limit_denominator() method below.) The last version of the \
constructor expects a string or unicode instance. The usual form for this instance is:)'

list1 = [i.lower() for i in re.findall(r'\w+', text)]
my_dict = {}
for item in set(list1):
    my_dict[item] = list1.count(item)

for i, (key, count) in enumerate(sorted(my_dict.items(), key=lambda item: item[1], reverse = True)[:10],1):
    print(i,key, count)
