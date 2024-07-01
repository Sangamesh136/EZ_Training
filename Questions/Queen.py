"""
# Each row can only have 1 Queen
# L-U-D, up, rud
# func(board, row)
safePosition => position of queen where there is no another queen in the diagonal, above it and in the same row

    if row == n
        print(board)
        return
for col in range(0, n):
    if safePosition(board, row,col) ==  True
        board[row][col] = 1
        fun(board, row+1)
    board[row][col] = 0

"""
def printBoard(board):
    return

def safePosition(board, row, col):
    
def find_(board, row):
    n = len(board)
    if row == n:
        printBoard(board)
    for col in range(0,n):
        if safePosition(board, row, col) == True
            board[row][col] = 1
            find_(board, row+1)
    board[row][col] = 0

board = [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]
find_(board, 0)
