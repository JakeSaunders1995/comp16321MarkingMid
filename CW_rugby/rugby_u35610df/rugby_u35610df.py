import sys
import os

inputFolder = sys.argv[1]
outputFolder = sys.argv[2]
scoreDict = {"tScore": 5, 'cScore': 2, 'pScore': 3, 'dScore': 3}

def rugbyScore(string1, filename):
    stringSplit = string1.split('T')
    print(stringSplit)
    for item in stringSplit:
        try:
            stringSplit.remove("")
        except:
            print('not empty')
            pass
        print(stringSplit)

    player1 = 0
    player2 = 0

    for each in stringSplit:
        if each[0] == '1':
            player1 += scoreDict[(str(each[1]) + 'Score')]
        elif each[0] == '2':
            player2 += scoreDict[(str(each[1]) + 'Score')]
        else:
            print('there are supposed to be only 2 teams...')
            break
    print(f'{player1 = } and {player2 = }')

    outputFilePath = outputFolder + '/' + filename.rstrip('.txt') + '_u35610df.txt'
    outputFile = open(outputFilePath, 'w')
    outputFile.write(f'{player1}:{player2}')
    outputFile.close()



for each in os.listdir(inputFolder):
    filename = each
    filePath = inputFolder + '/' + filename
    inputFile = open(filePath, 'r')
    string = "".join(inputFile.readlines())
    rugbyScore(string, filename)
    inputFile.close()






# inputFile = open(inputFilePath, 'r')
# outputFile = open(outputFilePath, 'w')

# inputLines = inputFile.readlines()
# print(inputLines)

# string1 = ''.join(inputLines)






# firstScorer = string1[0:2]
# print(firstScorer)

# stringSplit = string1.split("T1")
# finalStringList = []
# for each in stringSplit:
#     print(f"{each = }")
#     tmpString = each.split("T2")

    
#     for listItem in tmpString:
#         finalStringList.append(listItem)
    
# print(stringSplit)
# print(finalStringList)


# for item in finalStringList:
#     try:
#         finalStringList.remove("")
#     except:
#         print('not empty')
#         pass
#     print(finalStringList)

# if firstScorer == 'T1':
#     player1 = True

# for char in string1:



    


