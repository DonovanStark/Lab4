# drs474@nau.edu and rng49@nau.edu
import random
light_square = u'\u25A0'
dark_square = u'\u25A1'
alphabet = "abcdefghijklmnopqrstuvwxy"
print(light_square)
def Generate_Game():
    row0 = []
    row1 = []
    row2 = []
    row3 = []
    row4 = []
    for i in range(5):
        slot = random.randint(0,1)
        if slot == 1:
            slot = light_square            
            row0 += [slot]
        else:
            slot = dark_square
            row0 += [slot]
    for i in range(5):
        slot = random.randint(0,1)
        if slot == 1:
            slot = light_square            
            row1 += [slot]
        else:
            slot = dark_square
            row1 += [slot]
        
    for i in range(5):
        slot = random.randint(0,1)
        if slot == 1:
            slot = light_square            
            row2 += [slot]
        else:
            slot = dark_square
            row2 += [slot]


    for i in range(5):
        slot = random.randint(0,1)
        if slot == 1:
            slot = light_square            
            row3 += [slot]
        else:
            slot = dark_square
            row3 += [slot]
    
    for i in range(5):
        slot = random.randint(0,1)
        if slot == 1:
            slot = light_square            
            row4 += [slot]
        else:
            slot = dark_square
            row4 += [slot]


    grid = [row0,row1,row2,row3,row4]
    return grid 

grid = Generate_Game()

def play_game():
    inpt_row = int(input("Select ROW(0-4): "))
    inpt_column = int(input("Select COLUMN(0-4): "))
    inpt = [inpt_row,inpt_column]
    return inpt

def update_grid(inpt,grid):
        row = inpt[0]
        column = inpt[1]
        print(row,column)
        if grid[row][column] == dark_square:
            grid[row][column] = light_square
        else:
            grid[row][column] = dark_square
        
        if row != 0 and row != 4 and column != 0 and column != 4:
             
            if grid[row+1][column] == dark_square:
                grid[row+1][column] = light_square
            else:
                grid[row+1][column] = dark_square
        
            if grid[row-1][column] == dark_square:
                grid[row-1][column] = light_square
            else:
                grid[row-1][column] = dark_square

            if grid[row][column+1] == dark_square:
                grid[row][column+1] = light_square
            else:
                grid[row][column+1] = dark_square

            if grid[row][column-1] == dark_square:
                grid[row][column-1] = light_square
            else:
                grid[row][column-1] = dark_square
        
        
        elif row == 4 and column == 4:
            
                if grid[row-1][column] == dark_square:
                    grid[row-1][column] = light_square
                else:
                    grid[row-1][column] = dark_square

                if grid[row][column-1] == dark_square:
                    grid[row][column-1] = light_square
                else:
                    grid[row][column-1] = dark_square
        
        elif row == 0 and column == 0:
               
                if grid[row+1][column] == dark_square:
                    grid[row+1][column] = light_square
                else:
                    grid[row+1][column] = dark_square

                if grid[row][column+1] == dark_square:
                    grid[row][column+1] = light_square
                else:
                    grid[row][column+1] = dark_square


                
        elif row == 0 and column == 4:

                if grid[row+1][column] == dark_square:
                    grid[row+1][column] = light_square
                else:
                    grid[row+1][column] = dark_square

                if grid[row][column-1] == dark_square:
                    grid[row][column-1] = light_square
                else:
                    grid[row][column-1] = dark_square
    
        elif row == 4 and column ==0:

                if grid[row-1][column] == dark_square:
                    grid[row-1][column] = light_square
                else:
                    grid[row-1][column] = dark_square

        
                if grid[row][column+1] == dark_square:
                    grid[row][column+1] = light_square
                else:
                    grid[row][column+1] = dark_square


        elif row == 0 or row == 4:
            
            if row ==  0: 
            
                if grid[row+1][column] == dark_square:
                    grid[row+1][column] = light_square
                else:
                    grid[row+1][column] = dark_square

                if grid[row][column+1] == dark_square:
                    grid[row][column+1] = light_square
                else:
                    grid[row][column+1] = dark_square

                if grid[row][column-1] == dark_square:
                    grid[row][column-1] = light_square
                else:
                    grid[row][column-1] = dark_square
            
            else:
                
                if grid[row-1][column] == dark_square:
                    grid[row-1][column] = light_square
                else:
                    grid[row-1][column] = dark_square

                if grid[row][column+1] == dark_square:
                    grid[row][column+1] = light_square
                else:
                    grid[row][column+1] = dark_square

                if grid[row][column-1] == dark_square:
                    grid[row][column-1] = light_square
                else:
                    grid[row][column-1] = dark_square

        else:
            
            if column == 0: 
                if grid[row+1][column] == dark_square:
                    grid[row+1][column] = light_square
                else:
                    grid[row+1][column] = dark_square
        
                if grid[row-1][column] == dark_square:
                    grid[row-1][column] = light_square
                else:
                    grid[row-1][column] = dark_square

                if grid[row][column+1] == dark_square:
                    grid[row][column+1] = light_square
                else:
                    grid[row][column+1] = dark_square

            else:
                
                if grid[row+1][column] == dark_square:
                    grid[row+1][column] = light_square
                else:
                    grid[row+1][column] = dark_square
        
                if grid[row-1][column] == dark_square:
                    grid[row-1][column] = light_square
                else:
                    grid[row-1][column] = dark_square

                if grid[row][column-1] == dark_square:
                    grid[row][column-1] = light_square
                else:
                    grid[row][column-1] = dark_square
        
        return grid
    





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

def solvable(grid):
    pass


solvable(grid)

def solve_bot():
    row = random.randint(0,4)
    column = random.randint(0,4)
    inpt = [row,column]
    return inpt
s = 1
while s == 1:
    for i in range(5):
        print(grid[i])
    
    inpt = solve_bot()
    grid = update_grid(inpt,grid)
    s = check_grid(grid)

