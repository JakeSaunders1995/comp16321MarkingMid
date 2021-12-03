import argparse
import os

def scoreTypes(stype):
    result = 0
    if stype == 't':
        result = 5
    elif stype == 'c':
        result = 2
    elif stype == 'p' or stype == 'd':
        result = 3
    
    return result

#Command Line Arguments
parser = argparse.ArgumentParser()
parser.add_argument('inputFolder',type=str)
parser.add_argument('outputFolder', type=str)
args = parser.parse_args()

for j in range (len(os.listdir(args.inputFolder))):
    if (os.listdir(args.inputFolder)[j].__contains__(".txt")):
        iFile = open(os.path.join(args.inputFolder, os.listdir(args.inputFolder)[j]), "r")
        scores = iFile.read()

        t1score = 0
        t2score = 0
        currentTeam = ""
        for i in range(len(scores)):
            if scores[i] == '1':
                currentTeam = '1'
            elif scores[i] == '2':
                currentTeam = '2'

            if i % 3 == 2:
                scoreToAdd = scoreTypes(scores[i])
                if currentTeam == '1':
                    t1score += scoreToAdd
                elif currentTeam == '2':
                    t2score += scoreToAdd
        iFile.close()

        outputFileName = os.listdir(args.inputFolder)[j].replace(".txt","") + "_y78202oa.txt"
        pathToSave = os.path.join(args.outputFolder, outputFileName)
        oFile = open(pathToSave, "w+")
        oFile.write(str(t1score) + ":" + str(t2score))
        oFile.close()



