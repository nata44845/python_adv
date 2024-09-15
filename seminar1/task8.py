SPACE = ' '
STAR = '*'

num = int(input(f"Введите количество рядов: "))

for i in range(num):
    print(f"{SPACE*(num-i)}{STAR*(2*i+1)}")
