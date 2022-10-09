
#Создайте программу для игры в ""Крестики-нолики"".

#Пример интерфейса:
#
#   |   | 0
#-----------    
#   |   |
#-----------
#   | X |
#Ввод можно реализовать через введение двух чисел (номеров строки и столбца).

# a=[['1','2'],['3','4'],['5','6'],['7','8'],['9','10'],['11','12'],['13','14'],['15','16'],['17','18'],]
# print (a)

# print (a[0][0], a[0][1])
# print("\t {} | {} | {} ".format(a[0][0], a[0][1], a[0][2]))
# def print_pole (pole):
#     print("\t {} | {} | {} ".format(pole[0][0], pole[0][1], pole[0][2]))

# print_pole(a)

board = list(range(1,10))

def draw_board(board):
    print ("-" * 13)
    for i in range(3):
        print (board[0+i*3], "|", board[1+i*3], "|", board[2+i*3])
        print ("-" * 13)

def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input("Where will we put " + player_token+"? ")
        try:
            player_answer = int(player_answer)
        except:
            print ("Invalid input. Are you sure you entered a number?")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer-1]) not in "XO"):
                board[player_answer-1] = player_token
                valid = True
            else:
                print ("This cell is already taken")
        else:
            print ("Invalid input. Enter a number from 1 to 9 to be like.")

def check_win(board):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print (tmp, "won!")
                win = True
                break
        if counter == 9:
            print ("Draw!")
            break
    draw_board(board)

main(board)
