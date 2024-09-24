# Задание 2
# Пользователь вводит данные, сделайте проверку данных и преобразуйте если возможно в один из вариантов ниже:
# Целое положительное число
# Вещественное положительное или отрицательное число
# Строку в нижнем регистре, если в строке есть хотя бы одна заглавная буква
# Строку в верхнем регистре в остальных случаях

data = input("Введите данные: ")
if data.isdigit():
    result =int(data)
elif data.count('.')<=1 and data.count('-')<2 and '-' not in data[1:]\
    and data.replace('.','').replace('-','').isdigit():
    result = float(data)
elif not data.islower():
    result = data.lower()
else:
    result = data.upper()

print(result, type(result))