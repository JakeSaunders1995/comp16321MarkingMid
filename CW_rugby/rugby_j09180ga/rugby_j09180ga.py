import os
import sys

scoring = {
    "t": 5,
    "c": 2,
    "p": 3,
    "d": 3
}
inputfolder = sys.argv[1] + '/'
outputfolder = sys.argv[2] + '/'
files = os.listdir(inputfolder)
for file in files:
    t1score = 0
    t2score = 0
    myfile = inputfolder + file
    with open(myfile) as f:
        mydata = f.read()
        for i in range(0, len(mydata), 3):
            score = mydata[i: i + 3]
            if score[0:2] == "T1":
                t1score += scoring.get(score[2:3])
            elif score[0:2] == "T2":
                t2score += scoring.get(score[2:3])
            else:
                continue
        with open(outputfolder + file[0:-4] + "_j09180ga.txt", 'w') as f:
            f.write(str(t1score) + ':' + str(t2score))
