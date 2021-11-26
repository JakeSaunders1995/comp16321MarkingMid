import os, sys
import re

# save final score result in right format
def saveScore(inFile, T1, T2):
    # create output folder if it does not exist
    if not os.path.exists(sys.argv[2]):
        print("FOLDER CREATED")
        os.makedirs(sys.argv[2])

    outScore = str(T1) + ":" + str(T2)
    outFile = inFile.replace(".txt", "_f63279ma.txt")

    resultFile = open(sys.argv[2] + "/" + outFile, "w")
    resultFile.write(outScore)
    resultFile.close()


files = os.listdir(sys.argv[1])
for file in files:
    print("File: " + file)
    scoresFile = open(sys.argv[1] + "/" + file)
    scores = scoresFile.read()

    T1, T2 = 0, 0
    
    result = re.findall("T1t", scores) # find all occurances of T1t
    T1 += (len(result) * 5)
    result = re.findall("T1c", scores)
    T1 += (len(result) * 2)
    result = re.findall("T1p", scores)
    T1 += (len(result) * 3)
    result = re.findall("T1d", scores)
    T1 += (len(result) * 3)

    result = re.findall("T2t", scores)
    T2 += (len(result) * 5)
    result = re.findall("T2c", scores)
    T2 += (len(result) * 2)
    result = re.findall("T2p", scores)
    T2 += (len(result) * 3)
    result = re.findall("T2d", scores)
    T2 += (len(result) * 3)


    # WINNER
    if (T1 > T2):
        print("Winner is T1!")
    elif (T1 < T2):
        print("Winner is T2!")
    else:
        print("Draw!")

    print()
    scoresFile.close()
    
    saveScore(file, T1, T2)