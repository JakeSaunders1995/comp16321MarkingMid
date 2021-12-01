# python3 rugby_h86959th.py /home/csimage/16321_python_coursework_h86959th/midterm_files/Example_inputs/Example_inputs_program1 /home/csimage/16321_python_coursework_h86959th/midterm_files/Example_outputs/Example_outputs_program1
# python3 rugby_h86959th.py ./Example_inputs/Example_inputs_program1 ./Example_outputs/Example_outputs_program1
import argparse
from argparse import ArgumentParser
import os

parser = argparse.ArgumentParser() # argument setup
parser.add_argument('inputFolder', type=str, help="Input folder")
parser.add_argument('outputFolder', type=str, help="Output folder")
args = parser.parse_args()
inFile = ""


for filename in os.listdir(args.inputFolder): # goes thru all files in input folder
    if filename.endswith(".txt"): # goes thru all txt files

        inFile = (os.path.join(args.inputFolder, filename))
        filename = filename[:-4] + "_h86959th.txt" # removes txt and replace w ur username
        outFile = (os.path.join(args.outputFolder, filename))

        inputFile = open(inFile, "rt")
        temp = inputFile.read()

        t = 5
        c = 2
        p = 3
        d = 3

        team1 = 0

        t1 = temp.count("1t")
        team1 += t1 * t
        
        c1 = temp.count("1c")
        team1 += c1 * c

        p1 = temp.count("1p")
        team1 += p1 * p
        
        d1 = temp.count("1d")
        team1 += d1 * d

        team2 = 0

        t2 = temp.count("2t")
        team2 += t2 * t
        
        c2 = temp.count("2c")
        team2 += c2 * c

        p2 = temp.count("2p")
        team2 += p2 * p 

        d2 = temp.count("2d")
        team2 += d2 * d

        ratio = (str(team1) + ":" + str(team2))


        if team1 > team2:
            winner = "team 1"
        elif team2 > team1:
            winner = "team 2"
        else:
            winner = "draw"
            
        outputText = open(outFile, "w")
        outputText.write(ratio)
        outputText.close()

