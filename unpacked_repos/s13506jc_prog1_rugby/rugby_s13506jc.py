import argparse
from pathlib import Path

#Set up and parse command line arguments
rugbyParser = argparse.ArgumentParser('Input and output files.')
rugbyParser.add_argument("inputFolderPath", type=Path)
rugbyParser.add_argument("outputFolderPath", type=Path)
args = rugbyParser.parse_args()

#Set up scoring information
scoringDict = {"t": 5, "c": 2, "p": 3, "d": 3}

#Iterate through files in input folder
for file in args.inputFolderPath.glob('*'):
    #Reset scores
    scoresDict = {"1": 0, "2": 0}

    #Read input file
    try:
        with open(file, "r+") as inputFile:
            inputFileData = inputFile.read()
    except:
        print("Input file is not valid.")
        continue

    #Calculate the scores from the input data
    try:
        for n in range(0, len(inputFileData)//3):
            event = inputFileData[(3*n)+1:3*(n+1)]
            scoresDict[event[0]] += scoringDict[event[1]]
    except:
        print("Input file is incorrectly formatted.")
        continue

    #Assemble the final score into the desired format
    finalScore = str(scoresDict["1"]) + ":" + str(scoresDict["2"])

    #Write the final score to the output file
    try:
        args.outputFolderPath.mkdir(exist_ok=True)
        with open(args.outputFolderPath / str(file.stem + "_s13506jc.txt"), "w") as outputFile:
            outputFile.write(finalScore)
    except:
        print("Output folder path is not valid.")
        quit()

    #Compare scores to determine the winner
    print("The final score is " + finalScore + ".")
    if scoresDict["1"] > scoresDict["2"]:
        print("Team 1 wins!")
    elif scoresDict["1"] < scoresDict["2"]:
        print("Team 2 wins!")
    else:
        print("It's a draw!")
