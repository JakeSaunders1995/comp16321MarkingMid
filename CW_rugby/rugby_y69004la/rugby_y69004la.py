import os
import sys

t,c,p,d = 5,2,3,3
n  = 3
word = []
T1 = 0
T2 = 0
count = 0
a = 0

directory = sys.argv[1]
outputdirectory = sys.argv[2]
for filename in os.listdir(directory):
    filepath = directory + "/" + filename
    textfile = open(filepath, "r")
    score = textfile.read()

    for index in range(0, len(score), n):
        word.append(score[index : index + n])
    T1 = 0
    T2 = 0
    while (a < word.count("T1t")):
        T1 += t
        a+=1
    a = 0
    while (a < word.count("T1c")):
        T1 += c
        a+=1
    a = 0
    while (a < word.count("T1p")):
        T1 += p
        a+=1
    a = 0
    while (a < word.count("T1d")):
        T1 += d
        a+=1
    a = 0
    while (a < word.count("T2t")):
        T2 += t
        a+=1
    a = 0
    while (a < word.count("T2c")):
        T2 += c
        a+=1
    a = 0
    while (a < word.count("T2p")):
        T2 += p
        a+=1
    a = 0
    while (a < word.count("T2d")):
        T2 += d
        a+=1
    a = 0
    word = []
    textfile.close()

    #if((T1) > (T2)):
     #   print("T1 is the winner")
    #elif((T1) < (T2)):
     #   print("T2 is the winner")
    #else:
     #   print("draw")



    path = outputdirectory

    if not os.path.exists(path):
        os.makedirs(path)

    outputfile = outputdirectory + "/" + filename[0:-4] + "_" + "y69004la" + ".txt"
    s = open(outputfile, "w")
    s.write(str(T1)+":"+str(T2))
    s.close() 

