import sys
from os import listdir
from os.path import isfile, join
import re 


pointTypes =  [["p",3],["t",5],["d",3],["c",2]]

inputFolder = sys.argv[1]


testFiles = [f for f in listdir(inputFolder) if isfile(join(inputFolder, f))]



def pointCount (length):
       x = 0

       T1Score = 0
       T2Score = 0

       while x < (len(length))-1:
                    

                     team = length[x] + length[x+1]
                     scoretype = length[x+2]

                     if team == "T1":
                            for i in range(len(pointTypes)):
                                   if scoretype == pointTypes[i][0]:
                                         T1Score = T1Score + pointTypes[i][1]
                                  

                     elif team == "T2":
                            for y in range (len(pointTypes)):
                                   if scoretype == pointTypes[y][0]:
                                          T2Score = T2Score + pointTypes[y][1]
                                          x = x+3

                    

       output = str(T1Score) + ":" + str(T2Score)

       return output

for file in testFiles:
       inputFile = open(f"{inputFolder}/{file}")
       inputText = inputFile.readline()

       finalScore = pointCount(inputText)

       ouputFolder = sys.argv[2]
       outputFile = open(f"{ouputFolder}/{file}_h15879ac.txt","w")
       outputFile.write(finalScore)


       inputFile.close()
       outputFile.close()

