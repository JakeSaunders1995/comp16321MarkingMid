import sys
import os

files = os.listdir(sys.argv[1])

for filename in files:

    file = open(sys.argv[1] + "/" + filename, "r")

    team1Total = 0
    team2Total = 0
    invalidFile = False

    for line in file:
        line = line.rstrip()
        
        currentChar = 0
        while currentChar < len(line)-2:
            currentTeam = line[currentChar:currentChar + 2]
            
            if currentTeam == "T1" or currentTeam == "T2":
                if line[currentChar + 2] == "t":
                    scoredPoints = 5
                elif line[currentChar + 2] == "c":
                    scoredPoints = 2
                elif line[currentChar + 2] == "p":
                    scoredPoints = 3
                elif line[currentChar + 2] == "d":
                    scoredPoints = 3
                else: invalidFile = True

                if not invalidFile:
                    if currentTeam == "T1": team1Total += scoredPoints
                    if currentTeam == "T2": team2Total += scoredPoints

                currentChar += 3

            else: invalidFile = True

            if invalidFile: break

    file.close()
    newFile = sys.argv[2] + "/" + filename[:len(filename)-4] + "_e78508hb.txt"
    if not(invalidFile):
        file = open(newFile,"w")
        file.write(str(team1Total) + ":" + str(team2Total))
    file.close()
