import argparse
import os
parser = argparse.ArgumentParser()
parser.add_argument('input')
parser.add_argument('output')
args = parser.parse_args()

input_folder = args.input
output_folder = args.output


for file in os.listdir(input_folder):
    f = open(input_folder+"/"+file)
    input_file_read = f.read()
    input_list = list(input_file_read)

    i = 0
    team1 = []
    team2 = []
    for item in input_list:
        if item == "1":
            team1.append(input_list[i + 1])

        if item == "2":
            team2.append(input_list[i + 1])
        i += 1

    i = 0
    for score in team1:
        if score == "t":
            team1[i] = 5
        if score == "c":
            team1[i] = 2
        if score == "p":
            team1[i] = 3
        if score == "d":
            team1[i] = 3
        i += 1
    team1 = sum(team1)

    i = 0
    for score in team2:
        if score == "t":
            team2[i] = 5
        if score == "c":
            team2[i] = 2
        if score == "p":
            team2[i] = 3
        if score == "d":
            team2[i] = 3
        i += 1
    team2 = sum(team2)

    if team1 > team2:
        print("team 1 is the winner")
    elif team2 > team1:
        print("team 2 is the winner")
    else:
        print("draw")

    output_name = os.path.join(output_folder, file.replace(".txt", "_p15748aa.txt"))
    output_file = open(output_name, "w")
    output_file.write(f'{team1}:{team2}')
    output_file.close()
