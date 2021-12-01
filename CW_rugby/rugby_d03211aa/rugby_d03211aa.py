import os
import argparse
import sys

username = "_d03211aa"

parser = argparse.ArgumentParser()

parser.add_argument('inputs')

parser.add_argument('outputs')

args = parser.parse_args()


files = sorted(os.listdir(args.inputs))


for filename in files:
    file = open(args.inputs.strip("./") + '/' + filename)

    text = ""
    for line in file:
        text += line

    file.close()

    print(text)

    score = [0, 0]
    
    while len(text) != 0:
        team = int(text[1]) - 1
        score_type = text[2]

        if score_type == 't':
            score[team] += 5
        elif score_type == 'c':
            score[team] += 2
        elif score_type == 'p':
            score[team] += 3
        elif score_type == 'd':
            score[team] += 3

        if len(text) == 3:
            break

        text = text[3:]

    if filename[-4:] == ".txt": 
        edited_filename = filename[:len(filename) - 4] + username + ".txt"
    else:
        edited_filename = filename + username

    file = open(args.outputs.strip("./") + '/' + edited_filename, "w")

    score = str(score[0]) + ':' + str(score[1])

    file.write(score)

    file.close()

