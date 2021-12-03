import argparse, os, os.path, re
parser = argparse.ArgumentParser()
parser.add_argument("inputfolder")
parser.add_argument("outputfolder")
args = parser.parse_args()

infile = args.inputfolder
pathlist = os.listdir(infile)

#t = 5
#c = 2
#p = 3
#d = 3
for file in pathlist:
    filepath = os.path.join(infile, file)
    team1score = 0
    team2score = 0
    Team1 = []
    Team2 = []
    f=open(filepath, 'r')
    str = f.read()
    list = re.split(r'T', str)
    for n in range(1,len(list)):
        if list[n][0] == "1":
            Team1.append(list[n][1])
        elif list[n][0] == "2":
            Team2.append(list[n][1])
    for m in range(0,len(Team1)):
        if Team1[m] == "t":
            team1score += 5
        elif Team1[m] == "c":
            team1score += 2
        elif Team1[m] == "p":
            team1score += 3
        elif Team1[m] == "d":
            team1score += 3
    for a in range(0,len(Team2)):
        if Team2[a] == "t":
            team2score += 5
        elif Team2[a] == "c":
            team2score += 2
        elif Team2[a] == "p":
            team2score += 3
        elif Team2[a] == "d":
            team2score += 3
    f.close()
    name, ext = os.path.splitext(file)
    name += "_p56781ng" + ext
    output = os.path.join(args.outputfolder, name)
    winner = open(output, 'w')
    winner.write("%d:%d" % (team1score, team2score))
    winner.close()

