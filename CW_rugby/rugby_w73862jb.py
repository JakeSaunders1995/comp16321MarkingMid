import argparse, os

parser = argparse.ArgumentParser()
parser.add_argument('input')
parser.add_argument('output')
args = parser.parse_args()

inputfolder = args.input
outputfolder = args.output
inputfiles = os.listdir(inputfolder)

def scoring(char):
    if char == "t":
        return 5
    if char == "c":
        return 2
    if char == "p":
        return 3
    if char == "d":
        return 3

for i in inputfiles:

    filepath = os.path.join(inputfolder, i)
    currentfile = open(filepath)
    inputtext = currentfile.read()
    currentfile.close()

    team1score = 0
    team2score = 0
    a = 0
    while a < len(inputtext):
        if inputtext[a] == "1":
           team1score += scoring(inputtext[a + 1])
        elif inputtext[a] == "2":
           team2score += scoring(inputtext[a + 1])
        a += 1

    print("in the file " + i + "...")
    if team1score > team2score:
        print("team 1 is the winner")
    elif team2score > team1score:
        print("team 2 is the winner")
    elif team1score == team2score:
        print("team 1 and team 2 have tied")

    finalscore = str(team1score) + ":" + str(team2score)

    outputname = i[:-4] + "_w73862jb.txt"
    outputpath = os.path.join(outputfolder, outputname)

    outputfile = open(outputpath, "w")
    outputfile.write(finalscore)
    outputfile.close()





