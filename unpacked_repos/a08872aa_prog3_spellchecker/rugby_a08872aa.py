import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("input_folder")
parser.add_argument("output_folder")
args = parser.parse_args()
input_folder_name = args.input_folder
output_folder_name = args.output_folder

files_to_loop = os.listdir(input_folder_name)

for file in files_to_loop:
    input_file_name = file
    output_file_name = "{}_a08872aa.txt".format(input_file_name.replace(".txt",""))
    if "/" in input_folder_name:
       input_file = open("{}/{}".format(input_folder_name, input_file_name), "r")
    else:
       input_file = open("{}\{}".format(input_folder_name, input_file_name), "r")
    team1_score = 0
    team2_score = 0

    for line in input_file:
        i = 0
        while i < len(line):
            current_st = line[i:i+3]
            if current_st[2] == "t":
                points = 5
            elif current_st[2] == "c":
                points = 2
            elif current_st[2] == "p" or current_st[2] == "d":
                points = 3
            if current_st[1] == "1":
                team1_score += points
            else:
                team2_score += points
            i+=3
    input_file.close()

    if team1_score > team2_score:
        winner = "team1"
    elif team2_score > team1_score: 
        winner = "team2"
    else:
        winner = "draw"

    if "/" in output_folder_name:
        output_file = open("{}/{}".format(output_folder_name, output_file_name), "w")
    else:
        output_file = open("{}\{}".format(output_folder_name, output_file_name), "w")
    output_file.write("{}:{}".format(str(team1_score), str(team2_score)))
    output_file.close()
