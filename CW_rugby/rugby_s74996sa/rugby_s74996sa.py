import sys
import argparse
import os

def brain():
    if empty[0][x] == 't':
        if empty[0][x - 1] == '1':
            points['T1']+=5
        if empty[0][x - 1] == '2':
            points['T2']+=5
    elif empty[0][x] == 'p':
        if empty[0][x - 1] == '1':
            points['T1']+=3
        if empty[0][x - 1] == '2':
            points['T2']+=3
    elif empty[0][x] == 'd':
        if empty[0][x - 1] == '1':
            points['T1']+=3
        if empty[0][x - 1] == '2':
            points['T2']+=3
    elif empty[0][x] == 'c':
        if empty[0][x - 1] == '1':
            points['T1']+=2
        if empty[0][x - 1] == '2':
            points['T2']+=2


parser = argparse.ArgumentParser()

parser.add_argument('file', type=argparse.FileType('r'))
parser.add_argument('outfile', type=argparse.FileType('w'))

agp = parser.parse_args()

empty = []

for line in agp.file:
     empty.append(line)

points = {'T1': 0, 'T2': 0}

for x in range(len(empty[0])):
    brain()

agp.outfile.write(str(points['T1']) + ':' + str(points['T2']))

