import os, argparse
parser = argparse.ArgumentParser()
parser.add_argument("inputFile")
parser.add_argument("outputFolder")
args = parser.parse_args()
input1 = args.inputFile
output = args.outputFolder

files = os.listdir(input1)

def getScores(file):
    fileLocation = os.path.join(input1, file)
    scores = open(fileLocation, "r")
    scores = scores.read()
    team1score = 0
    team2score = 0
    for x in range(int(len(scores)/3)):
        #print(x)
        counter = x * 3

        team = scores[counter] + scores[counter+1]
        #print(team)
        individualScore = scores[counter+2]
        if team == "T1":
            
            if individualScore == "t":
                team1score += 5
            elif individualScore == "c":
                team1score += 2
            elif individualScore == "p":
                team1score += 3
            elif individualScore == "d":
                team1score += 3

        elif team == "T2":
            
            if individualScore == "t":
                team2score += 5
            elif individualScore == "c":
                team2score += 2
            elif individualScore == "p":
                team2score += 3
            elif individualScore == "d":
                team2score += 3
    print(team1score)
    print(team2score)
    if team1score == team2score:
        print("Team 1 drew with Team 2")
    elif team1score > team2score:
        print("Team 1 beat Team 2")
    elif team2score > team1score:
        print("Team 2 beat Team 1")
    finalScore = str(team1score) + ":" + str(team2score)
    return finalScore


def WriteToFile(output, finalScore, fileName):
    fileToOutput = os.path.join(output, fileName + "_p56273gd.txt")
    file = open(fileToOutput, "w")
    file.write(finalScore)

for file in files:
    finalScore = getScores(file)
    fileSplit = file.split(".")
    fileName = fileSplit[0]
    WriteToFile(output, finalScore, fileName)
