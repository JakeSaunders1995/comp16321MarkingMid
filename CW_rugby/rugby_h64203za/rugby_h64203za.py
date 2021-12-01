import argparse, os

parser = argparse.ArgumentParser()
parser.add_argument('inputDir')
parser.add_argument('outputDir')

args = parser.parse_args()


inputPath = args.inputDir
dirs = os.listdir(inputPath)
outputPath = args.outputDir
# print(dirs)
curDir = []
for k in range(len(dirs)):
    current = dirs[k]
    if current.endswith('.txt'):
        current = current[:-4]
        current = current + "_h64203za.txt"
        curDir.append(current)

# print(curDir)


def scoreCheck(team):
    x = 0
    for i in range(len(team)):
        if team[i] == "t":
            x += 5
        elif team[i] == "c":
            x += 2
        elif team[i] == "p":
            x += 3
        elif team[i] == "d":
            x += 3
    return x


for j in range(len(dirs)):
    readName = dirs[j]
    writeName = curDir[j]

    readFile = os.path.join(inputPath, readName)
    writeFile = os.path.join(outputPath, writeName)

    f = open(readFile,"r")
    team1 = []
    team2 = []
    line = f.readline()
    for i in range(len(line)):
        if line[i:i+2] == "T1":
            team1.append(line[i+2])
        elif line[i:i+2] == "T2":
            team2.append(line[i+2])
    f.close()

    score1 = scoreCheck(team1)
    score2 = scoreCheck(team2)

    # if score1 == score2:
    #     print("It's a draw!")
    # elif score1 > score2:
    #     print("Team 1 wins!")
    # else:
    #     print("Team 2 wins!")


    print(str(score1)+":"+str(score2))

    s = open(writeFile,"w")
    s.write(str(score1)+":"+str(score2))
    s.close()
