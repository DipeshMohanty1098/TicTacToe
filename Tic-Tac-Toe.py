import os
clear  = lambda: os.system('cls')
grid = [0]*9
turn = 0


def player1():
    turn = int(input("player 1 enter position: "))
    while turn not in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
        print("Invalid Position! Enter again!")
        turn = int(input("player 1 enter position: "))
    res = check_pos(int(turn))
    if res == 0:
        print("Position taken! Pls enter position again")
        player1()
    else:
        grid[int(turn) - 1] = 'X'


def print_board(grid):
    for i in range(0,8,3):
        print("{}|{}|{} ".format(grid[i], grid[i + 1], grid[i + 2]))
        print('_ _ _')


def player2():
    turn = (input("player 2 enter position: "))
    while turn not in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
        print("Invalid Position! Enter again!")
        turn = int(input("player 1 enter position: "))
    res = check_pos(int(turn))
    if res == 0:
        print("Position taken! Pls enter position again")
        player2()
    else:
        grid[int(turn) - 1] = 'O'


def check_pos(turn):
    if grid[turn-1] != 0:
        flag = 0
    else:
        flag = 1
    return flag


def check(grid):
    if (((grid[0] == 'X' and grid[1] == 'X' and grid[2]) == 'X') or
         ((grid[3] == 'X'and grid[4] == 'X' and grid[5]) == 'X') or
        ((grid[6] == 'X' and grid[7] == 'X' and grid[8]) == 'X') or
        ((grid[0] == 'X' and grid[4] == 'X' and grid[8]) == 'X') or
         ((grid[2] == 'X'and grid[4] == 'X' and grid[6]) == 'X') or
        ((grid[0] == 'X' and grid[3] == 'X' and grid[6]) == 'X') or
        ((grid[1] == 'X' and grid[4] == 'X' and grid[7]) == 'X') or
         ((grid[2] == 'X' and grid[5] == 'X' and grid[8]) == 'X')):
        print("Player 'X' wins!!")
        print_board(grid)
        run = False
        return run
    elif (((grid[0] == "O" and grid[1] == "O" and grid[2]) == "O") or
          ((grid[3] == "O" and grid[4] == "O" and grid[5]) == "O") or
          ((grid[6] == "O" and grid[7] == "O" and grid[8]) == "O") or
          ((grid[0] == "O" and grid[4] == "O" and grid[8]) == "O") or
          ((grid[2] == "O" and grid[4] == "O" and grid[6]) == "O") or
          ((grid[0] == "O" and grid[3] == "O" and grid[6]) == "O") or
          ((grid[1] == "O" and grid[4] == "O" and grid[7]) == "O") or
          ((grid[2] == "O" and grid[5] == "O" and grid[8]) == "O")):
        print("Player 'O' wins!!")
        print_board(grid)
        run = False
        return run
    else:
        pass


def check_draw(grid):
    if (grid[0] != 0 and grid[1] != 0 and grid[3] != 0 and grid[4] != 0 and grid[5] != 0 and
         grid[6] != 0 and grid[7] != 0 and grid[8] != 0):
            print("DRAW! Neither win!!!")
            print_board(grid)
            run = False
            return run
    else:
        pass


def board_reset(grid):
    for i in range(len(grid)):
        grid[i] = 0


def main():
    print("Ready to play? Y or N")
    ready = str(input().upper())
    if ready == 'Y':
        run = True
        print_board(grid)
    else:
        run = False
    while run is True:
            player1()
            check_pos(turn)
            print_board(grid)
            res1 = check(grid)
            if res1 is False:
                x = str(input("Play Again? Y or N: ").upper())
                if x == 'Y':
                    board_reset(grid)
                    main()
                else:
                    break
            res3 = check_draw(grid)
            if res3 is False:
                x = str(input("Play Again? Y or N: ").upper())
                if x == 'Y':
                    board_reset(grid)
                    main()
                else:
                    break
      
            player2()
            check_pos(turn)
            print_board(grid)
            res2 = check(grid)
            if res2 is False:
                x = str(input("Play Again? Y or N: ").upper())
                if x == 'Y':
                    board_reset(grid)
                    main()
                else:
                    break


main()














