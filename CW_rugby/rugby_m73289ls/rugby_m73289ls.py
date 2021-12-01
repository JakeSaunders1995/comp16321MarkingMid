import argparse
import os
#pathsetting
parser = argparse.ArgumentParser()
parser.add_argument('filepath1')
parser.add_argument('filepath2')
args = parser.parse_args()
inputpath = args.filepath1
outputpath = args.filepath2
inputfiles = os.listdir(inputpath)
#input
os.chdir(inputpath)
for files in inputfiles: 	
    with open(files) as file:
        line = file.readline()
    file.close()
    mylist=[]
    x = 0
    T1score=0
    T2score=0
    while x < len(line) :
        current=line[x:x+3]
        mylist.append(current)
        x = x +3
    else:
        for y in mylist:
            if y[2] == "t":
                currentscore = 5
            elif y[2] == "c":
                currentscore = 2
            elif y[2] == "p":
                currentscore = 3
            else:
                currentscore = 3                            
            if y[0:2] == "T1":
                T1score = T1score + currentscore
            else:
                T2score = T2score + currentscore
    final = str(T1score) + " : " + str(T2score)
#output
    filesname = str(files)
    name = filesname[0:-4] + "_m73289ls.txt"
    os.chdir(outputpath)
    with open(name, 'w') as file:
        file.write("%s\n" % final)
    file.close()
    os.chdir(inputpath)
    
