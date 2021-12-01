import argparse
import os
import re

# file_input = "T1tT2pT2pT1cT1d"
# file_input = "T1tT2tT2tT2pT2c"
# file_input = "T1cT1pT2tT2tT1t"
# file_output = ""

# Parse command line input
parser = argparse.ArgumentParser()
parser.add_argument('input_path', metavar='path', type=str)
parser.add_argument('output_path', metavar='path', type=str)
arguments = parser.parse_args()
input_path = arguments.input_path
output_path = arguments.output_path

# Read input file
# with open(input_path, 'r') as f:
#     file_input = f.read()
#     file_input.rstrip()

# Main program
SCORE_TYPES = {
    't': 5,
    'c': 2,
    'p': 3,
    'd': 3
}

# Function that finds score for each team
def find_score(team, file_input):
    iterator = re.finditer(team, file_input)
    score = 0

    for val in iterator:
        score_type = file_input[val.end()]
        score += SCORE_TYPES[score_type]

    return score

# Function that writes output file
def write_to_file(file_input, file_name):
    t1_score = find_score("T1", file_input)
    t2_score = find_score("T2", file_input)

    result = f"{t1_score}:{t2_score}"

    file_name = file_name.replace(".txt", "")

    # Write to output file
    with open(os.path.join(output_path, f"{file_name}_b98919gs.txt"), 'w') as f:
        f.write(result)

# Files
try:
    os.mkdir(output_path)
except OSError as e:
    print(e)

for file in os.listdir(input_path):
    with open(os.path.join(input_path, file), 'r') as f:
        inp = f.read().rstrip()
        write_to_file(inp, file)
