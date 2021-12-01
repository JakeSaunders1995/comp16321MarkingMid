import sys
import os

in_dir = sys.argv[1]
out_dir = sys.argv[2]

files = os.listdir(in_dir)

for file in files:
    address = in_dir + "/" + file
    points_file = open(address, "r")
    for text in points_file:
            text = text.rstrip()
    points_file.close()

    team = []
    points = []

    for char in text:
        if char == "T":
            continue
        if char == "1" or char == "2":
            team.append(char)
        else:
            points.append(char)

    t1_points = 0
    t2_points = 0

    for i in range(len(team)):
        if team[i] == "1":
            if points[i] == "t":
                t1_points += 5
            elif points[i] == "c":
                t1_points += 2
            elif points[i] == "p" or points[i] == "d":
                t1_points += 3
        if team[i] == "2":
            if points[i] == "t":
                t2_points += 5
            elif points[i] == "c":
                t2_points += 2
            elif points[i] == "p" or points[i] == "d":
                t2_points += 3

    name_len = len(file) - 4
    output_add = out_dir + "/" + file[:name_len] + "_g45512id.txt"
    score_file = open(output_add, "w")
    score_file.write(str(t1_points))
    score_file.write(":")
    score_file.write(str(t2_points))
    score_file.close()