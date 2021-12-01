import argparse
import os
import re

parser = argparse.ArgumentParser(
        description="Rugby Scoring program"
    )
parser.add_argument(
        "inp_folder"
    )
parser.add_argument(
        "out_folder"
    )
args = parser.parse_args()

if not os.path.isdir(args.out_folder):
    os.mkdir(args.out_folder)

username = "v35417sp"
for input in sorted(os.listdir(args.inp_folder)):
    name = re.match('(.*)\.txt', input).groups()[0]
    name += f"_{username}.txt"

    with open(args.inp_folder + "/" + input, 'r') as f:
        data = f.read()

    types = {
            't':5,
            'c':2,
            'p':3,
            'd':3
            }
    scores = [0, 0]

    for i in range(0, len(data), 3):
        scores[ int(data[i+1]) - 1 ] += types[data[i+2]]

    winner = ''
    if scores[0] > scores[1]:
        winner = "Team 1"
    elif scores[0] < scores[1]:
        winner = "Team 2"
    else:
        winner = "Draw"

    with open(args.out_folder + "/" + name, 'w') as f:
        f.write(':'.join(map(str,scores)))
