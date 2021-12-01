import argparse
import os
files = []
sortedfiles = []
y = 0
parser = argparse.ArgumentParser()
parser.add_argument('inputpath')
parser.add_argument('outputpath')
args = parser.parse_args()
inputstream = args.inputpath
outputstream = args.outputpath
print(args.inputpath)
outputfile = ""

for file in os.listdir(inputstream):
    files.append(os.path.join(inputstream, file))

sortedfiles = sorted(files)

for x in range(len(sortedfiles)):
    working = open(sortedfiles[x], "r")
    result = working.read()

    total1 = 0
    total2 = 0
    winner = ""

    for x in range(len(result)):
        if str(result[x]) == "1":
            if result[x + 1] == "t":
                total1 += 5
            elif result[x + 1] == "c":
                total1 += 2
            elif result[x + 1] == "p":
                total1 += 3
            elif result[x + 1] == "d":
                total1 += 3
        elif str(result[x]) == "2":
            if result[x + 1] == "t":
                total2 += 5
            elif result[x + 1] == "c":
                total2 += 2
            elif result[x + 1] == "p":
                total2 += 3
            elif result[x + 1] == "d":
                total2 += 3

    if total1 > total2:
        winner = "T1 won"
    elif total2 > total1:
        winner = "T2 won"
    elif total1 == total2:
        winner = "T1 and T2 drew"

    print ("The result of the game was ", winner)
    print (total1 , " : ", total2)

    y += 1
    outputfile = str(outputstream)+'/test_file'+str(y)+'_e11226oc.txt'
    writeout = open(outputfile, "w")
    writeout.write(str(total1)+':'+str(total2))
