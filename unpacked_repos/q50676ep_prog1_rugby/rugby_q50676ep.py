import os, re, sys
entries = os.listdir(sys.argv[1])
print(entries)
team1Score=0
team2Score=0
for i in range(len(entries)):
    print (entries[i])
    data = open(sys.argv[1] +"/" + entries[i])
    scores = data.read()
    print(scores)
    #TEAM 1 SCORING
    #tries
    team1Try = re.compile(r'T1t')
    tries1 = team1Try.finditer(scores)
    for match in tries1:
        team1Score= team1Score + 5
    #Goal KIck
    team1GK= re.compile(r'T1c')
    Gk1 = team1GK.finditer(scores)
    for match in Gk1:
        team1Score= team1Score + 2
    #Penalty
    team1Pens = re.compile(r'T1p')
    pens1 = team1Pens.finditer(scores)
    for match in pens1:
        team1Score= team1Score + 3
    #Drop Goal
    team1Dg = re.compile(r'T1d')
    Dgoals1 = team1Dg.finditer(scores)
    for match in Dgoals1:
        team1Score= team1Score + 3
    #Team 2 Scores
    team2Try = re.compile(r'T2t')
    tries2 = team2Try.finditer(scores)
    for match in tries2:
        team2Score= team2Score + 5
    #Goal KIck
    team2GK= re.compile(r'T2c')
    Gk2 = team2GK.finditer(scores)
    for match in Gk2:
        team2Score= team2Score + 2
    #Penalty
    team2Pens = re.compile(r'T2p')
    pens2 = team2Pens.finditer(scores)
    for match in pens2:
        team2Score= team2Score + 3
    #Drop Goal
    team2Dg = re.compile(r'T2d')
    Dgoals2 = team2Dg.finditer(scores)
    for match in Dgoals2:
        team2Score= team2Score + 3
    print("Team score 1 is " + str(team1Score))
    print("Team score 2 is " + str(team2Score))
    finalScores = open(sys.argv[2] + "/" + str(i) + "_q50676ep.txt" , "w") # allows us to writeover
    finalScores.write(str(team1Score) + ":" + str(team2Score))
    finalScores.close()
    team1Score= 0
    team2Score= 0
