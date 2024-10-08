# Задание 6
# Добавьте в модуль с загадками функцию, которая принимает на вход текст загадки и число, номер попытки
# Функция формирует словарь с информацией о результатах угадывания
# Для хранения используйте защищенный словарь уровня модуля
# Отдельно напишите функцию, которая выводит результаты угадывания из защищенного словаря в удобном для чтения виде
# Для формирования результатов используйте генераторное выражение


__all__ = ['riddle']

from task4 import riddle

_data = {}

def storage():
    puzzles = {
        'Зимой и летом одним цветом': ['ель', 'елка', 'ёлка', 'сосна'],
        'Сидит дед во сто шуб одет': ['лук', 'луковица'],
        'Не лает не кусает в дом не пускает': ['замок', 'домофон']
    }

    for key, item in puzzles.items():
        res = riddle(key, item)
        save_results(key, res)

def save_results(puzzle: str, nn: int) -> None:
    _data[puzzle] = nn

def show():
    res = (f"Загадку {puzzle} угадал с {nn} попытки" if nn>0
           else f"Загадка {puzzle} не разгадана" for puzzle, nn in _data.items())
    print(*res, sep = '\n')

if __name__ == '__main__':
    storage()
    show()