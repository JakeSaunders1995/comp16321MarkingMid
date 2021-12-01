import argparse as pa
import os

parser = pa.ArgumentParser()
parser.add_argument("inputpath", type=str)
parser.add_argument("outputpath", type=str)
args = parser.parse_args()
InputPath = args.inputpath
OutputPath = args.outputpath

dirs = os.listdir(InputPath)
for file in dirs:
    fileLocation = InputPath + '/' + file
    readfile = open(fileLocation, 'r')
    inputLine = readfile.read()
    readfile.close()

    T1score = 0
    T2score = 0
    times = len(inputLine) / 3
    position = 0
    for i in range(int(times)):
        position += 1
        if inputLine[position] == '1':
            position += 1
            if inputLine[position] == 't':
                T1score += 5
            elif inputLine[position] == 'c':
                T1score += 2
            elif inputLine[position] == 'p' or inputLine[position] == 'd':
                T1score += 3
        elif inputLine[position] == '2':
            position += 1
            if inputLine[position] == 't':
                T2score += 5
            elif inputLine[position] == 'c':
                T2score += 2
            elif inputLine[position] == 'p' or inputLine[position] == 'd':
                T2score += 3
        position += 1
    fileWithoutTxt = file[0:len(file)-4]
    fileLocation = OutputPath + '/' + fileWithoutTxt + '_j24834et.txt'
    readfile = open(fileLocation, 'w')
    readfile.write(str(T1score)+':'+str(T2score))
    readfile.close()