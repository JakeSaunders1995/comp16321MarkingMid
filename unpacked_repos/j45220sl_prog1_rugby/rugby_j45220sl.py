import argparse


def mark2score(mark):
    if mark == 't':
        score = 5
    elif mark == 'c':
        score = 2
    elif mark == 'p':
        score = 3
    elif mark == 'd':
        score = 3
    else:
        pass
    return score


# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument('inputfile', action='store', type=str)
parser.add_argument('outputfile', action='store', type=str)
args = parser.parse_args()
inputfile = args.inputfile
outputfile = args.outputfile

# read input
with open(inputfile, 'r') as FILE:
    string = FILE.readline()

# count score
T1 = 0
T2 = 0
for i in range(int(len(string)/3)):
    item = string[3*i:3*i+3]
    team = item[:2]
    mark = item[2]
    if team == 'T1':
        T1 += mark2score(mark)
    else:
        T2 += mark2score(mark)

# output
with open(outputfile, "w") as file:
    file.write('%d:%d' % (T1, T2))
