#!/usr/bin/env python3

'''
COMP16321 Mid Term
Program 1 - Rugby
Felix Waller
'''

import os
import argparse

def getOutputFile(inputFileName, outputFolder): 
    return outputFolder + ("" if outputFolder[-1] == "/" else "/") + inputFileName[0 : inputFileName.find(".txt")] + "_g75462fw.txt"

def rugby(inputFilePath, inputFileName, outputFolder):
    with open(inputFilePath) as file:
        input = file.read()[1:].split("T")

    team1, team2 = 0, 0

    for i in input:
        if i[1] == "t":
            score = 5
        elif i[1] == "c":
            score = 2
        else:
            score = 3
        
        if i[0] == "1":
            team1 += score
        else:
            team2 += score

    with open(getOutputFile(inputFileName, outputFolder), "w") as file:
        file.write(f"{team1}:{team2}")

parser = argparse.ArgumentParser()
parser.add_argument("inputFolder")
parser.add_argument("outputFolder")
args = parser.parse_args()

for entry in os.scandir(args.inputFolder):
    if ".txt" in entry.name:
        rugby(entry.path, entry.name, args.outputFolder)
