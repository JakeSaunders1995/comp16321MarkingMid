import argparse
from argparse import ArgumentParser
import os

def validateFilePath(f):
    if not os.path.exists(f):
        raise argparse.ArgumentTypeError("The filepath {0} does not exist. Please enter a valid filepath".format(f))
    return f

#COMMAND LINE INPUT
parser = argparse.ArgumentParser()
parser = argparse.ArgumentParser()
parser.add_argument('inpFold', type=str, help="Input file/test txt file path")
parser.add_argument('outFold', type=str, help="Output file/output txt path")
args = parser.parse_args()
validateFilePath(args.inpFold)
validateFilePath(args.outFold)
inpFile=""

for filename in os.listdir(args.inpFold):#Get the amount of files within the folder
    if filename.endswith(".txt"):#that are input files

        inpFile=(os.path.join(args.inpFold, filename))
        filename=filename[:-4]+"_r61875lj.txt"
        outFile=(os.path.join(args.outFold, filename))

        inputFile = open(inpFile, "rt")
        file = inputFile.read()
        Team1 = 0
        Team2 = 0
        while(file!=""):
            score=0
            if(file[2]=="t"):score=5
            elif(file[2]=="c"):score=2
            elif(file[2]=="p"):score=3
            elif(file[2]=="d"):score=3
            if(file[1]=="1"):Team1+=score
            elif(file[1]=="2"):Team2+=score
            file=file[3:]

        score=str(Team1)+":"+str(Team2)

        outputText = open(outFile, "w")
        outputText.writelines(score)
        outputText.close()
