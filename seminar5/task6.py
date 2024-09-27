# Задание 6.
# Выведите в консоль таблицу умножения от 2x2 до 9x10 как на школьной тетради
# Таблицу создайте в виде однострочного генератора, где каждый элемент генератора отдельный пример
# Для вывода используйте print без перехода на новую строку


# Таблица умножения
LOWER_LIMIT = 2
UPPER_LIMIT = 10
COLUMN = 4
ONE = 1

# for i_main in (LOWER_LIMIT, LOWER_LIMIT + COLUMN):
#     for s_num in range(LOWER_LIMIT, UPPER_LIMIT + ONE):
#         for f_num in range(i_main, i_main + COLUMN):
#             print(f"{f_num:>2} x{s_num:>2} ={f_num*s_num:>2}", end='\t')
#         print()
#     print()

table = (f"{f_num:>2} x{s_num:>2} ={f_num*s_num:>2}\t"  if f_num<i_main + COLUMN - ONE
        else f"{f_num:>2} x{s_num:>2} ={f_num*s_num:>2}\n" if s_num<UPPER_LIMIT
        else f"{f_num:>2} x{s_num:>2} ={f_num*s_num:>2}\n\n"
    for i_main in (LOWER_LIMIT, LOWER_LIMIT + COLUMN)
    for s_num in range(LOWER_LIMIT, UPPER_LIMIT + ONE)
    for f_num in range(i_main, i_main + COLUMN)
    )

print('', *table)