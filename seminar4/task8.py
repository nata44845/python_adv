# Задание 8
# Создайте несколько переменных, оканчивающиеся и не оканчивающиеся на s
# Напишите функцию, которая при запуске заменяет содержимое переменных, оканчивающихся на s
# (кроме переменной из одной s), без s на конце

def value_changer():
    g_var = globals()
    new_dict={}
    for key, value in g_var.items():
        if key.endswith('s') and key!='s':
            new_dict[key[:-1]]=value
            g_var[key] = None
    for key, value in new_dict.items():
        g_var[key] = value

data = [42, -73, 12, 85, -15, 2]
s = 'Hello world'
names = ['NoName', 'OtherName', 'NewName']
sx = 42

value_changer()

print(globals())



