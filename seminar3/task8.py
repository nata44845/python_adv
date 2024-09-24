# Задание 8. Множества
# Три друга взяли веши в поход. Сформируйте словарь, где ключ имя друга, а значения кортеж вешей
# Какие вещи взяли все три друга
# Какие вещи уникальны, есть только у одного
# Какие вещи есть у всех друзей, кроме одного и имя того, у кого отсутствует
# Для решения используйте операции с множествами

hike = {
    'Aaz': ("спички", "спальник", "дрова", "топор"),
    'Skeeve': ("спальник", "спички", "вода", "еда"),
    'Tananda': ("вода", "спички", "косметичка")
}
# Все
all_things = set()
for value in hike.values():
    all_things=all_things.union(set(value))
print(all_things)

# Уникальные
uniq_things = {}
for key1, first in hike.items():
    for key2, second in hike.items():
        if key1!=key2:
            if key1 not in uniq_things:
                uniq_things[key1] = set(first)-set(second)
            else:
                uniq_things[key1] -= set(second)
print(uniq_things)

# Нет у одного
double_things = set(all_things) #копия
one_things = {}
for things in uniq_things.values():
    double_things -= things
print(double_things)

for key, things in hike.items():
    print(f"1. У {key} отсутствуют {double_things - set(things)}")
    print(f"2. У {key} отсутствуют {(set(things)^double_things) - set(uniq_things[key])}")


