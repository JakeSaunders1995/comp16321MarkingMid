import sys,os

arguments = sys.argv
for filename in os.listdir(arguments[1]):
    if arguments[1][-1] != "/":
        source = arguments[1]+"/"+filename
    else:
        source = arguments[1]+filename
    with open(source,"r") as sourceFile:
        scoreSeries = sourceFile.read()

    scoreSources = scoreSeries.split("T")[1:]

    teamScores = [0,0]

    for score in scoreSources:
        if score[1] == "t":
            teamScores[int(score[0])-1] += 5
        elif score[1] == "c":
            teamScores[int(score[0])-1] += 2
        else:
            teamScores[int(score[0])-1] += 3

    finalScore = str(teamScores[0])+":"+str(teamScores[1])

    if arguments[2][-1] != "/":
        outputName = arguments[2]+"/"+filename[:-4]+"_t28107tj.txt"
    else:
        outputName = arguments[2]+filename[:-4]+"_t28107tj.txt"


    with open(outputName,"w") as outputFile:
        outputFile.write(finalScore)