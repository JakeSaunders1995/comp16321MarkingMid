import argparse
import os

parser = argparse.ArgumentParser(description='Get locations')
parser.add_argument('inputlocation', type=str)
parser.add_argument('outputlocation', type=str)
args = parser.parse_args()

def getFile(location):
    f = open(location, "r")
    text = f.read()
    f.close()
    return text


def getPointsT1(string):
    count = 0
    for i in range(len(string)):
        if string[i] == 'T' and string[i+1] == '1':
            i += 2
            if(string[i] == 't'):
                count += 5
            if (string[i] == 'c'):
                count += 2
            if (string[i] == 'p'):
                count += 3
            if (string[i] == 'd'):
                count += 3
    return count


def getPointsT2(string):
    count = 0
    for i in range(len(string)):
        if string[i] == 'T' and string[i + 1] == '2':
            i += 2
            if (string[i] == 't'):
                count += 5
            if (string[i] == 'c'):
                count += 2
            if (string[i] == 'p'):
                count += 3
            if (string[i] == 'd'):
                count += 3
    return count


def writeFile(location, result):
    f = open(location, 'w')
    f.write(result)
    f.close()


fileLocation = args.inputlocation
outputFileLocation = args.outputlocation

list = os.listdir(fileLocation)
for name in list:
    newloc = fileLocation+"/"+name
    Case = getFile(newloc)
    T1Points = getPointsT1(Case)
    T2Points = getPointsT2(Case)
    FinRes = str(T1Points) + ":" + str(T2Points)
    newout = outputFileLocation+"/"+name
    newout = newout.replace(".txt", "_t74769sm.txt")
    writeFile(newout, FinRes)