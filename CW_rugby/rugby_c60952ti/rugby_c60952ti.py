import os
import argparse
import re

parser = argparse.ArgumentParser(description="Rugby")
parser.add_argument("IN_FOLDER")
parser.add_argument("OUT_FOLDER")

args = parser.parse_args()

for input_filename in os.scandir(args.IN_FOLDER):
    with open(input_filename.path, "r") as input_file:
        input_str = input_file.read()

    score = [0, 0]

    team = 0
    for char in input_str:
        if char == "T":
            continue
        elif char == "1":
            team = 0
        elif char == "2":
            team = 1
        elif char == "t":
            score[team] += 5
        elif char == "c":
            score[team] += 2
        elif char == "p" or char == "d":
            score[team] += 3
        else:
            raise Exception("Invalid input!")

    output_str = str(score[0]) + ":" + str(score[1])

    output_filename = os.path.join(
        args.OUT_FOLDER,
        os.path.splitext(
            os.path.basename(input_filename))[0] +
        "_c60952ti" +
        os.path.splitext(input_filename)[1])

    with open(output_filename, "w") as output_file:
        output_file.write(output_str)
