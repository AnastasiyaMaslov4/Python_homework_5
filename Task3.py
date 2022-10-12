# Создайте программу для игры в "Крестики-нолики".

game_board = list(range(1,10))

def draw_board(game_board):
    print("-------------")
    for i in range(3):
        print("|", game_board[0+i*3], "|", game_board[1+i*3], "|", game_board[2+i*3], "|")
        print("-------------")

used_cell = []

def x_turn():
    valid = 0
    while valid == 0:
        x_step = int(input("Игрок Х, введите номер клетки, которую хотите занять: "))
        if (0 < x_step < 10) and x_step not in used_cell:
            game_board[x_step - 1] = str("X")
            used_cell.append(x_step)
            valid = 1
            draw_board(game_board)
        else:
            print("Не верное число. Введите цифру от 1 до 9")
        

def o_turn():
    valid = 0
    while valid == 0:
        o_step = int(input("Игрок О, введите номер клетки, которую хотите занять: "))
        if (0 < o_step < 10) and o_step not in used_cell:
            game_board[o_step - 1] = str("O")
            used_cell.append(o_step)
            valid = 1
            draw_board(game_board)
        else:
            print("Не верное число. Введите цифру от 1 до 9")
        
draw_board(game_board)

x_turn()
o_turn()
x_turn()
o_turn()
x_turn()
o_turn()
x_turn()
o_turn()
x_turn()

def who_wins():
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for i in win_coord:
        if game_board[i[0]] == game_board[i[1]] == game_board[i[2]]:
            print(f"Победил игрок {game_board[i[0]]}")
            quit()
    print("Ничья")
        

who_wins()
