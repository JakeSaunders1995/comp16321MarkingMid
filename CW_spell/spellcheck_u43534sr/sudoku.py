import math

# Defining the sudoku grid
sudoku = [
    [7,0,0,0,3,4,8,0,0],
    [8,0,4,6,0,0,0,0,0],
    [0,3,9,0,5,0,0,0,0],
    [1,0,0,5,0,0,6,0,0],
    [0,4,0,7,0,9,0,3,0],
    [0,0,3,0,0,8,0,0,9],
    [0,0,0,0,7,0,3,2,0],
    [0,2,6,0,0,1,9,0,5],
    [0,0,7,9,2,0,0,0,4]
]

size = len(sudoku)

# Printing the sudou grid
print("Unsolved Sudoku: ")
for row in range(size):
    print(sudoku[row])

# Getting the dimentions of each small box
area = int(math.sqrt(size))

gridUpdated = True
while (gridUpdated):
    gridUpdated = False
    # Searching for a target value
    for target in range(1, size + 1):
        row = 0
        while (row < size):
            column = 0
            while (column < size):
                targetFound = False
                for r in range(row, row + area):
                    for c in range(column, column + area):
                        if (sudoku[r][c] == target):
                            targetFound = True
                            break
                if not targetFound:
                    placeTargetAt = []
                    for r in range(row, row + area):
                        for c in range(column, column + area):
                            if (sudoku[r][c] == 0):
                                currentRow = sudoku[r]
                                currentColumn = [item[c] for item in sudoku]
                                if (target not in currentRow and target not in currentColumn):
                                    placeTargetAt.append([r,c])
                    if (len(placeTargetAt) == 1):
                        sudoku[placeTargetAt[0][0]][placeTargetAt[0][1]] = target
                        # for rows in range(size):
                        #     print (sudoku[rows])
                        gridUpdated = True
                column += area
            row += area
    for _row_ in range(0, size):
        if (0 in sudoku[_row_]):
            for _col_ in range(0, size):
                if (sudoku[_row_][_col_] == 0):
                    currentRowValues = sudoku[_row_]
                    currentColValues = [item[_col_] for item in sudoku]
                    validChoices = []
                    for n in range(1, size + 1):
                        if n not in currentRowValues and n not in currentColValues:
                            validChoices.append([_row_, _col_, n])
                    if len(validChoices) == 1:
                        x = validChoices[0][0]
                        y = validChoices[0][1]
                        n = validChoices[0][2]
                        sudoku[x][y] = n
                        gridUpdated = True

print("\n\nSolved Sudoku:")
for _rows_ in range(size):
    print(sudoku[_rows_])
