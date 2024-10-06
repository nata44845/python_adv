# Задание 2
# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
__all__ = ['check_date']

from sys import argv

def _is_leap(year: int) -> bool:
    return year%400==0 or year%100!=0 and year%4==0

def check_date(full_date: str) -> bool:
    day, month, year = (int(i) for i in full_date.split('.'))
    if year<1 or year>9999 or month<1 or month>12 or day<1 or day>31:
        return False
    elif month in [4,6,9,11] and day>30:
        return False
    elif month == 2 and day>29:
        return False
    elif month == 2 and not _is_leap(year) and day>28:
        return False
    return True

if __name__ == '__main__':
    if len(argv)>1:
        print(f'Проверка даты {argv[1]} = {check_date(argv[1])}')