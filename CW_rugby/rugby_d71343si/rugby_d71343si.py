import sys
import os

input_name = sys.argv[1]
output_name = sys.argv[2]

for testfile in os.listdir(input_name):
    f = os.path.join(input_name, testfile)
    print("File:", testfile)
    input_file = open(f, 'r')
    scores = input_file.read()
    team1 = []
    team2 = []
    count = len(scores)
    team1_points = 0
    team2_points = 0

    for x in range(count):
        if scores[x] == '1':
            team1.append(scores[x+1])

    for y in range(count):
        if scores[y] == '2':
            team2.append(scores[y+1])

    for a in team1:
        if a == "t":
            team1_points += 5
        elif a == "c":
            team1_points += 2
        elif a == "p":
            team1_points += 3
        elif a == "d":
            team1_points += 3

    for b in team2:
        if b == "t":
            team2_points += 5
        elif b == "c":
            team2_points += 2
        elif b == "p":
            team2_points += 3
        elif b == "d":
            team2_points += 3

    print(team1_points,':',team2_points)

    if team1_points > team2_points:
        print("Team 1 is the winner.")
    elif team1_points < team2_points:
        print("Team 2 is the winner.")
    elif team1_points == team2_points:
        print("It is a draw.")

    output_file_name = testfile[:-4] + "_d71343si.txt"
    output_file_path = os.path.join(output_name, output_file_name)

    output_file = open(output_file_path, "w")
    output_file.write(str(team1_points))
    output_file.write(":")
    output_file.write(str(team2_points))

    input_file.close()
    output_file.close()