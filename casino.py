import random
from random import randint
balance = 100
print ("--------Казино у пайтоні--------")
def show_rules():
    file_path = 'rules.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()
        print(file_content)


def start():
    chose = int(input("--Показати правила(1), грати(2), показати баланс(3)"))
    if chose == 1:
        show_rules()
        start()
    if chose == 2:
        play()
        start()
    if chose == 3:
        print(f"Ваш баланс--{balance}")
        start()
    if chose > 3:
        print("Прочитайте ще раз і введіть правильне число")
        start()


def play():
    global balance
    bal = balance

    print(f"Ваш баланс:{bal}")
    a = int(input ("Введіть вашу ставку або (0) для виходу"))
    if a == 0:
        start()
    if a > (balance):
        print("У вас немає стільки грошей :(")
        start()
    z = (randint(1,7))
    x = (randint(1,7))
    c = (randint(1,7))
    print(f"--{z}--{x}--{c}--")
    roll = int(z + x + c)
    if (roll) < 12:
        l = int(a / roll)
        print(f"Ви програли. Ви отримуєте---{l}")
        price = bal - a + l
        print(f"Ваш баланс---{price}")
        balance = price
    elif (roll) > 12:
        w = int(a * roll/3)
        print(f"Ви виграли. Ви отримуєте---{w}")
        price = bal - a + w
        print(f"Ваш баланс---{price}")
        balance = price

start()




