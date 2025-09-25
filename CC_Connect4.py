## Functions ##
# printBoard(board): displays game board
def printBoard(board):

    for i in range(len(board)): # rows
        print(f"| {len(board) - i} | {board[i][0]} | {board[i][1]} | {board[i][2]} | {board[i][3]} | {board[i][4]} | {board[i][5]} | {board[i][6]} |")
        print("-" * 33)
    print("|R/C| a | b | c | d | e | f | g |")
    print("-" * 33)


# resetBoard(board): initializes and resets the game board
def resetBoard():
    board = [[" ", " ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " ", " "],]
    return board

# availablePositions(board): returns list of all available positions
def availablePositions(board):

    positions = [" ", " ", " ", " ", " ", " ", " "] # stores all available positions in one row
    col_letters = ["a", "b", "c", "d", "e", "f", "g"] # to connect the column number

    # Looping through every position
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == " ":
                positions[j] = col_letters[j] + str(len(board) - i) # keeps adding positions until a space is filled

    return positions

# validateEntry(positions, entry, board): returns True if the user entered inputs are valid, otherwise False
def validateEntry(positions, entry, board):
    positions = availablePositions(board)
    if entry in positions:
        return True

    # Invalid entry
    print("Invalid entry: try again.\n")
    return False

# checkFull(board): returns True if the board is full, otherwise False
def checkFull(board):
    # Looping through board
    for i in range(len(board)): # rows
        for j in range(len(board[0])): # cols
            if board[i][j] == " ": # returns false for any empty space
                return False
    # went through whole loop, no empty space
    return True


# checkWin(board, turn): returns True when X or O becomes winner, otherwise False
def checkWin(board, mark):
    row_cols = []

    for i in range(len(board)): # row
        for j in range(len(board[0])): # col
            if board[i][j] == mark:
                row_cols.append([i, j]) # storing all places turn has occupied
    
    if len(row_cols) <= 4: # Needs to have at least 4 marks
        return False

    for x,y in row_cols:
        # Row checking
        count = 0
        for i in range(4):
            if [x+i, y] in row_cols:
                count += 1
            else:
                break
        if count == 4:
            print(f"{mark} IS THE WINNER!!!")
            return True

        # Column checking
        count = 0
        for i in range(4):
            if [x, y+i] in row_cols:
                count += 1
            else:
                break
        if count == 4:
            print(f"{mark} IS THE WINNER!!!")
            return True
        
        # Diagonal down-right
        count = 0
        for i in range(4):
            if [x+i, y+i] in row_cols:
                count += 1
            else:
                break
        if count == 4:
            print(f"{mark} IS THE WINNER!!!")
            return True

        # Diagonal down-left
        count = 0
        for i in range(4):
            if [x+i, y-i] in row_cols:
                count += 1
            else:
                break
        if count == 4:
            print(f"{mark} IS THE WINNER!!!")
            return True
        
    return False



def main():
 ## Start of game ##
    game = 'y'
    col_letters = ["a", "b", "c", "d", "e", "f", "g"]

    while game.lower() == 'y':
        # Initializing board, new game
        turn = 1
        board = resetBoard()
        print("New Game: X goes first.")
        print()
        printBoard(board)
        board_win = False

        while board_win != True:
            if turn == 1:
                mark = "X"
            else:
                mark = "O"

            # Validating entry
            entry = False
            while entry != True:
                print(f"{mark}'s turn.")
                print(f"Where do you want your {mark} placed?")
                positions = availablePositions(board)
                print(f"Available positions are: {positions}\n")
                row_col = input("Please enter column-letter and row-number (e.g., a1): ")
                entry = validateEntry(positions, row_col, board)

            # Converting entry into row col vals
            print("Thank you for your selection.")
            col = col_letters.index(row_col[0])
            row = len(board) - int(row_col[1])

            # Inputting mark and checking board
            board[row][col] = mark
            board_win = checkWin(board, mark)
            board_full = checkFull(board)
            if board_full == True:
                print("\nDRAW! NOBODY WINS!\n")
                printBoard(board)
                break
            printBoard(board)
            turn *= -1
        
        game = input("Another game? (y/n)?").lower()
    print("Thank you for playing!")

    
if __name__ == '__main__':
    main()