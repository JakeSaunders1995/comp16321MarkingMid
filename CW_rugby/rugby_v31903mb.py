import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("input", help="Input directory. Directory is scanned for valid input files.")
parser.add_argument("output", help="Output directory. Output files are written to directory. Will overwrite file if it already exists.")
args = parser.parse_args()
scores = {"t": 5, "c": 2, "p": 3, "d": 3}

files = os.scandir(args.input)
for file in files:
    if not file.is_file() or file.name[-4:] != ".txt":
        continue
    text = ""
    with open(file.path) as f:
        text = f.read()

    teamOneScore = 0
    teamTwoScore = 0
    for i in range(0, int(len(text)/3)):
        invalidFile = False
        team = text[i*3:i*3+2]
        scoreType = text[i*3+2:i*3+3]
        if scoreType not in scores.keys():
            invalidFile = True
            break
        if team == "T1":
            teamOneScore += scores[scoreType]
        elif team == "T2":
            teamTwoScore += scores[scoreType]
        else:
            invalidFile = True
            break
    if invalidFile:
        continue

    if teamOneScore == teamTwoScore:
        print(f"It was a draw, the score was {teamOneScore}:{teamTwoScore}.")
    elif teamOneScore > teamTwoScore:
        print(f"Team one won, the score was {teamOneScore}:{teamTwoScore}.")
    else:
        print(f"Team two won, the score was {teamOneScore}:{teamTwoScore}.")
        
    fileName = os.path.join(args.output, file.name[:-4] + "_v31903mb.txt")
    os.makedirs(os.path.dirname(fileName), exist_ok=True)
    with open(fileName, "w") as f:
        f.write(f"{teamOneScore}:{teamTwoScore}")