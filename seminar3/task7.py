# Задание 7. Количество символов в строке
# Пользователь вводит строку текста. Посчитайте сколько раз встречается каждая буква в строке без использования метода count и с ним
# Результат сохраните в словаре, где ключ - символ, а значение частота встречи
# Обратите внимание на порядок ключей

data = input("Введите строку текста: ")

my_dict1 = {}
for i in set(data):
    my_dict1[i] = data.count(i)
print(my_dict1)

my_dict2 = {}
for i in data:
    my_dict2.setdefault(i,0)
    my_dict2[i] +=1
print(my_dict2)

my_dict3 = {}
for i in data:
    my_dict3[i] = my_dict3.get(i,0)+1
print(my_dict3)