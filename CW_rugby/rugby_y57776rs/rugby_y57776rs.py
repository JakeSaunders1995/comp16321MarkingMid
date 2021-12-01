import sys
import os
argumentlist = sys.argv
inputfolder = str(argumentlist[1])
outputfolder = str(argumentlist[2])
file_name = "_y57776rs.txt"

def calculator (inputfile):
        T1score = 0
        T2score = 0
        length = len(file)
        numofscores = int(length / 3)
        for i in range (0, numofscores):
                start = int(i * 3)
                end = int(start + 3)
                scoreinfo = str(file[start : end])
                if scoreinfo[2] == 't':
                        points = 5
                elif scoreinfo[2] == 'c':
                        points = 2
                elif scoreinfo[2] == 'p':
                        points = 3
                elif scoreinfo[2] == 'd':
                       points = 3
                if scoreinfo[1] == '1':
                        T1score += points
                elif scoreinfo[1] == '2':
                        T2score += points
        output = str(T1score) + ":" + str(T2score)
        return(output)

basepath = inputfolder + "/"
with os.scandir(basepath) as entries:
        for entry in entries:
                if entry.is_file():
                        filename = entry.path
                        name = os.path.basename(filename).split('.')[0]
                        newname = name + file_name
                        completeName = os.path.join(outputfolder, newname)
                        print(completeName)
                        f = open(str(filename), "r")
                        file = str(f.read())
                        print (file)
                        output = calculator(file)
                        x = open(completeName, "a")
                        x.write(output)
                        x.close()
                        f.close()
