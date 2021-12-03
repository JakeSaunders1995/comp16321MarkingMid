import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input', type=argparse.FileType('r'))
parser.add_argument('output', type=argparse.FileType('w'))
args = parser.parse_args()

input = args.input
output = args.output

scores = input.read()

t1Scores=0
t2Scores = 0

lst = scores.split("T")
lst.pop(0)

points = {"t": 5, "c": 2, "p": 3, "d": 3}

for ele in lst:
    if ele[0] == "1":
        t1Scores += points[ele[1]]
    else:
        t2Scores += points[ele[1]]

finalScores = str(t1Scores) + ":" + str(t2Scores)
output.write(finalScores)
output.close()