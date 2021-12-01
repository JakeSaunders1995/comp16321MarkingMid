import argparse
import os

parser = argparse.ArgumentParser(description = 'Path')
parser.add_argument('inputpath', type=str, help='input file path')
parser.add_argument('outputpath', type=str, help='output file path')
args = parser.parse_args()

InputPath = args.inputpath
OutputPath = args.outputpath
dirs1 = os.listdir(args.inputpath)


for filein in dirs1:
    f = open(InputPath + "/" + filein)
    input = f.readline()
    T1 = 0
    T2 = 0
    for i in range(0,len(input),3):
        if input[i:i+2] == "T1":
            if input[i+2] == "t":
                T1 += 5
            elif input[i+2] == "c":
                T1 += 2
            elif input[i+2] == "p":
                T1 += 3
            elif input[i+2] == "d":
                T1 += 3
        if input[i:i+2] == "T2":
            if input[i+2] == "t":
                T2 += 5
            elif input[i+2] == "c":
                T2 += 2
            elif input[i+2] == "p":
                T2 += 3
            elif input[i+2] == "d":
                T2 += 3
    Score = str(T1) + ":" + str(T2)
    
    ff = open(OutputPath + "/" + filein[:-4] + "_j95271zf.txt","w")
    ff.write(Score)
    ff.close()
    f.close()
