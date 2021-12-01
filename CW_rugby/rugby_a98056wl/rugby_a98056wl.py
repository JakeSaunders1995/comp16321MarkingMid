import sys, os

# read command line arguments
inputDirectory = sys.argv[1]
outputDirectory = sys.argv[2]

# go through each character
# if it is a number, change the current team
# if it is a letter (excluding "T"), add appropriate score
def CalculateScores(data):
    scores = [0, 0]
    currentTeam = 0
    for char in data:
        if char == "T": continue
        if char.isnumeric():
            currentTeam = int(char) - 1
        else:
            if char == "t":
                scores[currentTeam] += 5
            elif char == "c":
                scores[currentTeam] += 2
            else:
                scores[currentTeam] += 3
    return scores

def GetOutput(data):
    scores = CalculateScores(data)
    return f"{scores[0]}:{scores[1]}"

# read & write final scores to files
for root, dirs, files in os.walk(inputDirectory):
    for fileName in files:
        inputPath = inputDirectory + "/" + fileName
        outputPath = outputDirectory + "/" + fileName[:-4] + "_a98056wl.txt"

        file = open(inputPath)
        data = file.readline().replace("\n", " ").strip()
        file.close()
        outputText = GetOutput(data)

        file = open(outputPath, "w")
        file.write(outputText)
        file.close()
