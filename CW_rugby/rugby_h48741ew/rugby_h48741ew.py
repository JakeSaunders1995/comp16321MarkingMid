import argparse
import os
import re

parser = argparse.ArgumentParser()
parser.add_argument("input",type = str, help = "the file to input the text in")
parser.add_argument("output", type = str, help = "the file to output the text in")
args = parser.parse_args()

pathdest = args.input
realoutputpath = args.output

def check(filedest, string, score):
        score = 0
        file = open(filedest)
        line = file.readline()
        
        new = re.findall("...",line)
        for x in new:
            if string in x:
                score += 1
        return score

for file in os.listdir(pathdest):
    outputpath = realoutputpath
    name = file.split(".")[0]
    fileName = name + "_h48741ew.txt"
    outputpath = os.path.join(outputpath,fileName)
    T1t5 = 0
    T1c2 = 0
    T1p3 = 0
    T1d3 = 0
    T2t5 = 0
    T2c2 = 0
    T2p3 = 0
    T2d3 = 0

    T2p3 = check(os.path.join(pathdest,file), "T2p", T2p3)
    T2t5 = check(os.path.join(pathdest,file), "T2t", T2t5)
    T2c2 = check(os.path.join(pathdest,file), "T2c", T2c2)
    T2d3 = check(os.path.join(pathdest,file), "T2d", T2d3)
    T1p3 = check(os.path.join(pathdest,file), "T1p", T1p3)
    T1d3 = check(os.path.join(pathdest,file), "T1d", T1d3)
    T1t5 = check(os.path.join(pathdest,file), "T1t", T1t5)
    T1c2 = check(os.path.join(pathdest,file), "T1c", T1c2)

    T1 = T1c2*2 + T1p3*3 + T1d3 *3 + T1t5*5
    T2 = T2c2*2 + T2p3*3 + T2d3 *3 + T2t5*5
    for i in range(len(os.listdir(pathdest))):
        outputfile = open(outputpath,"w")
        outputfile.write(str(T1)+":"+str(T2))
        i +=1

