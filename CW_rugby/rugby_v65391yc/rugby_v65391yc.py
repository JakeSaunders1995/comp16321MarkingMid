import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('inputPath', type=str)
parser.add_argument('outputPath', type=str)
args = parser.parse_args()

fileList = os.listdir(args.inputPath)

def rugby(input):
    t1 = 0
    t2 = 0

    for item in input:
        if item == '1':
            team = 1
        elif item == '2':
            team = 2
        elif item == 't':
            if team == 1:
                t1 = t1 + 5
            elif team == 2:
                t2 = t2 + 5
        elif item == 'c':
            if team == 1:
                t1 = t1 + 2
            elif team == 2:
                t2 = t2 + 2
        elif item == 'p' or item == 'd':
            if team == 1:
                t1 = t1 + 3
            elif team == 2:
                t2 = t2 + 3

    result = str(t1) + ':' + str(t2)
    return result

def changeName(inputName):
    nameList = list(inputName)
    nameList.insert(-4, '_v65391yc')
    outputName = ''.join(nameList)
    return outputName

for file in fileList:
    inputPath = args.inputPath + '/' + file
    openFile = open(inputPath)
    content = openFile.read()
    
    outputPath = args.outputPath + '/' + changeName(file)

    newFile = open(outputPath, 'w')
    newFile.write(str(rugby(content)))
    newFile.close()
    openFile.close()
