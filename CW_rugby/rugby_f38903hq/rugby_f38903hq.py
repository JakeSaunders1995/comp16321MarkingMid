import argparse
import os
import re
parser = argparse.ArgumentParser()
parser.add_argument('input_folder')
parser.add_argument('output_folder')
args = parser.parse_args()
inputFolder = args.input_folder
outputFolder = args.output_folder
wen = os.listdir(inputFolder)
t1 = ""
t2 = ""
s1 = 0
s2 = 0
for file in wen:
    os.chdir(inputFolder)
    te = []
    tr =[]
    with open(file) as files:
        q = files.read()
        for line in q:
            line = line.strip()
            teappend(line)

    t = len(te)
    x = 1
    while a1 in t1:
        if a1 == 't':
            s1 += 5
        elif a1 =='c':
            s1 += 2
        elif a1 =='p':
            s1 += 3
        elif a1 =='d':
            s1 += 3
    while a2 in t2:
        if a2 =='t' :
            s2 += 5
        elif a2 =='c':
            s2 += 2
        elif a2 =='p' :
            s2 += 3
        elif a2 =='d':
            s2 += 3
    for char in te:
        while x < len(te):
            marks = te[x+1]
            teams = te[x]
            if te[x] == '1':
                t1 += marks
            else:
                t2 += marks
            x += 3
