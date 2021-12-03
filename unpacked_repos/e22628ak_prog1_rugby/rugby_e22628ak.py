import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('inputf', type=str)
parser.add_argument('outputf', type=str)
args = parser.parse_args()
inputfiles = os.listdir(args.inputf)
for file in inputfiles:
    fileloc = fr'{args.inputf}/{file}'
    outloc = fr'{args.outputf}/{file[: -4]}_e22628ak.txt'
    fin = open(fileloc ,'r')
    fout = open(outloc, 'w')
    line = fin.readline()
    inp = line.strip()
    playerscores = [0,0]
    for i,letter in enumerate(inp):
        if letter.isdigit() == True:
            pchoice = int(letter) - 1
            p = inp[i+1]
            if p == 't':
                playerscores[pchoice] += 5
            elif p == 'c':
                playerscores[pchoice] += 2
            elif p == 'p':
                playerscores[pchoice] += 3
            else:
                playerscores[pchoice] += 3
    output = f'{playerscores[0]}:{playerscores[1]}'
    fout.write(output)
    fin.close()
    fout.close()
    