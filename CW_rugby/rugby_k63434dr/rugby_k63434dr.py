import argparse
import sys
import os

parser = argparse.ArgumentParser()
parser.add_argument("inputDirectory")
parser.add_argument("outputDirectory")
parsed_args = parser.parse_args(sys.argv[1:])

scoreDict = {'t': 5, 'c': 2, 'p': 3, 'd': 3}


def scoreAdd(scores):
    T1, T2 = 0, 0
    for i, char in enumerate(scores):
        if char == 'T':
            T1 = T1 + scoreDict[scores[i + 2]] if scores[i + 1] == '1' else T1
            T2 = T2 + scoreDict[scores[i + 2]] if scores[i + 1] == '2' else T2
    return f'{T1}:{T2}'


def getFiles(dirPath):
    return next(os.walk(dirPath))[2]


files = getFiles(parsed_args.inputDirectory)
for file in files:
    inp = open(f"{parsed_args.inputDirectory}\{file}", 'r')
    out = open(f"{parsed_args.outputDirectory}\{file.replace('.txt, ''')}_k63434dr.txt", 'w+')
    out.write(scoreAdd(inp.read()))
    out.close()
