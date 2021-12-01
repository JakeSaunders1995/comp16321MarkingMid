import argparse
import glob
import os
import sys

parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("output")
args = parser.parse_args()

file = os.path.join(args.input, "*")
filenames = glob.glob(file)

for f in filenames:
    scores = open(f, "r")
    scores = scores.read()

    new = scores.split("T")

    i = 1
    t1 = 0
    t2 = 0
    result = ""

    while i < len(new):
        if new[i].startswith("1"):
            if new[i][len(new[i]) - 1] == "t":
                t1 += 5
            elif new[i][len(new[i]) - 1] == "c":
                t1 += 2
            elif new[i][len(new[i]) - 1] == "p":
                t1 += 3
            elif new[i][len(new[i]) - 1] == "d":
                t1 += 3
        else:
            if new[i][len(new[i]) - 1] == "t":
                t2 += 5
            elif new[i][len(new[i]) - 1] == "c":
                t2 += 2
            elif new[i][len(new[i]) - 1] == "p":
                t2 += 3
            elif new[i][len(new[i]) - 1] == "d":
                t2 += 3
        i += 1

    if t1 == t2:
        result = "Draw"
    elif t1 > t2:
        result = "T1 is the winner"
    elif t1 < t2:
        result = "T2 is the winner"

    filename = os.path.basename(f)
    filename = filename.split(".")
    newname = filename[0] + "_b69141na.txt"

    print(filename[0] + ": " + result)

    outputfolder = os.path.join(args.output, "")
    newpath = os.path.join(outputfolder, newname)

    filename = open(newpath, "a")

    filename.write(str(t1) + ":" + str(t2))
