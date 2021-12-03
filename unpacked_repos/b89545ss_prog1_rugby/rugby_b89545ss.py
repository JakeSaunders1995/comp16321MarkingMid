#rugby = open("test_file1.txt", "r")

#text = rugby.read()
#print(text)
import os
import sys
import glob
import argparse

from os.path import abspath
parser = argparse.ArgumentParser()
parser.add_argument("rugbyfile")
parser.add_argument("outputfile")

args = parser.parse_args()
inputPath = args.rugbyfile
outputPath = args.outputfile



rugbyfile = []
#for name in sys.argv[1:]:
    #for file in glob.glob(os.path.join(name, "*.txt")):
        #with open(file, "r") as f:
            #rugbyfile.append(f.read())
def rugbyscores(fpath):
    rugbyfilePosition = 0
    while (rugbyfilePosition < len(rugbyfile)):
        rugby = rugbyfile[rugbyfilePosition]
#import argparse
#from os import waitpid
#parser = argparse.ArgumentParser()
#parser.add_argument("inputfile")
#parser.add_argument("outputfile")
#args = parser.parse_args()
#all_files = os.listdir(args.inputfile)

#with open(args.inputfile) as input:
 #   rugby = input.read()

        T1 = 0
        T2 = 0
    #Types of scores in rugby
        t = 5 #try
        c = 2 #goalkick
        p = 3 #penalty
        d = 3 #dropgoal

        rugbyPosition = 0
        while (rugbyPosition < len(rugby)):
            if rugby[rugbyPosition] == "T":
                rugbyPosition = rugbyPosition + 1
            elif rugby[rugbyPosition] == "1":
                rugbyPosition = rugbyPosition + 1
            if rugby[rugbyPosition] == "t":
                T1 = T1 + t
                rugbyPosition = rugbyPosition + 1
            elif rugby[rugbyPosition] == "c":
                T1 = T1 + c
                rugbyPosition = rugbyPosition + 1
            elif rugby[rugbyPosition] == "p":
                T1 = T1 + p
                rugbyPosition = rugbyPosition + 1
            elif rugby[rugbyPosition] == "d":
                T1 = T1 + d
                rugbyPosition = rugbyPosition + 1

            elif rugby[rugbyPosition] == "2":
                rugbyPosition = rugbyPosition + 1
            if rugby[rugbyPosition] == "t":
                T2 = T2 + t
                rugbyPosition = rugbyPosition + 1
            elif rugby[rugbyPosition] == "c":
                T2 = T2 + c
                rugbyPosition = rugbyPosition + 1
            elif rugby[rugbyPosition] == "p":
                T2 = T2 + p
                rugbyPosition = rugbyPosition + 1
            elif rugby[rugbyPosition] == "d":
                T2 = T2 + d
                rugbyPosition = rugbyPosition + 1

        print(str(T1) + ":" + str(T2))

        username = "b89545ss"
        Results = str(T1) + ":" + str(T2)

        if (T1 > T2):
            print("Team 1 won the game")
        elif (T2 > T1):
            print("Team 2 won the game")
        else:
            print("It was a draw")


        rugbyfilePosition = rugbyfilePosition + 1

    os.chdir(outputPath)
    Results = open(f[:-4] + "_b89545ss.txt", "w")
    Results.write(username)
    Results.write(Results)

    Results.close()




    for f in os.listdir(inputPath):
        if f.endswith(".txt"):
            fpath = f"{inputPath}/{f}"
            print(fpath)
            file = open(fpath, "r")
            txt = file.read()
            file.close
            run = rugbyscores(fpath)
