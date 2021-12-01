import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("inputDirectory")
parser.add_argument("outputDirectory")

args = parser.parse_args()

for filename in os.listdir(args.inputDirectory):
  filePath = os.path.join(args.inputDirectory,filename)
  if os.path.isfile(filePath):
    
    f = open(filePath, "r")
    string = f.read()
    f.close()

    team1Score = 0
    team2Score = 0

    prevChar = ""

    scoreChar = False
    for char in string:
      if scoreChar:
        points = 0
        if char == "t":
          points = 5
        elif char == "c":
          points = 2
        elif char == "p" or char == "d":
          points = 3

        if prevChar == "1":
          team1Score += points
        else:
          team2Score += points

      if prevChar == "T" and (char == "1" or char == "2"):
        scoreChar = True
      else:
        scoreChar = False

      prevChar = char

    output = str(team1Score) + ":" + str(team2Score)
      
    f = open(args.outputDirectory + "/" + filename[:-4] + "_p67189ml.txt", "w")
    f.write(output)
    f.close()