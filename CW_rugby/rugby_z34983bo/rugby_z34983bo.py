import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("cheese", type=str, nargs="+")
path = parser.parse_args()

scanned = os.scandir(path.cheese[0])
directories = []
for j in scanned:
    directories.append(j.path)
directories = sorted(directories)
fileNo = 1;
for i in directories:

    file = open(i, "r")
    score = file.readline()
    file.close()

    Team1Score = 0
    Team2Score = 0
    t = 5; c = 2; p = 3; d = 3

    def givescore(x):
        if (x == "c"):
            return 2
        if (x == "p" or x == "d"):
            return 3
        if (x == "t"):
            return 5
    for i in range(len(score)):
        if (score[i] == "1"):
            Team1Score += givescore(score[i+1])
        elif (score[i] == "2"):
            Team2Score += givescore(score[i+1])

    final = str(Team1Score) + ":" + str(Team2Score)
    file = open(path.cheese[1]+"/test_file" + str(fileNo) + "_z34983bo.txt", "w")
    fileNo+=1
    file.write(final)
    file.close()
