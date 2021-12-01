import argparse
import os

# Sort out parsing from command line and get the necessary file paths
parser = argparse.ArgumentParser(description='Calculate rugby score')
parser.add_argument('inFolder', type=str, help='Filepath of folder containing rugby score breakdowns')
parser.add_argument('outFolder', type=str, help='Filepath of folder to place the calculated final score files')
args = parser.parse_args()
inFolderpath = args.inFolder
outFolderpath = args.outFolder

if (inFolderpath[0:-1] != "/"):
        inFolderpath += "/"

if (outFolderpath[0:-1] != "/"):
        outFolderpath += "/"

for filename in os.listdir(inFolderpath):
    # Read data from the input file
    inputFileHandle = open(inFolderpath + filename, 'r')
    scoreData = inputFileHandle.readline()
    inputFileHandle.close()

    # Be super safe and handle newline exception
    scoreData.strip('\n')

    # Calculate scores
    team1ID = 'T1'
    team2ID = 'T2'
    tryID = 't'
    goalKickID = 'c'
    penaltyID = 'p'
    dropGoalID = 'd'
    team1Score = 0
    team2Score = 0
    scoreIncrement = 0

    for index in range(0, len(scoreData), 3):

        scoreType = scoreData[index + 2: index + 3]
        if (scoreType == tryID):
            scoreIncrement = 5
        elif (scoreType == goalKickID):
            scoreIncrement = 2
        elif (scoreType == penaltyID or scoreType == dropGoalID):
            scoreIncrement = 3

        team = scoreData[index: index + 2]
        if (team == team1ID):
            team1Score += scoreIncrement
        elif (team == team2ID):
            team2Score += scoreIncrement

    # Output Scores to file
    outputFileName = filename[0:len(filename) - 4] + "_h89565jc.txt"
    outputFileHandle = open(outFolderpath + outputFileName, 'w')
    outputFileHandle.write("%i:%i" % (team1Score, team2Score))
    outputFileHandle.close()