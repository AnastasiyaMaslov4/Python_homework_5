# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг 
# после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота

from random import randint

start = randint(0, 2)

candy = 200

while candy > 28:
    if start == 0:
        player_takes = int(input("Ваш ход. Введите количество конфет (от 1 до 28): "))
        candy = candy - player_takes
        print(f"Осталось конфет: {candy}")
        start = 1
        print()
    else:
        bot_takes = randint(1, 29)
        candy = candy - bot_takes
        print(f"Бот взял {bot_takes}  конфет")
        print(f"Осталось конфет: {candy}")
        start = 0
        print()

if start == 0:
    print("Вы победили!")
else:
    print("Победил бот :(")


