# Задание 5. Словарь
# Функция принимает на вход три списка одинаковой длины: имена, ставка, премия
# Вернуть словарь с именем в качестве ключа и суммой премии в качестве значения
# Сумма рассчитывается как ставка, умноженная на процент премии
import decimal

def bonus_list(names: list[str], bets: list[int], rewards: list[str]) -> dict[str, decimal.Decimal]:
        result = {}
        for name, bet, reward in zip(names, bets, rewards):
            result[name] = bet*decimal.Decimal(reward[:-1])/100
        return result

n = ['Alex', 'Ben', 'Chris']
b = [20000, 10000, 30000]
r = ['5.5%','10.25%','3.14%']

print(bonus_list(n,b,r))
