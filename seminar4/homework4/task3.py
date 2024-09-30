# Задание 3.
# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

import decimal

CMD_DEPOSIT = 'П'
CMD_WITHDRAW = 'С'
CMD_BALANCE = 'Б'
CMD_EXIT = 'В'
RICH_LIMIT = decimal.Decimal(5_000_000)
RICH_TAX = decimal.Decimal(10/100)
WITHDRAW_PERCENT = decimal.Decimal(15/1000)
ADD_PERCENT = decimal.Decimal(3/100)
MULT = 50
MIN_REMOVAL = 30
MAX_REMOVAL = 600
COUNT_WITHDRAW = 3

operation_log = []

def logging(operation: str):
    print(operation)
    operation_log.append(operation)

def show_log():
    print("-- ЛОГ ОПЕРАЦИЙ --")
    for o in operation_log:
        print(o)

def show_menu():
    print(" \
        С: снять \n \
        П: пополнить \n \
        Б: баланс \n \
        В: выход"
          )

def get_tax(summ: decimal):
    percent = summ * RICH_TAX
    summ -= percent
    return True, summ, percent

def show_balance(summ: decimal.Decimal):
    print(f"Баланс счета: {summ:.2f}")
    logging(f"Баланс счета: {summ:.2f}")

def withdrow(summ: decimal.Decimal, count):
    amount = 1
    while amount % MULT != 0:
        amount = decimal.Decimal(input("Введите сумму "))

    percent = amount * WITHDRAW_PERCENT
    if percent < MIN_REMOVAL:
        percent = MIN_REMOVAL
    elif percent > MAX_REMOVAL:
        percent = MAX_REMOVAL

    if percent + amount <= summ:
        summ -= (amount + percent)
        count += 1
        logging(f"Снятие средств {amount:.2f} комиссия {percent:.2f}\nНа счету {summ:.2f}")
        if count == COUNT_WITHDRAW:
            count = 0
            percent = summ * ADD_PERCENT
            summ += percent
            logging(f"Начислены проценты {round(ADD_PERCENT * 100)}% {percent:.2f}\nНа счету {summ:.2f}")
        return True, summ, count
    else:
        logging(f"Ошибка снятия средств {amount:.2f} комиссия {percent:.2f}\nНа счету {summ:.2f}")
        return False, summ, count

def deposit(summ: decimal.Decimal):
    amount = 1
    while amount % MULT != 0:
        amount = decimal.Decimal(input("Введите сумму "))
    summ += amount
    return True, summ

def main():
    account = decimal.Decimal(0)
    count = 0
    while True:
        show_menu()
        command = input(f'Введите команду меню: ')
        if command == CMD_EXIT:
            break

        if command == CMD_BALANCE:
            show_balance(account)
            continue

        if account > RICH_LIMIT:
            logging('УДЕРЖАНИЕ НЕЛОГА')
            result, account, percent = get_tax(account)
            if result:
                logging(f"Удержан налог на богатство {int(RICH_TAX*100)}% {percent:.2f} у.е.\nНа счету {account:.2f} у.е.")
        if command == CMD_DEPOSIT:
                logging('ПОПОЛНЕНИЕ')
                result, account = deposit(account)
                if result:
                    logging(f"Пополнение карты\nНа счету {account} у.е.")
                else:
                    logging(f"Ошибка пополнения\nНа счету {account} у.е.")
        if command == CMD_WITHDRAW:
            logging('СНЯТИЕ')
            result, account, count = withdrow(account, count)
            if result:
                logging(f"Снятие средств выполнено успешно")
            else:
                logging(f"Недостаточно средств")
    logging(f"Заберите карту на которой {account:.2f} у.е.")
    show_log()

if __name__ == '__main__':
    main()

