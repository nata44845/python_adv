# Задание 3
# Функция получает на вход строку из двух чисел через пробел
# Сформируйте словарь, где ключом будет символ из Unicode, а значением целое число
# Диапазон пар ключ-значение от наименьшего из введенных пользователем чисел, до наибольшего включительно

def range_unicode(text) -> dict[str, int]:
    n1, n2, *rest = map(int,text.split())
    result = {}
    for i in range(min(n1,n2), max(n1,n2)+1):
        result[chr(i)] = i
    return result

data = input("Введите два числа через пробел: ")
print(range_unicode(data))