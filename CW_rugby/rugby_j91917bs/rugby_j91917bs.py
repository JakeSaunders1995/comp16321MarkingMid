import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('inputfile', type=str, help="need input file")
parser.add_argument('outputfile', type=str, help="need output file")
args = parser.parse_args()

print(args.inputfile)
print(args.outputfile)

inputFile = args.inputfile


outputFile = args.outputfile


teamOnePoints = 0
teamTwoPoints = 0


for x in os.listdir(inputFile):
    file = os.path.join(inputFile, x)
    dpath = os.path.dirname(file)
    readFile = open(file, "r")
    results = readFile.readline()



    length = len(results)

    count = 1
    teamOnePoints = 0
    teamTwoPoints = 0
    winner = ""

    for i in range(length):

        if i % 3 == 1:
            print(results[i])
            team = int(results[i])
            if team == 1:
                if results[i + 1] == "t":
                    teamOnePoints += 5
                elif results[i + 1] == "c":
                    teamOnePoints += 2
                elif results[i + 1] == "p":
                    teamOnePoints += 3
                elif results[i + 1] == "d":
                    teamOnePoints += 3
            elif team == 2:
                if results[i + 1] == "t":
                    teamTwoPoints += 5
                elif results[i + 1] == "c":
                    teamTwoPoints += 2
                elif results[i + 1] == "p":
                    teamTwoPoints += 3
                elif results[i + 1] == "d":
                    teamTwoPoints += 3
            else:
                print("error in scores")
        else:
            continue

        if teamOnePoints > teamTwoPoints:
            winner += "Team One"
        elif teamTwoPoints > teamOnePoints:
            winner += "Team Two"
        else:
            winner += "tie"
        print(winner)

    if outputFile[-1] != "/":
        outputName = outputFile + "/" + x.split(".txt")[0] + "_j91917bs.txt"
        outFile = outputName
        dir = os.path.dirname(outFile)
        print(dir)
    else:
        outputName = outputFile + x.split(".txt")[0] + "_j91917bs.txt"
        outFile = outputName
        dir = os.path.dirname(outputFile)

    if not os.path.exists(dir):
        os.makedirs(dir)


    scoresFinal = open(outFile, "w")
    scoresFinal.write(str(teamOnePoints) + ":" + str(teamTwoPoints))
    scoresFinal.close()
    count += 1
