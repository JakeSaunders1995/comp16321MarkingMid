import sys
import os
LoadFile = sys.argv[1]
OutputFile = sys.argv[2]
username = "_z54873hs.txt"
team1= ""
team2= ""
team1score= 0
team2score= 0
t = 5
c = 2
p = 3
d = 3

for path , dir ,files in os.walk(LoadFile):
    Files = (files)


for j in Files:
    file = open(rf"{LoadFile}/{j}","r")


    for x in file:
        for i in range (len(x)):
            if x[i] == "1":
                team1 += x[i+1]

            elif x[i]=="2":
                team2+= x[i+1]
    team1score =0
    for x in team1:

        for i in range (len(x)):

            if x == "t":
                team1score = team1score + t
            if x == "c":
                team1score = team1score + c
            if x == "p":
                team1score = team1score + p
            if x == "d":
                team1score = team1score + d
    team2score= 0
    for x in team2:

        for i in range (len(x)):

            if x == "t":
                team2score = team2score + t
            if x == "c":
                team2score = team2score + c
            if x == "p":
                team2score = team2score + p
            if x == "d":
                team2score = team2score + d

    g = j.split(".")
    fn = os.path.join(OutputFile,g[0]+username)
    OutFile=open(f"{OutputFile}/{g[0]}{username}","w")
    team1=""
    team2=""
    OutFile.write(str(team1score)+":"+str(team2score))

    OutFile.close()
    if team1score < team2score:
        print("Team 2 wins")
    if team1score > team2score:
        print("Team 1 wins")
    if team1score==team2score:
        print("It is a draw")
