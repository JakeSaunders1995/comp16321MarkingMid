import sys
import os

def findscore():
        findscore.team1score = 0
        findscore.team2score = 0

        scoreArray = str(scorelist)
        scoreArray = scoreArray.replace("[", "") 
        scoreArray = scoreArray.replace("'", "")
        scoreArray = scoreArray.replace("]", "")

        #for every 3 characters in scorelist array
        for character in range(0, len(scoreArray)):
   
            if character % 3 != 0:
                continue
    
            tempTeam = scoreArray[character + 1]
            tempScoreType = scoreArray[character + 2]
    
            if tempScoreType == "t":
                tempScore = 5
                pass
            elif  tempScoreType == "c":
                tempScore = 2
                pass
            elif  tempScoreType == "p":
                tempScore = 3
                pass
            elif  tempScoreType == "d":
                tempScore = 3
                pass

            if tempTeam == "1":
                findscore.team1score += tempScore
                pass
            elif tempTeam == "2":
                findscore.team2score += tempScore
                pass

        #compare scores
        if findscore.team2score < findscore.team1score:
            winner = "Team 1"
        elif findscore.team2score > findscore.team1score:
            winner = "Team 2"
        else:
            winner = "Draw"

def createTextFile():
    line = filename
    index = line.find(".txt")
    createTextFile.output_file = line[:index] + "_h52171rh" + ".txt"
    pass

def outputFileToFolder():

        completeName = os.path.join(outputPath, createTextFile.output_file)
        output = str(findscore.team1score) + ":" +  str(findscore.team2score) 
        file1 = open(completeName, "w")
        file1.write(output)
        file1.close()

inFolder = sys.argv[1]
inFolderPath = os.path.abspath(inFolder)
outFolder = sys.argv[2]

#if outFolder already exists, quit program

if os.path.exists(outFolder) == False:
    os.mkdir(outFolder)     
    outputPath = os.path.abspath(outFolder)
else:
    outputPath = os.path.abspath(outFolder)

arr = os.listdir(inFolder)

for everyFile in arr:

    if os.getcwd() != inFolderPath:
        os.chdir(inFolderPath)
    
    with open(everyFile,'r') as i:
        scorelist = i.readlines()
        filename = everyFile
        findscore()     
        createTextFile()
        outputFileToFolder()    
    pass