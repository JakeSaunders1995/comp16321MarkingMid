from argparse import ArgumentParser
import os

parser = ArgumentParser(description="Take in files")
parser.add_argument("input", help="Take in input folder.")
parser.add_argument("output", help="Take in output folder.")
args = parser.parse_args()
folders = args

def score(filename):
    f = open(f'{folders.input}/{filename}', "r")
    line = f.read()
    team1 = 0
    team2 = 0
    flag = False

    for char in line:
        if char == "T":
            continue
        elif char == "1":
            flag = True
        elif char == "2":
            flag = False
        elif char == "t":
            if flag:
                team1 += 5
            else:
                team2 += 5
        elif char == "c":
            if flag:
                team1 += 2
            else:
                team2 += 2
        elif char == "p":
            if flag:
                team1 += 3
            else:
                team2 += 3
        elif char == "d":
            if flag:
                team1 += 3
            else:
                team2 += 3

    with open(f'{folders.output}/{filename[:-4]}_m09857ly.txt', "w") as output:
        output.write(f'{team1}:{team2}')
        output.close()

try:
    os.mkdir(folders.output)
except:
    pass

for file in os.listdir(folders.input):
    score(file)
