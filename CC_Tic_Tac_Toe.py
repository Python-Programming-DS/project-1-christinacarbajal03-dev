
## Functions ##

# printBoard(board): displays game board (3x3 matrix)
def printBoard(board):
    print("-" * 17)
    print("|R\\C| 0 | 1 | 2 |")

    for i in range(len(board)): # rows
        print("_" * 17)
        print(f"| {i} | {board[i][0]} | {board[i][1]} | {board[i][2]} |") # prints each row of the board
    print("_" * 17)
    print()

# resetBoard(board): initializes and resets the game board
def resetBoard():
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]
    return board

# validateEntry(row, col, board): returns True if the user entered inputs are valid, otherwise False
def validateEntry(row, col, board):

    # Looping through board
    if row in range(len(board)): # rows
        if col in range(len(board[0])): # cols
            if board[row][col] == " ": # Empty space, valid entry
                return True
            else: # Non empty space, invalid entry
                print("That cell is already taken.")
                print("Please make another selection.\n")
                return False          
    
    # row or col not in range, invalid entry
    print("Invalid entry: try again.")
    print("Row & column numbers must be either 0, 1, or 2.\n")
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
    
    if len(row_cols) <= 2: # Needs to have at least 3 marks
        return False

    for x,y in row_cols:
        # Row checking
        count = 0
        for i in range(3):
            if [x+i, y] in row_cols:
                count += 1
            else:
                break
        if count == 3:
            print(f"{mark} IS THE WINNER!!!")
            return True

        # Column checking
        count = 0
        for i in range(3):
            if [x, y+i] in row_cols:
                count += 1
            else:
                break
        if count == 3:
            print(f"{mark} IS THE WINNER!!!")
            return True
        
        # Diagonal down-right
        count = 0
        for i in range(3):
            if [x+i, y+i] in row_cols:
                count += 1
            else:
                break
        if count == 3:
            print(f"{mark} IS THE WINNER!!!")
            return True

        # Diagonal down-left
        count = 0
        for i in range(3):
            if [x+i, y-i] in row_cols:
                count += 1
            else:
                break
        if count == 3:
            print(f"{mark} IS THE WINNER!!!")
            return True
        
    return False


def main():
    ## Start of game ##
    game = 'y'

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
                row_col = input("Please enter row number and column number separated by a comma.\n")
                row_col = row_col.split(",")
                row = int(row_col[0])
                col = int(row_col[1])
                print(f"You have entered row #{row} and column #{col}")
                entry = validateEntry(row, col, board)
            print("Thank you for your selection.")
            board[row][col] = mark
            board_win = checkWin(board, mark)
            board_full = checkFull(board)
            if board_full == True:
                print("\nDRAW! NOBODY WINS!\n")
                printBoard(board)
                break
            printBoard(board)
            turn *= -1
        
        game = input("Another game? Enter Y or y for yes.\n").lower()
    print("Thank you for playing!")


if __name__ == '__main__':
    main()