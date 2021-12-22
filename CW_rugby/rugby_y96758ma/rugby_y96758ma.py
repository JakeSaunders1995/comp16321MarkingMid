import sys
filename = sys.argv[-2]
filename2 = sys.argv[-1]
f = open(filename, 'r')
teamscoring=(f.readline()).strip()
2, 5, 8, 11,
run = len(teamscoring)
i=0
team1score = 0
team2score = 0
while i < run/3:
    char=1+(3*i)
    score=2+(3*i)
    if (teamscoring[char]) == "1":
        if (teamscoring[score]) == "t":
            team1score+=5
        elif (teamscoring[score]) == "c":
            team1score+=2
        elif (teamscoring[score]) == "p":
            team1score+=3
        elif (teamscoring[score]) == "d":
            team1score+=3
    elif (teamscoring[char]) == "2":
        if (teamscoring[score]) == "t":
            team2score+=5
        elif (teamscoring[score]) == "c":
            team2score+=2
        elif (teamscoring[score]) == "p":
            team2score+=3
        elif (teamscoring[score]) == "d":
            team2score+=3
    i+=1
if team1score<team2score:
    print("Team 2 has won!")
elif team2score<team1score:
    print("Team 1 has won!")
else:
    print("There is a draw!")
ratio=(str(team1score)+":"+str(team2score))
store = open(filename2, 'w')
store.write(ratio)
store.close()
f.close()
