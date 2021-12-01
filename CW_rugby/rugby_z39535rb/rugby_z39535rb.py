import argparse
import os


def CalculateScore():
    team1Score = 0
    team2Score = 0

    for char in range(0, len(teams), 3):
        charEnd = char + 2
        if teams[char: charEnd] == "T1":
            if teams[charEnd] == "t":
                team1Score += 5
            elif teams[charEnd] == "c":
                team1Score += 2
            elif teams[charEnd] == "p":
                team1Score += 3
            elif teams[charEnd] == "d":
                team1Score += 3
        elif teams[char: charEnd] == "T2":
            if teams[charEnd] == "t":
                team2Score += 5
            elif teams[charEnd] == "c":
                team2Score += 2
            elif teams[charEnd] == "p":
                team2Score += 3
            elif teams[charEnd] == "d":
                team2Score += 3
    global finalScore
    finalScore = str(team1Score) + ":" + str(team2Score)


def FileHandling():
    inputPath = args.teamsEnter
    fileList = os.listdir(inputPath)
    fileList.sort()

    outputPath = args.scoreSave

    for file in fileList:
        with open(inputPath + '/' + file) as f:
            global teams
            teams = f.read()
        CalculateScore()
        with open(outputPath + '/' + file[:-4] + '_z39535rb.txt', 'w') as s:
            s.write(finalScore)
        s.close()
        f.close()


parser = argparse.ArgumentParser(description="file path")
parser.add_argument("teamsEnter", type=str, help="input file path")
parser.add_argument("scoreSave", type=str, help="output file path")
args = parser.parse_args()

FileHandling()
