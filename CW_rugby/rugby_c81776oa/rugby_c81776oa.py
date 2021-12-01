import sys
import os

output = []
index = 0
listofFiles = os.listdir(sys.argv[1])
listofFiles.sort()
for files in listofFiles:
    with open(sys.argv[1]+"/"+files, 'r') as f:
        score = f.read()
        t1Score = 0
        t2Score = 0

        for char in range(0,len(score)):
            if char % 3 == 0:
                if score[char] == 'T' and score[char+1] == '1':
                    if score[char+2] == 't':
                        t1Score += 5
                    elif score[char+2] == 'c':
                        t1Score += 2
                    elif score[char+2] == 'p':
                        t1Score += 3
                    else:
                        t1Score += 3
                if score[char] == 'T' and score[char+1] == '2':
                    if score[char+2] == 't':
                        t2Score += 5
                    elif score[char+2] == 'c':
                        t2Score += 2
                    elif score[char+2] == 'p':
                        t2Score += 3
                    else:
                        t2Score += 3

        finalscore = str(t1Score)+":"+str(t2Score)
        output.append(finalscore)


for i in range(0,len(output)):
    listofFiles[i] = listofFiles[i][:-4]
    with open(sys.argv[2]+"/"+listofFiles[i]+"_c81776oa.txt", 'w') as f:
        string = output[i]
        f.write(string)
