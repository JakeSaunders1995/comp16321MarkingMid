import os
import sys

output =[]
index =0

directory = os.listdir(sys.argv[1])
directory.sort()
for files in directory:
    with open(sys.argv[1]+"/"+files, 'r') as h:
        scores= list(h.read())

        i = 2
        team1 = 0
        team2 = 0
        while  i < len(scores):
            if (scores[i] == 't'):
                score = 5
                if (scores[i - 1] == '1'):
                    team1 = team1 + score
                elif (scores[i - 1] == '2'):
                    team2 = team2 + score
            elif (scores[i] == 'c'):
                score = 2
                if (scores[i - 1] == '1'):
                    team1 = team1 + score
                elif (scores[i - 1] == '2'):
                    team2 = team2 + score
            elif (scores[i] == 'p', 'd'):
                score = 3
                if (scores[i - 1] == '1'):
                    team1 = team1 + score
                elif (scores[i - 1] == '2'):
                    team2 = team2 + score
            i = i + 3
            score = 0

        output.append(str(team1) + ":" + str(team2))

for i in range(0,len(output)):
   directory[i]= directory[i][:-4]
   with open(sys.argv[2]+"/"+directory[i]+ '_e17646fa.txt','w+') as h:
       string = output[i]
       h.write(string)
