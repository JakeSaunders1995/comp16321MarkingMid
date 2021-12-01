import os
o = 3
f = 0

filepa = input("please input and output file path: ")
filepath= filepa.split()
filepath1 = filepath[0]
outputinp = filepath[1]

realdirect = os.listdir(filepath1)

coolerreal = (filepath1 + ("\\"))
coolerreal.strip()
coolerreal1 = coolerreal + realdirect[0]


reallen = len(realdirect)

while reallen != f:
    sickbeans = coolerreal + realdirect[f]
    newlist = []
    rfile = open(sickbeans,"r")
    for line in rfile:
        for character in line:
            newlist.append(character)
    s = len(newlist)
    output=[newlist[i:i+o] for i in range(0,s,o )]
    cool = 0
    faster = s/3
    team1 = 0
    team2 = 0
    while cool != faster:
        bean1 = output[cool]
        if bean1[1] == ("1"):
            x = bean1[2]
            if x == ("t"):
                team1 = team1 + 5
            elif x == ("c"):
                team1 = team1 + 2
            elif x == ("p"):
                team1 = team1 + 3
            elif x == ("d"):
                team1 = team1 + 3
        elif bean1[1] == ("2"):
            x = bean1[2]
            if x == ("t"):
                team2 = team2 + 5
            elif x == ("c"):
                team2 = team2 + 2
            elif x == ("p"):
                team2 = team2 + 3
            elif x == ("d"):
                team2 = team2 + 3
        cool = cool + 1
    overallscore = (str(team1)+":"+str(team2))
    replacedoverallscore =  overallscore.strip(" ' ")
    calc = f +1
    otfilenam = (("test_file")+(str(calc))+("_j79871am.txt"))
    outp = os.path.join(outputinp,otfilenam)
    opres = open(outp,"w")
    finalscore = repr(replacedoverallscore)
    opres.write(finalscore)
    opres.close()
    f = f+1

