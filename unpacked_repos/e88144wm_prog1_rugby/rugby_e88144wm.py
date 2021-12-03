import os
import argparse

# handels the command line arguments, turns them into varibales
parser = argparse.ArgumentParser()
parser.add_argument('inputPath', type=str)
parser.add_argument('outputPath', type=str)
args = parser.parse_args()

# sets variables to the input and output path specified by the user
inpPath = args.inputPath
outPath = args.outputPath

# dictionary for scoring
scoring = {
    "t": 5,
    "c": 2,
    "p": 3,
    "d": 3
}

# function to get score for a input file
def get_score(filePath):
    # gets text from file
    file = open(filePath, 'r')
    txt = file.read()
    file.close()

    # initialises varibales used in loop
    t1Scr, t2Scr = 0, 0
    loops = int(len(txt) / 3)
    pointer = 0
    
    # Loops through every 3 characters of input string
    for i in range(0, loops):
        event = txt[pointer:pointer+3]
        points = scoring[event[2]]

        if event[0:2] == 'T1':
            t1Scr += points
        else:
            t2Scr += points
        
        pointer += 3
    return str(t1Scr) + ':' + str(t2Scr)


# looping through files
for name in os.listdir(inpPath):
    score = get_score(inpPath + '/' +name)

    name = name[:-4] + "_e88144wm.txt"
    outputFile = open(outPath + '/' + name, 'a')
    outputFile.write(score)
    outputFile.close()

