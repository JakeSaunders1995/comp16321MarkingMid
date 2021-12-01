## rugby

## cli args (from sys import later)
import sys, os

def writeDataToFile(filename):
    for i in range(len(filename)):
        if filename[i] == '.':
            fileExtention = filename[i:]
            filename = filename[:i] ## remove the file extention (most likely .txt)
            break
    else:
        fileExtention = ''

    fileWrite = open((folderWritePath+'/'+filename+'_'+username+fileExtention), "wt")
    fileWrite.write(str(team1)+":"+str(team2))
    fileWrite.close()

## globals
username = "j16919mb"
folderReadPath = (sys.argv)[1] 
folderWritePath = (sys.argv)[2]

for filename in os.listdir(folderReadPath):
    fileR = open(folderReadPath+'/'+filename, "rt")

    team1 = 0
    team2 = 0
    
    while True:
        block = fileR.read(3)
        if not block:
            break
        dictScore = {"t":5, "c":2, "p":3, "d":3}
        
        if block[1] == "1":
            team1 += dictScore[block[2]]
        else:
            team2 += dictScore[block[2]]

    fileR.close()
    writeDataToFile(filename)