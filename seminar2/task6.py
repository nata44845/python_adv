# Напишите программу банкомат
# Начальная сумма равна 0
# Допустимые действия: пополнить, снять, выйти
# Суммы пополнения и снятия кратны 50
# Процент за снятие 1.5% от суммы снятия, но не менее 30 и не более 600
# После каждой третьей операции снятия начисляются проценты 3%
# Нельзя снять больше, чем на счете
# При превышении суммы 5 млн вычитать налог на богатство перед каждой операцией, даже ошибочной
# Любое действие выводит сумму денег

import decimal

CMD_DEPOSIT = 'П'
CMD_WITHDRAW = 'С'
CMD_EXIT = 'В'
RICH_LIMIT = decimal.Decimal(5_000_000)
RICH_TAX = decimal.Decimal(10/100)
WITHDRAW_PERCENT = decimal.Decimal(15/1000)
ADD_PERCENT = decimal.Decimal(3/100)
MULT = 50
MIN_REMOVAL = 30
MAX_REMOVAL = 600
COUNT_WITHDRAW = 3

account = decimal.Decimal(0)
count = 0

while True:
    command = input(f'Пополнить {CMD_DEPOSIT}, Снять {CMD_WITHDRAW}, Выход {CMD_EXIT} ')
    if command == CMD_EXIT:
        print(f"Заберите карту на которой {account} у.е.")
        break
    if account > RICH_LIMIT:
        percent = account*RICH_TAX
        account -= percent
        print(f"Удержан налог на богатство {percent}")
    print(f"На счету {account} у.е.")
    if command in (CMD_WITHDRAW, CMD_DEPOSIT):
        amount = 1
        while amount%MULT != 0:
            amount = decimal.Decimal(input("Введите сумму "))

        if command == CMD_DEPOSIT:
            account += amount
            print(f"Пополнение карты на {amount}\nНа счету {account} у.е.")
        elif command == CMD_WITHDRAW:
            percent = amount * WITHDRAW_PERCENT
            if percent<MIN_REMOVAL:
                percent = MIN_REMOVAL
            elif percent>MAX_REMOVAL:
                percent = MAX_REMOVAL

            if percent+amount<=account:
                account -= (amount+percent)
                count += 1
                print(f"Снятие средств {amount} комиссия {percent}\nНа счету {account}")
                if count == COUNT_WITHDRAW:
                    count = 0
                    percent = account*ADD_PERCENT
                    account += percent
                    print(f"Начислены проценты {round(ADD_PERCENT*100)}% {percent}\nНа счету {account}")
            else:
                print(f"Недостаточно средств, сумма {amount}, комиссия {percent}, на карте {account}")



