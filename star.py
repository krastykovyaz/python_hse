# Пользователь вводит число, обязательно нечетное и символ, программа рисует диагонали квадрата. 
# Ввод 5
# *
# Вывод
# *   *
#  * *
#   *
#  * *
# *   *
number = int(input())
symbol = str(input())
i = number - 1
j = 0
for row in range(number):
    for colomn in range(number):
        char = ' '
        if row == colomn or number - row - 1 == colomn:
            char = symbol
        print(char, end='')
    print()
