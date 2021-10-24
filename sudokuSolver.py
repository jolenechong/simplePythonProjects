"""
Solving Sudoku Problems with Backtracking algorithm
"""

boardList = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print('\n- - - - - - - - - - - - - - - ')

        print("")

        for num in range(len(board[i])):
            if num % 3 == 0 and num != 0:
                print('|', end="")

            print("" ,board[i][num], end=" ")

def pickEmpty(board):
    for i in range(len(board)):
        for p in range(len(board[0])):
            if board[i][p] == 0:
                return (i,p)  # return row and column (of num that shld be guessed)
    return None

def valid(board, num, pos):
    for rowNum in range(len(board[0])):
        # for each row we check if anyth same
        if board[pos[0]][rowNum] == num and pos[1] != rowNum:
            # if any of the board rows number is the number u entered or boards column number same  as the num u entered
            # ignore current position number cus it will be 0
            return False

    for colNum in range(len(board)):
        # for each column we check if anyth same
        if board[colNum][pos[1]] == num and pos[0] != colNum:
            return False

    # check box
    box_x = pos[1] // 3 #will only return 1 2 3 which will tell u which box
    box_y = pos[0] // 3 #will only return 1 2 3 which will tell u which box

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    # return true if everyth runs smoothly wihtout returning False
    return True
# valid(boardList, 1, (0,2))

def solve(board):
    find = pickEmpty(board)

    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(board, i, (row, col)):
            # if you get a valid num that works, add to board
            board[row][col] = i

            if solve(board):
                return True

            # reset bcs last element cant be correct
            board[row][col] = 0

    return False
print('original')
print_board(boardList)
solve(boardList)
print('\nsolved')
print_board(boardList)