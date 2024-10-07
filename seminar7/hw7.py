# Задание 2.
# Напишите функцию группового переименования файлов. Она должна:
# - принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# - принимать параметр количество цифр в порядковом номере.
# - принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# - принимать параметр расширение конечного файла.
# - принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

__all__ = ['gen_random_files', 'file_group_rename']

from random import sample, choice
import string
from pathlib import Path
import os


__all__ = ['file_group_rename']

def gen_random_files(count: int):
    file_ext = ['txt', 'jpg', 'mov', 'mp3', 'bin', 'csv', 'md', 'doc']
    for _ in range(count):
        name = ''.join(sample(string.ascii_lowercase, 10)) + '.' + choice(file_ext)
        with open(name, 'w', encoding='utf-8') as file:
            file.write(name)

def file_group_rename(path: str = Path.cwd(),
                 new_name: str = '',
                 count: int = 1,
                 in_ext: str = '',
                 out_ext: str = '___',
                 limits: tuple = (0, 10)):
    counter = 1
    path = Path(path)
    if path.is_dir():
        for file in path.iterdir():
            if file.is_file():
                name, ext = file.stem, file.suffix[1:]
                if ext == in_ext or not in_ext:
                    re_name = (f'{name[limits[0]-1:limits[1]]}'
                               f'{new_name if new_name else ""}'
                               f'{counter:0>{count}}.{out_ext}')
                    print(f'{name} {ext} -> {re_name}')
                    path_new = os.path.join(path, re_name)
                    if not Path(path_new).is_file():
                        os.rename(file, path_new)
                        counter += 1
                    else:
                        print(f'Ошибка сохранения уже есть файл {path_new}')
        print(f'Было переименовано {counter - 1}')
    else:
        print('Это не директория!')


if __name__ == '__main__':
    gen_random_files(5)
    file_group_rename(# path = 'c:\\Nata\\GeekBrains\\gb-git\\python_adv\\seminar7\\dir\\photo',
                      new_name='time', in_ext='txt', out_ext='text', count=1, limits=(1, 1))