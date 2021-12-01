import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("in_path", type=str)
parser.add_argument("out_path", type=str)
args = parser.parse_args()
inPath = str(args.in_path).rstrip("/")
outPath = str(args.out_path).rstrip("/")

# Main
for fileName in os.listdir(inPath):
    inFile = open(inPath + "/" + fileName, "r") 
    outFile = open(outPath + "/" + fileName[0:-4] + "_p72426yp.txt", "w") 

    s = inFile.read().rstrip("\n")
    t1Score = 0; t2Score = 0

    scoring = {
            't': 5,
            'c': 2,
            'p': 3,
            'd': 3
        }

    for i in range(0, len(s), 3):
        if (s[i+1] == '1'):
           t1Score += scoring[s[i+2]]
        else:
           t2Score += scoring[s[i+2]] 

    outFile.write(str(t1Score)+":"+str(t2Score))

    inFile.close()
    outFile.close()

