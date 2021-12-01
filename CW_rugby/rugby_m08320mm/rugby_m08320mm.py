import argparse
import os
parser = argparse.ArgumentParser()
try:
    parser.add_argument('inputFile')
    parser.add_argument('outputFile')
    args = parser.parse_args()
except:
    print("List arguments in the form: python3 rugby_m08320mm.py [input file path] [output file path]")
    exit()


def processFile(game):
    #score counters
    score=0
    t1Score=0
    t2Score=0

    #loops through input file in sections of 3
    i = 0
    for i in range(int(len(game)/3)):
        #calculates amount of points scored for section
        pointType = game[i*3+2]
        if(pointType=="p" or pointType=="d"):
            score=3
        elif(pointType=="c"):
            score=2
        elif(pointType=="t"):
            score=5
        else:
            print("Unexpected input format")
            exit()
        #awards points to relevant team
        team = game[i*3:i*3+2]
        if(team=="T1"):
            t1Score+=score
        elif(team=="T2"):
            t2Score+=score
        else:
            print("Unexpected input format")
            exit()
        i+=3

    #Calculates and prints result
    result=str(t1Score)+":"+str(t2Score)
    if(t1Score>t2Score):
        print("The score is "+result+", Team 1 wins")
    elif(t2Score>t1Score):
        print("The score is "+result+", Team 2 wins")
    else:
        print("The score is "+result+", it's a draw")
    return result

#folder file
for file in os.listdir(args.inputFile):
    #checks if text file
    if file.endswith(".txt"):
        print("\n"+file)
        #reads file
        currentPath = os.path.join(args.inputFile, file)
        f = open(currentPath, "r")
        new = f.read()
        f.close()
        result = processFile(new)
        #writes to new file
        newPath = os.path.join(args.outputFile, file[0:-4]+"_m08320mm.txt")
        f = open(newPath, "w")
        f.write(result)
        f.close()
