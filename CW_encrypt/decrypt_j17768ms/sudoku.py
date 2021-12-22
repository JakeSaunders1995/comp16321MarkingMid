import math
sudokuGrid = [
[0,0,0,1],
[0,2,0,0],
[0,0,4,0],
[3,0,0,0]
]
size = len(sudokuGrid)
print("Sudoku grid size is ", size, " by ", size)
for row in range(size):
    print(sudokuGrid[row])
area = int(math.sqrt(size))
print("Size of each area is: ",area,"by",area)

gridUpdated=True
while(gridUpdated):
    gridUpdated=False
    for target in range(1,size+1):
        row = 0
        while (row < size):
            col = 0
            while (col < size):
                print("\nChecking the following area for target value: ", target)
                print("start row: ",row)
                print("end row: ", row + area -1)
                print("start sol: ",col)
                print("end col: ", col + area -1)
                print()

                print("Looking for ", target)
                foundTarget= False
                for r in range(row, row + area):
                    for c in range(col, col + area):
                        print("Checking - Row: ", r," Column: ", c, end="")
                        if (sudokuGrid[r][c]==target):
                            print("Target is already in area")
                            foundTarget=True
                            break
                        else:
                            print(" - Not here")
                print("The target value ",target,end="")
                if not foundTarget:
                    print(" was not in area")
                    placeTargetAt = []
                    for r in range(row, row+area):
                        for c in range(col, col+area):
                            print("Checking row ",r ," column", c)
                            if (sudokuGrid[r][c] == 0):
                                print("Square available")
                                #Get current values for this row
                                currentRowValues = sudokuGrid[r]
                                #and values for the column
                                currentColValues=[item[c] for item in sudokuGrid]
                                print ("Row contains", currentRowValues)
                                print ("Col contains", currentColValues)
                                if target not in currentRowValues and target not in currentColValues:
                                    print("Could place ",target," at,(",r,",",c,")")
                                    placeTargetAt.append([r,c])
                    if (len(placeTargetAt)==1):
                        print ("placed ",target," at", placeTargetAt[0][0], " x ", placeTargetAt[0][1])
                        sudokuGrid[placeTargetAt[0][0]][placeTargetAt[0][1]]=target
                        gridUpdated = True
                else:
                    print(" was found in area")
                col+=area
            row+= area
        print("Looking for ", target)
        print("Checking - Row: ",r,"Column: ",c,end="")
    else:
        print(" - Not here")
for row in range(size):
    print(sudokuGrid[row])