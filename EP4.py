###############
#  cccccccccccc
#r
#r
#r
#r
#r
#r
#r             sampleList[row][column]

def main():
    running = True
    player = 1
    print('Tic Tac Toe')
    gameBoard = [['#', '#', '#'], ['#', '#', '#'], ['#', '#', '#']]
    boardPrint(gameBoard)
    print()
    while(running):
        input1 = True
        input2 = True
        checkWin(gameBoard)
        if(player == 1):
            print('X\'s are playing')
            while(input1):
                firstRowInp = int(input('Enter the row for your play:\n'))
                firstColInp = int(input('Enter the column for your play:\n'))
                print()
                if(gameBoard[firstRowInp][firstColInp] == '#'):
                    gameBoard[firstRowInp][firstColInp] = 'x'
                    input1 = False
                else:
                    print('Enter a space that hasn\'t already been used')

            boardPrint(gameBoard)
            print()
            checkWin(gameBoard)
            if (checkWin(gameBoard) == 'X'):
                print()
                print('X\'s win!\n')
                running = False
        elif(player == 2):
            print('O\'s are playing')
            while(input2):
                secondRowInp = int(input('Enter the row for your play:\n'))
                secondColInp = int(input('Enter the column for your play:\n'))
                print()
                if(gameBoard[secondRowInp][secondColInp] == '#'):
                    gameBoard[secondRowInp][secondColInp] = 'o'
                    input2 = False
                else:
                    print('Enter a space that hasn\'t already been used')
            boardPrint(gameBoard)
            print()
            checkWin(gameBoard)
            if(checkWin(gameBoard) == 'O'):
                print()
                print('O\'s win!\n')
                running = False

        spaceCounter = 0

        for i in range(len(gameBoard)):
            for j in range(len(gameBoard[i])):
                if(gameBoard[i][j] != '#'):
                    spaceCounter += 1
                    if(spaceCounter == 9):
                        print('The game is a draw\n')
                        running = False

        if(player == 1):
            player = 2
        elif(player == 2):
            player = 1


def boardPrint(gameBoard):
    for i in range(len(gameBoard)):
        if(i == 1 or i == 2):
            print()
        for j in range(len(gameBoard[i])):
            print(gameBoard[i][j], end='\t')

def checkWin(gameBoard):
    #row checker
    if(gameBoard[0][0] == 'x' and gameBoard[0][1] == 'x' and gameBoard[0][2] == 'x'):
        return 'X'
    elif(gameBoard[1][0] == 'x' and gameBoard[1][1] == 'x' and gameBoard[1][2] == 'x'):
        return 'X'
    elif(gameBoard[2][0] == 'x' and gameBoard[2][1] == 'x' and gameBoard[2][2] == 'x'):
        return 'X'

    #column checker
    if(gameBoard[0][0] == 'x' and gameBoard[1][0] == 'x' and gameBoard[2][0] == 'x'):
        return 'X'
    elif(gameBoard[0][1] == 'x' and gameBoard[1][1] == 'x' and gameBoard[2][1] == 'x'):
        return 'X'
    elif(gameBoard[0][2] == 'x' and gameBoard[1][2] == 'x' and gameBoard[2][2] == 'x'):
        return 'X'

    # row checker
    if (gameBoard[0][0] == 'o' and gameBoard[0][1] == 'o' and gameBoard[0][2] == 'o'):
        return 'O'
    elif (gameBoard[1][0] == 'o' and gameBoard[1][1] == 'o' and gameBoard[1][2] == 'o'):
        return 'O'
    elif (gameBoard[2][0] == 'o' and gameBoard[2][1] == 'o' and gameBoard[2][2] == 'o'):
        return 'O'

    # column checker
    if (gameBoard[0][0] == 'o' and gameBoard[1][0] == 'o' and gameBoard[2][0] == 'o'):
        return 'O'
    elif (gameBoard[0][1] == 'o' and gameBoard[1][1] == 'o' and gameBoard[2][1] == 'o'):
        return 'O'
    elif (gameBoard[0][2] == 'o' and gameBoard[1][2] == 'o' and gameBoard[2][2] == 'o'):
        return 'O'


    #diagonal checker
    if(gameBoard[0][0] == 'x' and gameBoard[1][1] == 'x' and gameBoard[2][2] == 'x'):
        return 'X'
    elif(gameBoard[0][2] == 'x' and gameBoard[1][1] == 'x' and gameBoard[2][0] == 'x'):
        return 'X'

    if (gameBoard[0][0] == 'o' and gameBoard[1][1] == 'o' and gameBoard[2][2] == 'o'):
        return 'O'
    elif (gameBoard[0][2] == 'o' and gameBoard[1][1] == 'o' and gameBoard[2][0] == 'o'):
        return 'O'
    else:
        return 'Continue'


main()