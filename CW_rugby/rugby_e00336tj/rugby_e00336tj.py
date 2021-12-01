import sys
username = "_e00336tj"
fileList = []
index = 0
for file in sys.argv[1:]:
    if username in file:
        index = sys.argv[1:].index(file.replace(username,""))
        filePair = [sys.argv[1:][index],file]
        fileList.append(filePair)
for pair in fileList:
    inputFile = open(pair[0],'r')
    scorecount = inputFile.read()
    outputFile = open(pair[1],'w')
    team1=0
    team2=0 
    rules = [['d',3],['p',3],['c',2],['t',5]]
    for i in range(len(scorecount)):
        if scorecount[i]=="T":
            for j in rules:
                if j[0] == scorecount[i+2]:
                    points=j[1]
            if scorecount[i+1] == "1":
                team1 += points
            if scorecount[i+1] == "2":
                team2+=points
    if team1>team2:
        winner="Team 1"
    if team1<team2:
        winner="Team 2"
    else:
        winner="it's a draw"
    finalscore = str(team1)+':'+str(team2)
    outputFile.write(finalscore)
    inputFile.close()
    outputFile.close()