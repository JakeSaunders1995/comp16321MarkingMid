import sys
from os import listdir
from os.path import isfile, join
input_folder = sys.argv[1]
files = [file for file in listdir(input_folder) if isfile(join(input_folder, file)) and file[0] != '.']
 
 
 
allmark = 'T1tT2pT2pT1pT1d'
t = int(5)
c = int(5)
p = int(3)
d = int(3)
 
 
def function(allmark, score1 = 0, score2 = 0):
 
    if len(allmark) == 0: return f"{score1}:{score2}"
    else:
 
        if (allmark[1] == "1"):
            if allmark[2] == "t":
                score1 += 5
            if allmark[2] == "c":
                score1 += 2
            if allmark[2] =="p":
                score1 +=3
            if allmark[2] == "d":
                score1 += 3
        else:
 
            if allmark[2] == "t":
                score2 += 5
            if allmark[2] == "c":
                score2 += 2
            if allmark[2] =="p":
                score2 +=3
            if allmark[2] == "d":
                score2 += 3
 
        return function(allmark[3:], score1, score2) 
 

for file in files:
    input_file = open(f"{input_folder}/{file}")
    allmark = input_file.readline()
 
    output_folder = sys.argv[2]
    output_file = open(f"{output_folder}/{file[:-4]}_p99614sy.txt", "w")
    output_file.write(str(function(allmark)))
 
    input_file.close()
    output_file.close()
 
