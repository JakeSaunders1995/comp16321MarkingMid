import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('input_folder')
parser.add_argument('output_folder')
args = parser.parse_args()

input_directory = args.input_folder
output_directory = args.output_folder

for filename in sorted(os.listdir(input_directory)):

    output_file = filename.split(".")[0] + "_u08120fh.txt"

    with open(os.path.join(input_directory, filename), "r") as file:
        line = file.read()

    lst = []
    for i in range(len(line)):
        if line[i].isupper():
            lst.append(line[i]+line[i+1]+line[i+2])

    T1Score, T2Score = [], []

    for score in lst:
        if "T1" in score:
            T1Score.append(score[-1])
        if "T2" in score:
            T2Score.append(score[-1])

    T1 = 0
    T2 = 0

    for letter in T1Score:
        if letter == "t":
            T1 += 5
        if letter == "c":
            T1 += 2
        if letter == "p":
            T1 += 3
        if letter == "d":
            T1 += 3

    for letter in T2Score:
        if letter == "t":
            T2 += 5
        if letter == "c":
            T2 += 2
        if letter == "p":
            T2 += 3
        if letter == "d":
            T2 += 3

    with open(os.path.join(output_directory, output_file), "w") as op:
        op.write(str(T1) + ":" + str(T2))
