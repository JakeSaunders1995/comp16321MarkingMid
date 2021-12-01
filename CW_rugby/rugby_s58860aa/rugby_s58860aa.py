import os
import sys

#assign input
input_folder = sys.argv[1]
output_folder = sys.argv[2]
if not os.path.isdir(output_folder):
    os.mkdir(output_folder)


for file in os.listdir(input_folder):
    with open(os.path.join(input_folder, file), "r") as inputt:
        team_scores = inputt.read()

    t = 5
    c = 2
    p = 3
    d = 3
    team1 = 0
    team2 = 0
    count = 0

    string = team_scores
    for x in range(0, len(string)):
        count += 1
        pos = x
        if (string[x] == "1"):
            if (string[pos+1] == "t"):
                team1 += 5
            elif(string[pos+1]== "c"):
                team1 += 2
            elif (string[pos + 1] == "p"):
                team1 += 3
            elif (string[pos + 1] == "d"):
                team1 += 3
        elif (string[x] == "2"):
            if (string[pos+1] == "t"):
                team2 += 5
            elif(string[pos+1]== "c"):
                team2 += 2
            elif (string[pos + 1] == "p"):
                team2 += 3
            elif (string[pos + 1] == "d"):
                team2 += 3
        else:
            x+1
    # checking
    with open(os.path.join(output_folder, os.path.basename(file)[:-4] + "_s58860aa.txt"), "w")as output_file:
        output_file.write(str(team1) + ":" + str(team2))
