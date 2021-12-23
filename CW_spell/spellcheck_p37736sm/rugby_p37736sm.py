import sys
print("argument list: ", str(sys.argv))

infile = sys.argv[1]
outfile = sys.argv[2]
infile = open(infile, "r")
string = infile.read()
print(string)

#decode string
T1Score = 0
T2Score = 0

for i in range(len(string)):
    print("I = "+str(i))
    if string[i] == "T":
        i += 1
        team = string[i]
        print("Team is "+str(team))

        i += 1
        scoreType = string[i]
        print("Score type: "+str(scoreType))
        #decode to num of points
        if(scoreType == "t"):
            score = 5
        elif(scoreType =="c"):
            score = 2
        elif(scoreType == "p" or scoreType == "d"):
            score = 3
        print("Score: "+str(score))

        if(team == "1"):
            T1Score += score
            print("Added "+str(score)+" to team 1. for a total of "+str(T1Score))
        elif(team == "2"):
            T2Score += score
            print("Added "+str(score)+" to team 2. for a total of "+str(T2Score))

        else:
            print("ERROR: Team not valid")

print("Team 1 Final score = "+str(T1Score))
print("Team 2 Final score = "+str(T2Score))

outString = str(T1Score)+":"+str(T2Score)
print(outString)

#write to output file
outOpen = open(outfile, "w")
outOpen.write(outString)
outOpen.close()

