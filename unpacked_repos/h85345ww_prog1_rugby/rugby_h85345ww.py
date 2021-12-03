import os
import argparse
from os import listdir, path
import os.path

parser = argparse.ArgumentParser()
parser.add_argument("input_folder_path", type = str)
parser.add_argument("output_folder_path", type = str)
args=parser.parse_args()
inputpath = args.input_folder_path
outputpath = args.output_folder_path

filenames = listdir(inputpath)
for k in range(len(filenames)):
    teams = open(inputpath + filenames[k], "r")
    winner = open(outputpath + filenames[k], "w")
    for line in teams:
        line = line.rstrip()
    t1score = 0
    t2score = 0
    i = 0
    while i < len(line):
        if line[i] == "T":
            if line[i + 1] == "1":
                if line[i + 2] == "t":
                    t1score += 5 
                if line[i + 2] == "p" or line[i + 2] == "d":
                    t1score += 3
                if line[i + 2] == "c":
                    t1score += 2      
            if line[i + 1] == "2":
                if line[i + 2] == "t":
                    t2score += 5
                if line[i + 2] == "p" or line[i + 2] == "d":
                    t2score += 3
                if line[i + 2] == "c":
                    t2score += 2
        i += 3
    winner.write(str(t1score) + ":" + str(t2score))

winner.close()
for k in range(len(filenames)):
    oldname = filenames[k].strip("/").split(".")
    os.rename(outputpath + filenames[k], outputpath + oldname[0] + '_h85345ww.txt')