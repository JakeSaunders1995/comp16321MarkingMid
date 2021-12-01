import sys

def scoreType(type):
    if(type == "t"):
        return int(5)
    elif(type == "c"):
        return int(2)
    elif(type == "p"):
        return int(3)
    elif(type == "d"):
        return int(3)

inputFile = sys.argv[1]
outputFile = sys.argv[2]

inputF = open(inputFile, "r")
outputF = open(outputFile, "w")

scores = inputF.read()
team1score = 0
team2score = 0

for i in range(len(scores)):
    team = scores[i:i+2]
    if(team == "T1"):
        team1score = team1score + scoreType(scores[i+2])
    elif(team == "T2"):
        team2score = team2score + scoreType(scores[i+2])
    i += 2

if(team1score > team2score):
    print("The winner is Team 1!")
elif(team2score > team1score):
    print("The winner is Team 2!")
else:
    print("It is a draw!")

outputF.write(str(team1score) + ":" + str(team2score))
