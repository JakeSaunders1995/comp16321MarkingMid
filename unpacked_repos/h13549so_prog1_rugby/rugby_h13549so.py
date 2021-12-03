import sys
import os

# iterates over input directory and stores an array of the files 
files = os.listdir(sys.argv[1])
for i in range(len(files)-1):
    if files[i] == ".DS_Store":
        files.remove(".DS_Store")
    else:
        continue

# converts string to score
def translate(str, index, start):
    score = 0
    if str == "t":
        score = score + 5
    elif str == "d" or str == "p":
        score = score + 3
    elif str == "1":
        score = score
    else:
        score = score + 2
    return score

# Summing scores
def sum(team, file):
    readInput = open(sys.argv[1]+"/"+file, "r")
    actions = readInput.read()
    teamScore = 0
    start = 0 
    end = len(actions) - 1
    index = 0
    while start <= end and index != -1:
        index = actions.find(team, start, end)
        if index != 0:
            start = index + 3
        else:
            start = start + 3
        action = actions[index + 2]
        teamScore = teamScore + translate(action, index, start)
    return teamScore

# runs output procedure for each file in input directory
for file in files:
    # f = open(sys.argv[2]+"/"+file.removesuffix(".txt")+"_h13549so.txt", mode='a')
    f = open(sys.argv[2]+"/"+file.removesuffix(".txt")+"_h13549so.txt", "w")
    f.write(str(sum("T1", file)))
    f.write(":")
    f.write(str(sum("T2", file)))
    f.write("\n")

