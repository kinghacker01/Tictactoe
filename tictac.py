board = [' ' for x in range(10)]


def printboard(board):
    print("   |   |   ")
    print(" " + board[1] + " | " + board[2] + " | " + board[3] + " ")
    print("   |   |   ")
    print("------------")
    print("   |   |   ")
    print(" " + board[4] + " | " + board[5] + " | " + board[6] + " ")
    print("   |   |   ")
    print("------------")
    print("   |   |   ")
    print(" " + board[7] + " | " + board[8] + " | " + board[9] + " ")
    print("   |   |   ")


def isfreespace(pos):
    return board[pos] == ' '


def isfullboard(board):
    if board.count(' ') == 1:
        return True
    else:
        return False


def insertletter(pos, letter):
    board[pos] = letter


def randomselect(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]


def iswinner(b, le):
    return ((b[1] == le and b[2] == le and b[3] == le) or
            (b[4] == le and b[5] == le and b[6] == le) or
            (b[7] == le and b[8] == le and b[9] == le) or
            (b[1] == le and b[4] == le and b[7] == le) or
            (b[2] == le and b[5] == le and b[8] == le) or
            (b[3] == le and b[6] == le and b[9] == le) or
            (b[1] == le and b[5] == le and b[9] == le) or
            (b[3] == le and b[5] == le and b[7] == le))


def playermove():
    run = True
    while run:
        move = input("Select a position to place an X between (1-9):")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if isfreespace(move):
                    insertletter(move, 'X')
                    run = False
                else:
                    print("Sorry!The position is already occupied!")
            else:
                print("Please select a number between (1-9)")

        except:
            print("Please type a number!")


def compmove():
    possiblemove = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possiblemove:
            boardcopy = board[:]
            boardcopy[i] = let
            if iswinner(boardcopy, let):
                move = i
                return move

    corneropen = []
    for i in possiblemove:
        if i in [1, 3, 7, 9]:
            corneropen.append(i)

    if len(corneropen) > 0:
        move = randomselect(corneropen)
        return move

    if 5 in possiblemove:
        move = 5
        return move

    edgesopen = []
    for i in possiblemove:
        if i in [2, 4, 6, 8]:
            edgesopen.append(i)

    if len(edgesopen) > 0:
        move = randomselect(edgesopen)
        return move


def main():
    print("Welcome to Tic Tac Toe")
    printboard(board)

    while not isfullboard(board):
        if not iswinner(board, 'O'):
            if not isfullboard(board):
                playermove()
                printboard(board)
        else:
            print("Computer won this time!")
            break

        if not iswinner(board, 'X'):
            if not isfullboard(board):
                move = compmove()
                if move == 0:
                    print("Tie Game!")
                else:
                    insertletter(move, 'O')
                    print("Computer placed an \'O\' in position ", move, "!")
                    printboard(board)

        else:
            print("You won the Game!")
            break

    if isfullboard(board):
        print("Tie Game!")


main()
while True:
    print("Do you want to play again?[y/n]")
    play = input()
    if play.lower() == 'y':
        board = [' ' for x in range(10)]
        main()
    else:
        break
