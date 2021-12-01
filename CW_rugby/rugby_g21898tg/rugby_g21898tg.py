import argparse
import os
import sys

#command-line argument parser
argp = argparse.ArgumentParser(description='Input a file in the format T1xT2x')
argp.add_argument('Input', metavar='input_path', type=str,
                    help='input folder')
argp.add_argument('Output', metavar='output_path', type=str,
                    help='output folder')

args = argp.parse_args()
inputPath = args.Input
outputPath = args.Output

#check if file exists
if not os.path.isdir(inputPath):
    print("Input directory does not exist...")
    sys.exit()
elif not os.path.isdir(outputPath):
    print("Creating output directory")
    os.makedirs(outputPath)

#checks if the file is in the correct format
def formatCheck(fileContent):
    print(fileContent)
    if len(fileContent) % 3 != 0:
        print("File not in correct format")
    elif not ("T1" in fileContent or "T2" in fileContent):
        if input("File doesn't contain references to team. Is this a no scoring game y/n? ").lower() == "n":
            print("File not in correct format. Skipping. \n")
        else:
            return 0,0
    else:
        return scoreGen(fileContent)

#generates scores for each team
def scoreGen(textScores):
    T1, T2 = 0, 0
    for i in range(0, len(textScores), 3):
        team = textScores[i:i+2].upper()
        score = textScores[i+2].lower()

        if score == "t": score = 5
        elif score == "c": score = 2
        elif score == "p": score = 3
        elif score == "d": score = 3
        else: continue

        if team == "T1": T1 += score
        elif team == "T2": T2 += score
        else: continue
    return T1, T2

#formats and outputs final file
def outputFormat(T1Score, T2Score, filePath):
    outputText = "{0}:{1}".format(T1Score, T2Score)
    with open(filePath, 'w') as f:
        f.write(outputText)
    print("Output File Created at: {} \n".format(filePath))

#the starting procedure
files = os.listdir(inputPath)
for x in files:
    with open("{}/{}".format(inputPath, x), 'r') as f:
        score = formatCheck(f.read())
        if score is None:
            continue
        else:
            outputFormat(score[0], score[1], "{}/{}".format(outputPath, x))