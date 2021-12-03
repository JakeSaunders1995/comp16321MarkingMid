import os
import argparse

def score(name):
    t1 = 0
    t2 = 0
    f = open(name, "r")
    txt = f.read()
    f.close()
    for i in range(0, len(txt), 3):
        if (txt[i] == "T"):
            if (txt[i+1] == "1"):
                if (txt[i+2] == "t"):
                    t1 += 5
                elif (txt[i+2] == "c"):
                    t1 += 2
                elif (txt[i + 2] == "p" or txt[i + 2] == "d"):
                    t1 += 3
            if (txt[i+1] == "2"):
                if (txt[i+2] == "t"):
                    t2 += 5
                elif (txt[i+2] == "c"):
                    t2 += 2
                elif (txt[i + 2] == "p" or txt[i + 2] == "d"):
                    t2 += 3
    return (str(t1)+":"+str(t2))

def store(name, content):
    if (os.path.isfile(name)):
        f = open(name, "w")
        f.write(content)
        f.close()
    else:
        f = open(name, "x")
        f.write(content)
        f.close()

parser = argparse.ArgumentParser()
parser.add_argument("inputPath", help="increase input path")
parser.add_argument("outputPath", help="increase output path")
args = parser.parse_args()
currentPath = os.getcwd()
os.chdir(args.inputPath)
pathList = os.listdir()
list1 = []
list2 = []
for text in pathList:
    list1.append(text)
    list2.append(score(text))
os.chdir(currentPath)
os.chdir(args.outputPath)
for i in range(len(list1)):
    if (list1[i][-4:] == ".txt"):
        tmp = list1[i][0:-4] + "_y70582kd.txt"
    else:
        tmp = list1[i] + "_y70582kd"
    store(tmp, list2[i])

