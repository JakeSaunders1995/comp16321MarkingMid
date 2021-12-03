import argparse
import os

parser = argparse.ArgumentParser()

parser.add_argument('input_folder')
parser.add_argument('output_folder')

args = parser.parse_args()

inputfolderpath = (args.input_folder)
outputfolderpath = (args.output_folder)

for files in os.listdir(inputfolderpath):
    inputfiles = open(inputfolderpath + "/" + files, "r")
    words = inputfiles.readline()
    text = files.split(".")

    reader = words
    #Initial Score
    T1score = 0;
    T2score = 0;

    #Starts at index 2 and increments by 3 for each score value
    for i in range(2,len(reader),3):

    #Team 2
        if reader[i-1] == "2":
            if reader[i] == "t":
                T2score += 5
            elif reader[i] == "c":
                T2score += 2
            elif (reader[i] == "p" or reader[i] == "d"):
                T2score += 3

    #Team 1
        else:
            if reader[i] == "t":
                T1score += 5
            elif reader[i] == "c":
                T1score += 2
            elif (reader[i] == "p" or reader[i] == "d"):
                T1score += 3


    outputfilename = text[0] + "_[n95301jf].txt"
    outputfiles = open(outputfolderpath + "/" + outputfilename, "w")
    outputfiles.write(str(T1score)+":"+str(T2score))
    outputfiles.close()

