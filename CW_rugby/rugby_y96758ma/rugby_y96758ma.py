import os
import sys


folder=sys.argv[-2]
folderlist = (os.listdir(folder))
folderlist.sort()
folder2=sys.argv[-1]
folderlist2 = os.listdir(folder2)

for folders in folderlist:
    i_file = open(os.path.join(folder, folders))
    readdd = (i_file.readline()).strip()
    folderstring=folders.replace(".txt","_y96758ma.txt")
    run = len(readdd)
    i=0
    team1score = 0
    team2score = 0
    while i < run/3:
        char=1+(3*i)
        score=2+(3*i)
        if (readdd[char]) == "1":
            if (readdd[score]) == "t":
                team1score+=5
            elif (readdd[score]) == "c":
                team1score+=2
            elif (readdd[score]) == "p":
                team1score+=3
            elif (readdd[score]) == "d":
                team1score+=3
        elif (readdd[char]) == "2":
            if (readdd[score]) == "t":
                team2score+=5
            elif (readdd[score]) == "c":
                team2score+=2
            elif (readdd[score]) == "p":
                team2score+=3
            elif (readdd[score]) == "d":
                team2score+=3
        i+=1
    if team1score<team2score:
        print("Team 2 has won!")
    elif team2score<team1score:
        print("Team 1 has won!")
    else:
        print("There is a draw!")
    ratio=(str(team1score)+":"+str(team2score))
    o_file = open(os.path.join(folder2, folderstring), 'w')
    o_file.write(str(ratio))
