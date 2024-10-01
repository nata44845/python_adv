# Задание 2
# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

def parse_path(path):
    path_only, _, file_name = path.rpartition('\\')
    file_name, _, file_ext = file_name.rpartition(".")
    return path_only, file_name, file_ext

if __name__ == '__main__':
    print(parse_path('C:\\Nata\\GeekBrains\\gb-git\\python_adv\\seminar3\\task1.py'))