import os
import sys
import glob

username = "x09137dp"

t1Score = 0 #Team 1's Score
t2Score = 0 #Team 2's Score

for file in glob.iglob(sys.argv[1] + "/**"):
    input = open(file, 'r') #Opens input file in read only mode

    while True:
        team = input.read(2).casefold() #Checks for specific team
        if team == "":
            break
        pointType = input.read(1).casefold() #Checks what type of point was scored

        if pointType == "t":
            points = 5
        elif pointType == "c":
            points = 2
        elif pointType == "p":
            points = 3
        elif pointType == "d":
            points = 3
        else:
            points = 0

        if team == "t1":
            t1Score = t1Score + points #Adds relevant points to team1
        if team == "t2": #Adds relevant points to team2
            t2Score = t2Score + points

    path, filenameExt = os.path.split(file)
    filename, extentsion = os.path.splitext(filenameExt)
    outputPath = os.path.join(sys.argv[2], filename + "_" + username + ".txt")
    output = open(outputPath, 'w') #Creates and opens output file in write mode

    output.write(str(t1Score) + ":" + str(t2Score)) #Writes output to text file
    t1Score = 0
    t2Score = 0

    output.close()
    input.close()
