import sys

file = open(sys.argv[1],"r")  
Scores = file.read()
file.close()
team1Score = 0
team2Score = 0     #Set variables for score of each team and Scores to equal the Input file
wTeam = ""      #Variable to be used when determining which team
wScore = ""     #Variable to be used when determining which score e.g. if it was a try
num = 0

for i in range(len(Scores)):    #As Scores is effectively one word in the way they are written in the test files 
    if Scores[i] == "1":           #We can use a for loop and have it set to the length of Scores
        num = i + 1
        if Scores[num] == "t":
            team1Score += 5
        elif Scores[num] == "c":
            team1Score += 2
        else:
            team1Score += 3                        
    elif Scores[i] == "2":
        num = i + 1
        if Scores[num] == "t":
            team2Score += 5
        elif Scores[num] == "c":        #Algorithm to run through whether it is team 1 or team 2 scoring and 
            team2Score += 2             #How many points to award
        else:
            team2Score += 3

file = open(sys.argv[2],"w")
file.write("%s %s %s" %(team1Score,":",team2Score))
file = open(sys.argv[2])                 #Writing the score into an output file   
file.close()

