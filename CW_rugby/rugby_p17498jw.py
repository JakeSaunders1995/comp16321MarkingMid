import argparse
import os
import re

parser = argparse.ArgumentParser()
# Create arguments
parser.add_argument("input_dir", help="A dirpath for the input score files")
parser.add_argument("output_dir", help="A dirpath for the output score files")

args = parser.parse_args()

input_dir = args.input_dir
output_dir = args.output_dir

# Make output directory if required
if not os.path.isdir(output_dir):
    os.makedirs(output_dir)

input_files = []
output_files = []
# Walk through input directory recursively to get files
for root, dirs, files in os.walk(input_dir):
    for name in files:
        # root will be relative or absolute depending on what was given as an arg
        input_files.append(os.path.join(root, name))
        # The slice assumes that the input filename ends in .txt
        output_files.append(os.path.join(output_dir, name[:-4] + "_p17498jw.txt"))

score_map = {"t":5, "c":2, "p":3, "d":3}
for i in range(0, len(input_files)):
    in_file = input_files[i]
    out_file = output_files[i]
    # Read scores from file - assume on first and only first line
    in_fh = open(in_file, "r")
    in_scores = in_fh.readline()
    in_fh.close()
    
    team1_score = 0
    team2_score = 0
    # Split string by team scores to produce them in an enumerable list
    for score in re.findall(r"T\d[tcpd]", in_scores):
        # Use map to determine score to add to team's total
        if score[1] == "1":
            team1_score += score_map[score[2]]
        elif score[1] == "2":
            team2_score += score_map[score[2]]

    # Determine winner
    if team1_score == team2_score:
        print("{0}:{1} Teams 1 and 2 drew".format(team1_score, team2_score))
    elif team1_score > team2_score:
        print("{0}:{1} Team 1 won".format(team1_score, team2_score))
    else:
        print("{0}:{1} Team 2 won".format(team1_score, team2_score))
    
    # Store final score in output file
    out_fh = open(out_file, "w+")
    out_fh.write("{0}:{1}".format(team1_score, team2_score))
    out_fh.close()

