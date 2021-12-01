import argparse
import os
parser = argparse.ArgumentParser()
parser.add_argument('input', metavar='i', type=str)
parser.add_argument('output', metavar='o', type=str)
paths = parser.parse_args()
def scorer(file):
    scores = ''
    for line in file.readlines():
        scores += line
    cache = []
    T1 = []
    T2 = []
    file.close()
    for character in scores:
        cache.append(character)
        if len(cache) == 3:
            if cache[1] == '1':
                T1.append(cache[2])
            else:
                T2.append(cache[2])
            cache = []
    T1Score = 0
    T2Score = 0
    for score in T1:
        if(score == "t"):
            T1Score += 5
        elif(score=="c"):
            T1Score += 2
        else:
            T1Score+= 3
    for score in T2:
        if(score == "t"):
            T2Score += 5
        elif(score=="c"):
            T2Score += 2
        else:
            T2Score+= 3
    if(T1Score != T2Score):
        if(T1Score > T2Score):
            print("T1 Won!!!")
        else:
            print("T2 Won!!!")
    else:
        print("Draw!!!")
    return str(T1Score)+":"+str(T2Score)
files = os.scandir(paths.input)
for entry in files:
    path = ""
    if paths.input[-1] != "/":
        path = paths.input +"/"
    else:
        path = paths.input
    fileInput = open(path+entry.name)
    out = scorer(fileInput)
    fileInput.close()
    if paths.output[-1] != "/":
        path = paths.output + "/"
    else:
        path = paths.output
    fileOutput = open(paths.output + "/" + entry.name.replace('.txt','') + "_n54133hu.txt",'w')
    fileOutput.write(out)
    fileOutput.close()
