# Задание 2
# Напишите функцию, которая принимает строку текста
# Сформируйте список с уникальными кодами Unicode каждого символа, отсортированный по убыванию

def chars(text):
    text = sorted(text)
    my_list = []
    for item in set(text):
        my_list.append(ord(item))
    return(sorted(my_list, reverse=True))

data = input("Введите строку текста: ")

print(chars(data))