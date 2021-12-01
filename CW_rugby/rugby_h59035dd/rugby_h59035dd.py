import os
import sys

inputFolder = sys.argv[1]
outputFolder = sys.argv[2]
for file in os.listdir(inputFolder):#reads file from directory
    input = open(inputFolder + "/" + file, "r")
    data = input.read()
    team1 = 0 #team1 score
    team2 = 0 #team2 score
    for i in range(0, len(data), 3):
        team = data[i:i+2]
        if(data[i+2] == "t"): points = 5 #determines how many points was score
        elif(data[i+2] == "c"): points = 2
        elif(data[i+2] == "p" or data[i+2] == "d"): points = 3
        if(team == "T1"): team1 += points ##determines which team gets points
        elif(team == "T2"): team2 += points
    if(os.path.isfile(outputFolder + "/" + file[0:len(file) - 4] + "_h59035dd.txt")): #output
        output = open(outputFolder + "/" + file[0:len(file) - 4] + "_h59035dd.txt", "w")
    else:
        output = open(outputFolder + "/" + file[0:len(file) - 4] + "_h59035dd.txt", "x")
    output.write(str(team1) + ":" + str(team2))
    input.close()
    output.close()
