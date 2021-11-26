import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("inputfolder")
parser.add_argument("outputfolder")
args = parser.parse_args()

def AccessFolder(ifolder, ofolder):
    for file in sorted(os.listdir(ifolder)):
        T1Score, T2Score = getScores(os.path.join(ifolder, file))
        filename = os.path.basename(os.path.join(ifolder, file))
        prefix = filename.split(".txt")
        outputFileName = prefix[0] + "_r94627as.txt"
        print(outputFileName)
        WriteFile(ofolder, outputFileName, T1Score, T2Score)
def getScores(file):
    with open(file) as scoresFile:
        gameEvents = scoresFile.read()

    print(gameEvents)
    T1Score = 0
    T2Score = 0
    for n in range(len(gameEvents)):
        print(gameEvents[n])
        if gameEvents[n] == "1":
            if gameEvents[n+1] == "t":
                T1Score += 5
            elif gameEvents[n+1] == "c":
                T1Score += 2
            elif gameEvents[n+1] == "p" or gameEvents[n+1] == "d":
                T1Score += 3
        elif gameEvents[n] == "2":
            if gameEvents[n+1] == "t":
                T2Score += 5
            elif gameEvents[n+1] == "c":
                T2Score += 2
            elif gameEvents[n+1] == "p" or gameEvents[n+1] == "d":
                T2Score += 3
    print(T1Score)
    print(T2Score)


    if T1Score > T2Score:
        print("Team 1 defeated Team 2")
    elif T1Score ==  T2Score:
        print("Team 1 Drew with Team 2")
    else:
        print("Team 2 defeated Team 1")
    scoresFile.close()

    return T1Score, T2Score

def WriteFile(outputFolder, outputFileName, T1Score, T2Score):
    with open(os.path.join(outputFolder, outputFileName), "w") as resultFile:
        resultFile.write(str(T1Score)+":"+str(T2Score))
    resultFile.close()


AccessFolder(args.inputfolder, args.outputfolder)
