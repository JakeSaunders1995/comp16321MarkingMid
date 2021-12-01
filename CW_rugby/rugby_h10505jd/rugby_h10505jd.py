import sys
import os

inputFile = sys.argv[1]
outFile = sys.argv[2]

files = os.listdir(inputFile)

'''
print(inputFile)
print(files)
print(inputFile+"/"+files[0])

file = open(inputFile+"/"+files[0],"r")
line = file.readline()
file.close()

print(line)
'''

for fileName in files:
    file = open(inputFile+"/"+fileName,"r")
    line = file.readline()
    file.close()
    scores = []
    while len(line) > 0:
        scores += [line[1:3]]
        line = line[3:]

    onePoints = 0
    twoPoints = 0
    for f in scores:
        if f[1] == "t":
            points = 5
        elif f[1] == "c":
            points = 2
        else:
            points = 3
        if f[0] == "1":
            onePoints += points
        else:
            twoPoints += points

    onePoints = str(onePoints)
    twoPoints = str(twoPoints)

    file = open(outFile+"/"+fileName[:-4]+"_h10505jd.txt","w")
    file.write(onePoints+":"+twoPoints)
    file.close()
