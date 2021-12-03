import argparse
import os
from pathlib import Path

def checkScore(value):
    if value == "t":
        return 5
    if value == "c":
        return 2
    if value == "p" or value == "d":
        return 3

# Get both files
parser = argparse.ArgumentParser(description = "Take the scores of both teams, and store the total scores in another file")

parser.add_argument('input_folder', help="The input folder")
parser.add_argument('output_folder', help="The output folder")
files = parser.parse_args()

# Check files exist
input_exists, output_exists = os.path.exists(files.input_folder), os.path.exists(files.output_folder)

if len(os.listdir(files.input_folder)) == 0:
    print('No files in input folder')
    os._exit(1)

if input_exists and output_exists:
    pass
else:
    print("Incorrect file paths were entered")
    os._exit(1)

# Loop through files in the input folder
for filename in os.listdir(files.input_folder):
    if filename.endswith('.txt'):

        # Open the current txt file
        input_filepath = os.path.join(files.input_folder, filename)
        input_file = open(str(input_filepath), "r")

        output_filename = str(Path(filename).stem + "_k77872uk.txt")

        # Make the output file
        output_filepath = os.path.join(files.output_folder, output_filename)
        output_file = open(str(output_filepath), "w")

        # Go through the input file and sort the scores, T1tT2pT2pT1pT1d
        scores = input_file.readline().rstrip()

        # Seperate the different scores
        T1_scores = int(0)
        T2_scores = int(0)

        for c in range(0,len(scores)):
            character = scores[c]
            if character != "T" or character != 1 or character != 2:
                score = checkScore(character)
                if scores[c-1] == "1":
                    T1_scores += score
                elif scores[c-1] == "2":
                    T2_scores += score


        # Write to the output file, then close the files
        output_file.write("{}:{}".format(str(T1_scores),str(T2_scores)))
        input_file.close()
        output_file.close()
