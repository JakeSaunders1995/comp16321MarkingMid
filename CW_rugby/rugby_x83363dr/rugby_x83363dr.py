import argparse, re, os, pathlib

parser = argparse.ArgumentParser(description="Need a input and output file")
parser.add_argument("inputFileDirectory", type=str)
parser.add_argument("outputFileDirectory", type=str)
args = parser.parse_args()

inputDirectory = args.inputFileDirectory
outputDirectory = args.outputFileDirectory

for file in os.listdir(inputDirectory):
    if file.endswith(".txt"):
        inputFilePath = inputDirectory + "/" + file
        outputFilePath = (
            outputDirectory + "/" + file.split(".")[0] + " _x83363dr" + ".txt"
        )
        scores = ""
        with open(inputFilePath, "r") as f:
            scores = f.read()
        scores = re.findall(r"[1|2][t|c|p|d]", scores)
        finalScore = [0, 0]
        for item in scores:
            i = 0 if item[0] == "1" else 1
            if item[1] == "t":
                finalScore[i] += 5
            elif item[1] == "d" or item[1] == "p":
                finalScore[i] += 3
            else:
                finalScore[i] += 2
        outputFileContents = str(finalScore[0]) + ":" + str(finalScore[1])
        pathlib.Path(outputDirectory).mkdir(parents=True, exist_ok=True)
        with open(outputFilePath, "w") as f:
            f.write(outputFileContents)
