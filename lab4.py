# drs474@nau.edu and rng49@nau.edu
import random
light_square = u'\u25A0'
dark_square = u'\u25A1'
alphabet = "abcdefghijklmnopqrstuvwxy"
print("In order to win remove all:'\u25A0'")

# represent the board as a list of lists
row0 = [dark_square, dark_square, dark_square, dark_square, dark_square]
row1 = [dark_square, dark_square, dark_square, dark_square, dark_square]
row2 = [dark_square, dark_square, dark_square, dark_square, dark_square]
row3 = [dark_square, dark_square, dark_square, dark_square, dark_square]
row4 = [dark_square, dark_square, dark_square, dark_square, dark_square]
grid = [row0, row1, row2, row3, row4]
blank_grid = grid


# randomize the board
def make_init_board():
    row = random.randint(0, 4)
    column = random.randint(0, 4)
    inpt = [row, column]
    return inpt


# prompt the user to select rows and columns
def play_game():
    j = 1
# While loop checks user input to make sure it is an int 0-4
# If user input is not 0-4 asks again
    while j == 1:
        counter1 = 0
        counter2 = 0
        inpt_row = input("Select ROW(0-4): ")
        inpt_column = input("Select COLUMN(0-4): ")
        for i in range(5):
            if inpt_row != str(i):
                counter1 += 1
            if inpt_column != str(i):
                counter2 += 1
        if counter1 < 5 and counter2 < 5:
            j = 0
        else:
            j = 1
            print("Row and Column must be integer 0-4")
    inpt = [int(inpt_row), int(inpt_column)]
    return inpt


# change grid when row and columnn are selected
def update_grid(inpt, grid):
    row = inpt[0]
    column = inpt[1]
    if grid[row][column] == dark_square:
        grid[row][column] = light_square
    else:
        grid[row][column] = dark_square

    if row != 0 and row != 4 and column != 0 and column != 4:

        if grid[row + 1][column] == dark_square:
            grid[row + 1][column] = light_square
        else:
            grid[row + 1][column] = dark_square

        if grid[row - 1][column] == dark_square:
            grid[row - 1][column] = light_square
        else:
            grid[row - 1][column] = dark_square

        if grid[row][column + 1] == dark_square:
            grid[row][column + 1] = light_square
        else:
            grid[row][column + 1] = dark_square

        if grid[row][column - 1] == dark_square:
            grid[row][column - 1] = light_square
        else:
            grid[row][column - 1] = dark_square

    elif row == 4 and column == 4:

        if grid[row - 1][column] == dark_square:
            grid[row - 1][column] = light_square
        else:
            grid[row - 1][column] = dark_square

        if grid[row][column - 1] == dark_square:
            grid[row][column - 1] = light_square
        else:
            grid[row][column - 1] = dark_square

    elif row == 0 and column == 0:

        if grid[row + 1][column] == dark_square:
            grid[row + 1][column] = light_square
        else:
            grid[row + 1][column] = dark_square

        if grid[row][column + 1] == dark_square:
            grid[row][column + 1] = light_square
        else:
            grid[row][column + 1] = dark_square

    elif row == 0 and column == 4:

        if grid[row + 1][column] == dark_square:
            grid[row + 1][column] = light_square
        else:
            grid[row + 1][column] = dark_square

        if grid[row][column - 1] == dark_square:
            grid[row][column - 1] = light_square
        else:
            grid[row][column - 1] = dark_square

    elif row == 4 and column == 0:

        if grid[row - 1][column] == dark_square:
            grid[row - 1][column] = light_square
        else:
            grid[row - 1][column] = dark_square

        if grid[row][column + 1] == dark_square:
            grid[row][column + 1] = light_square
        else:
            grid[row][column + 1] = dark_square

    elif row == 0 or row == 4:

        if row == 0:

            if grid[row + 1][column] == dark_square:
                grid[row + 1][column] = light_square
            else:
                grid[row + 1][column] = dark_square

            if grid[row][column + 1] == dark_square:
                grid[row][column + 1] = light_square
            else:
                grid[row][column + 1] = dark_square

            if grid[row][column - 1] == dark_square:
                grid[row][column - 1] = light_square
            else:
                grid[row][column - 1] = dark_square

        else:

            if grid[row - 1][column] == dark_square:
                grid[row - 1][column] = light_square
            else:
                grid[row - 1][column] = dark_square

            if grid[row][column + 1] == dark_square:
                grid[row][column + 1] = light_square
            else:
                grid[row][column + 1] = dark_square

            if grid[row][column - 1] == dark_square:
                grid[row][column - 1] = light_square
            else:
                grid[row][column - 1] = dark_square

    else:

        if column == 0:
            if grid[row + 1][column] == dark_square:
                grid[row + 1][column] = light_square
            else:
                grid[row + 1][column] = dark_square

            if grid[row - 1][column] == dark_square:
                grid[row - 1][column] = light_square
            else:
                grid[row - 1][column] = dark_square

            if grid[row][column + 1] == dark_square:
                grid[row][column + 1] = light_square
            else:
                grid[row][column + 1] = dark_square

        else:

            if grid[row + 1][column] == dark_square:
                grid[row + 1][column] = light_square
            else:
                grid[row + 1][column] = dark_square

            if grid[row - 1][column] == dark_square:
                grid[row - 1][column] = light_square
            else:
                grid[row - 1][column] = dark_square

            if grid[row][column - 1] == dark_square:
                grid[row][column - 1] = light_square
            else:
                grid[row][column - 1] = dark_square

    return grid


p = 1
while p == 1:
    for _ in range(100):
        inpt = make_init_board()
        grid = update_grid(inpt, grid)
    if grid == blank_grid:
        p = 0
    else:
        p = 1


def check_grid(grid):
    for i in range(5):
        if light_square == grid[0][i]:
            return 1

    for i in range(5):
        if light_square == grid[1][i]:
            return 1

    for i in range(5):
        if light_square == grid[2][i]:
            return 1

    for i in range(5):
        if light_square == grid[3][i]:
            return 1
    for i in range(5):
        if light_square == grid[4][i]:
            return 1
    return 0


moves = 0
s = 1
while s == 1:
    for i in range(5):
        print(grid[i])
    print("Moves:" + str(moves))
    inpt = play_game()
    grid = update_grid(inpt, grid)
    gg = check_grid(grid)
    moves += 1
    if gg == 0:
        print("Congratulations!You won in "+str(moves)+" moves.")
        a = input("Would you like to play again?(y/n): ").lower()
        if a == "y" or a == "yes":
            for _ in range(100):
                inpt = make_init_board()
                grid = update_grid(inpt, grid)
            moves = 0
            s = 1
        else:
            s = 0
