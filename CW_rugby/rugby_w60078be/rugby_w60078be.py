import argparse
import os


parser = argparse.ArgumentParser()      #argument setup
parser.add_argument("inputs")
parser.add_argument("outputs")
args = parser.parse_args()
#arg2 = parser.parse_args()




pathIn = args.inputs                #accepts argument 1 and argument 2 and assigns them as the path to folder
pathOut = args.outputs
fileNames = os.listdir(pathIn)
#print(fileNames)

for j in fileNames:
    #print(j)
    textIn = pathIn+"/"+j
    file = open(textIn,"r")
    score = file.read()
    file.close()


    #score = "T1tT2pT2pT1pT1d"      #For testing

    tPos = 1                                #Initialisation
    sPos = 2
    team1 = 0
    team2 = 0

    scoring = {
        "t": 5,
        "c": 2,
        "p": 3,
        "d": 3
    }

    while tPos<len(score)-1:                #Determine who gets point
        if score[tPos] == "1":
            team1 += scoring[score[sPos]]
        else:
            team2 += scoring[score[sPos]]
        tPos += 3
        sPos += 3
        
    if team1 > team2:                       #Determine winner
        result = "T1 wins"  
    elif team1 == team2:
        result = "draw"
    else:
        result = "T2 wins"
    



    #Create text documents with correct file name
    txtStripped = j.replace(".txt","")  #removes.txt from input file so username can be added
    textOut = pathOut +"/"+txtStripped+"_w60078be.txt"
    #print(textOut)
    
    file = open(textOut,"w")                #creates file with score in it
    file.write(str(team1)+":"+str(team2))
    file.close()
