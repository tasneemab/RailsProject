from random import randint, choice
import copy


# check row if it's valid
def checkRow(bo, val, pos):
    row, col = pos[0], pos[1]

    for i in range(len(bo[0])):
        if bo[row][i] == val and col != i:
            return False
    return True


# check col if it's valid
def checkCol(bo, val, pos):
    row, col = pos[0], pos[1]
    for j in range(len(bo)):
        if bo[j][col] == val and row != j:
            return False
    return True


# check if each sub-square is valid
def checkSquare(bo, val, pos):
    row, col = pos[0], pos[1]
    x = col // 3
    y = row // 3
    for i in range(y * 3, y * 3 + 3):
        # we run on sub-boards, row after row
        for j in range(x * 3, x * 3 + 3):
            if bo[i][j] == val and (i, j) != (row, col):
                return False
    return True


# Checks if the number can be added to the board
def isValid(bo, val, pos):
    if ((checkRow(bo, val, pos)
         and checkCol(bo, val, pos)) and checkSquare(bo, val, pos)):
        return True
    return False


# find all the empty cells in the matrix (has 0) and return their position or cells that can be replaced
def findEmptyCells(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] is 0:
                return i, j
    return 0


# find all the cells that can be replaced
def findMovableCells(bo, fc):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if (i, j) not in fc:
                return i, j
    return 0


# fills the board with values in range(1,9), finds a legal solution
def fillBoard(bo):
    cells = []
    # find an empty cell
    empty = findEmptyCells(bo)
    # if there's no one like this we ends this function
    if not empty:
        return True
    else:  # there's an empty cell
        pos = empty
        # the position of the empty cell
    for x in range(9):
        cells.append(randint(1, 9))
        # an if statement to check if the value we add is legal
    for i in cells:
        if isValid(bo, i, pos):
            bo[pos[0]][pos[1]] = i
            # recursive call for the function fillBoard, to check whether we filled it legally or not
            if fillBoard(bo):
                return True
            bo[pos[0]][pos[1]] = 0  # rest the value and try another num
    return False


# printing the board in a special format
def printBoard(bo, fc):
    for i in range(len(bo)):
        if i % 3 == 0:
            print('-' * 34)

        for j in range(len(bo[0])):
            if j % 3 == 0:
                print('| ', end='')
            if j == 8:
                print(f' {str(bo[i][j])}', '|')
            elif bo[i][j] != 0 and (i, j) in fc:
                print('.' + str(bo[i][j]) + ' ', end='')
            else:
                print(f' {str(bo[i][j])} ', end='')
    print('-' * 34)


# Creates empty board
def createEmptyBoard():
    sudokuBoard = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    return sudokuBoard


# generate a primary sudoku board
def sudokuGenerator(bo, numOfCells):
    getBoard = fillBoard(bo)
    if getBoard:
        startBoard(bo, numOfCells)


# starts the board according to how many cells the user wants to be filled
def startBoard(bo, val):
    counter = val
    fixedCells = []
    i = randint(0, 8)
    j = randint(0, 8)

    # בוחרים תאים בצורה רנדומאלית כדי לשמור אותם להמשך המשחק
    while counter > 0:
        if (i, j) not in fixedCells:
            fixedCells.append((i, j))
            counter -= 1
        # מגרילים שוב אינדקסים חדשים
        i = randint(0, 8)
        j = randint(0, 8)

    deleteUnfixed(bo, fixedCells)


# deletes all the cells except the ones have been generated
def deleteUnfixed(bo, fc):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if (i, j) not in fc:
                bo[i][j] = 0
    printBoard(bo, fc)
    gameController(bo, fc)
    return bo


# checks if the board is solved
def isSolved(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return False
    return True


# gives a hint for the user
def giveHint(bo, pos):
    numbers = []
    board = copy.deepcopy(bo)
    for num in range(1, 10):
        if isValid(board, num, pos) and num not in numbers:
            numbers.append(num)
    print("hint: set cell {} to {} ".format(pos, choice(numbers)))


# checks if the current board can be solved
def validate(bo, fc):
    board = copy.deepcopy(bo)  # get a deep copy of the board
    if fillBoard(board):  # checks if it can be
        print('The sudoku board can be solved')
        gameController(bo, fc)
    else:
        print('The sudoku board can not be solved')
        answer = input('do you want to generate another board ? y/n')
        if answer == 'y':
            main()
        else:
            exit(0)


# controls the game
def fillVal(bo, value, pos, fc):
    fullCells = []
    if pos not in fullCells and pos not in fc:

        if isValid(bo, value, pos):
            bo[pos[0]][pos[1]] = value
            fullCells.append((pos[0], pos[1]))
            printBoard(bo, fc)
            return True
    else:
        return False


# check if the command that we got from the user is valid
def validCommand(command, bo, fc):
    command = [x for x in command.split(' ')]
    fullCells = [] + fc

    if command[0].upper() == 'SET':
        if len(command) != 4:
            print('Error: invalid command')
            gameController(bo, fc)

        else:
            row = command[2]
            col = command[1]
            pos = (int(command[2]), int(command[1]))
            value = command[3]
            if (row.isdigit() and col.isdigit()) and value.isdigit():
                row = int(row)
                col = int(col)
                value = int(value)
                if row in range(0, 10) and col in range(0, 10) and value in range(1, 10):
                  if fillVal(bo, value, pos, fc):
                     fullCells.append(pos)
                     gameController(bo, fc)
                  else:
                      print('The command you have entered can not be done')
                else:
                    print('Error: invalid values')
                    gameController(bo, fc)

    elif command[0].upper() == 'HINT':
        if len(command) !=3:
            print('Error: invalid command')
            gameController(bo, fc)
        else:
            row = command[2]
            col = command[1]
            pos = (int(command[2]), int(command[1]))
            if row.isdigit() and col.isdigit():
                if pos not in fullCells:
                    giveHint(bo, pos)

            else:
              print('Error: invalid command')

    elif command[0].upper() == 'VALIDATE':
        validate(bo, fc)

    elif command[0].upper() == 'RESTART':
        print('Starting a new game...')
        main()

    elif command[0].upper() == 'EXIT':
        print('Exiting the game...')
        exit(0)
    else:
        print('Error: invalid command')


# Controls and starts the game
def gameController(bo, fc):
    if not isSolved(bo):
        command = input('Enter a command\n')

    while not isSolved(bo) and command != ' ':
        validCommand(command, bo, fc)
        if not isSolved(bo):
            command = input('Enter a command\n')
        if isSolved(bo):
            continue

    # asks the user if he wants to replay the game
    if isSolved(bo):
        print('Great Job, you solved the sudoku board')
        ask = input('Do you want to start a new game ? y/n\n')
        if ask == 'y':
            main()
        elif ask == 'n':
            print('Okay, the game is over...')
            exit(0)


# main function that runs the starting stage of the game
def main():
    numOfCells = int(input('Please enter the number of cells to fill[0-80]\n'))
    if 0 <= numOfCells <= 80:
        board = createEmptyBoard()
        sudokuGenerator(board, numOfCells)

    while numOfCells not in range(0, 81):
        print('Error: invalid number of cells to fill')
        numOfCells = int(input('Please enter the number of cells to fill[0-80]\n'))
        if numOfCells in range(0, 81):
            board = createEmptyBoard()
            sudokuGenerator(board, numOfCells)
            break


if __name__ == '__main__':
    main()
