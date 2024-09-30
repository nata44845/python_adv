# Задание 4.
# Создайте модуль с функцией внутри
# Функция получает на вход загадку, список с возможными вариантами отгадок и количеством попыток на угадывание
# Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если исчерпаны

def riddle(riddle_text: str, answers: list[str], count: int = 3) -> int:
    print(f'Отгадай загадку\n{riddle_text}')
    for i in range(1,count+1):
        answer = input(f'Попытка {i}: ')
        if answer.lower() in list(map(lambda x: x.lower(),answers)):
            return i
    return 0

if __name__ == '__main__':
    print("Угадал" if riddle("Ни окон ни дверей полна горница людей",["Огурец","огурец"], 3)>0 else "не угадал")