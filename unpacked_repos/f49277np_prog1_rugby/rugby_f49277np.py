import sys
import os
path = sys.argv[1]
filelist=[]
files=os.listdir(path)
for f in files:
        filelist.append(f)
for x in filelist:
    file = open(str(path)+x, "r")
    points = file.read()
    file.close()
    team1total= 0
    team2total= 0
    for i in points:
        if i.isdigit()==True:
            currentTeam=int(i)
        elif i.islower()==True:
                if i== "t":
                    if currentTeam==1:
                        team1total += 5
                    else:
                        team2total += 5

                elif i== "c":
                    if currentTeam==1:
                        team1total += 2
                    else:
                        team2total += 2

                else:
                    if currentTeam==1:
                        team1total += 3
                    else:
                        team2total += 3
        else:
            pass
    out= str(x)
    index = out.find('.txt')
    outfile = out[:index]+"_f49277np.txt"
    outpath = str(sys.argv[2])+outfile
    file = open(outpath, "x")
    file.write(str(team1total)+":"+str(team2total))
    file.close()
