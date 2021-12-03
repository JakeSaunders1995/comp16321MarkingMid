import sys
import os
import re

inputFile = sys.argv[1]
outputFile = sys.argv[2]

scoresList = []

# Open input file and read lines
for file in os.listdir(inputFile):
    with open(os.path.join(inputFile, file), 'r') as inp:
        line = inp.readlines()

    # Add the line into a list
    scoresList.append(line)

    # Join list into string so I can read it using len()
    scoresString = ''.join(str(i) for i in scoresList)

    # Find the number of occurances of each scoring type in the string 
    # and times the number of occurances by the number of points the scoring type is worth
    # e.g. if team 1 scores 3 tries, 3 * 5 (score for  try) = 15 
    T1t = len(re.findall("T1t", scoresString)) * 5
    T1c = len(re.findall("T1c", scoresString)) * 2
    T1p = len(re.findall("T1p", scoresString)) * 3
    T1d = len(re.findall("T1d", scoresString)) * 3
    print(T1t)

    T2t = len(re.findall("T2t", scoresString)) * 5
    T2c = len(re.findall("T2c", scoresString)) * 2
    T2p = len(re.findall("T2p", scoresString)) * 3
    T2d = len(re.findall("T2d", scoresString)) * 3

    # Add the total scores of each team
    team_score1 = T1t + T1c + T1p + T1d
    team_score2 = T2t + T2c + T2p + T2d

    # Display the scores in correct format 
    finalScores = (str(team_score1) + ":" + str(team_score2))

    # Write finalScores into output file
    outputTxt = str(os.path.splitext(file)[0]) + "_s29576tb" + str(os.path.splitext(file)[1])
    fullOutputTxt = os.path.join("output_1/" + outputTxt)
    with open(fullOutputTxt, 'w') as out:
        for lines in finalScores:
            out.write(lines)

    scoresList = []
