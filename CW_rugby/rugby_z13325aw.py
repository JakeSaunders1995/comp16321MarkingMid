#Calculating Rugby Score Program: Final

import argparse, os, re

#Getting Args from the Terminal
parser = argparse.ArgumentParser()
parser.add_argument("input", type = str)
parser.add_argument("output", type = str)
args = parser.parse_args()

# Iterating through all Files in Input Folder
for file in os.listdir(args.input):
    
    # Check whether file is in text format or not
    if file.endswith(".txt"):
        file_path = f"{args.input}/{file}"
        
        #Reading File and Saving T1 and T1
        with open(file_path, "r") as f:
            score = f.read()
            T1regex = re.findall("T1t|T1c|T1p|T1d", score)
            T2regex = re.findall("T2t|T2c|T2p|T2d", score)

        #Declaring Variables
        T1score = 0
        T2score = 0
        
        #Calculating T1 Score
        for x in range(len(T1regex)):
            scoreBoard = T1regex[x] 
            if scoreBoard == "T1t":
                scoreBoard = 5
            elif scoreBoard == "T1c":
                scoreBoard = 2
            elif scoreBoard == "T1p" or scoreBoard == "T1d":
                scoreBoard = 3

            T1score = T1score + scoreBoard
      
        #Calculating T2 Score
        for y in range(len(T2regex)):
            scoreBoard = T2regex[y] 
            if scoreBoard == "T2t":
                scoreBoard = 5
            elif scoreBoard == "T2c":
                scoreBoard = 2
            elif scoreBoard == "T2p" or scoreBoard == "T2d":
                scoreBoard = 3

            T2score = T2score + scoreBoard

        #Finding Winner
        if T1score > T2score:
            Winner = "T1"
        elif T2score > T1score:
            Winner = "T2"
        elif T1score == T2score:
            Winner = "Draw"


        #Outputting File with T1score:T2score
        onlyName = os.path.splitext(file)[0] #Removes Extension from File Name
        newName = onlyName + "_z13325aw" + ".txt" 
        file_path = f"{args.output}/{newName}"
        with open(file_path, "w") as o:
            o.write(str(T1score) + ":" + str(T2score))









