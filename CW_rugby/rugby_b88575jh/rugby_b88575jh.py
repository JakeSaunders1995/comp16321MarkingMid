import argparse
import os

def interpretScore(value):
    if value == 't':
        return 5
    elif value == 'c':
        return 2
    else:
        return 3

def format(file):
    contents = []
    item = ""
    while True:
        char = f.read(1)
        if not char:
            break
        item += char
        if char in ['t','c','p','d']:
            contents.append(item)
            item = ""

    return contents

def score(input, scores=[0,0]):
    item = input.pop()
    scores[(int(item[1])-1)] += interpretScore(item[2])
    if input != []:
        scores = score(input,scores)
    return scores

parser = argparse.ArgumentParser(description='Return Rugby Scores from Files')
parser.add_argument('source', type=str,help='Path to source folder')
parser.add_argument('output', type=str, help='Path to destination folder')
args = parser.parse_args()

if not args.source.endswith("/"):
    args.source += "/"
if not args.output.endswith("/"):
    args.output += "/"

os.makedirs(args.output, exist_ok=True)

print(args.source)

for filename in os.listdir(args.source):
    f=open(args.source+filename, "r")
    input = format(f)
    f.close()

    print(input)
    scores = score(input)
    f=open(args.output+filename[:-4]+"_b88575jh.txt", "w")
    f.write(str(scores[0])+":"+str(scores[1]))
    f.close()
