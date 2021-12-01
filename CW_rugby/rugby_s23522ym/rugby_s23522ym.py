import argparse
import os
parser= argparse.ArgumentParser()
parser.add_argument('inPath', type=str)
parser.add_argument('outPath', type=str)
args = parser.parse_args()

FileList=os.listdir(args.inPath)
FilenameList=[]
for item in FileList:
    if ".txt" in item:
        FilenameList.append(item)

for Filename in FilenameList:
    file = open(args.inPath+"/"+Filename,"r")
    TeamScore = file.readlines()
    file.close()
    if not TeamScore:
        finaloutput = str(0)+":"+str(0)
        file1 = open(args.outPath+"/"+Filename[:-4]+"_s23522ym.txt","w")
        file1.write(finaloutput)
    elif TeamScore != "":
        TS       = TeamScore[0].replace("T","")
        T1score = 0
        T2score = 0
        for i in range(0, len(TS),2):
            if TS[i]=="1":
                if TS[i+1]=="t":
                    T1score+=5
                if TS[i+1]=="c":
                    T1score+=2
                if TS[i+1]=="p":
                    T1score+=3
                if TS[i+1]=="d":
                    T1score+=3
            if TS[i]=="2":
                if TS[i+1]=="t":
                    T2score+=5
                if TS[i+1]=="c":
                    T2score+=2
                if TS[i+1]=="p":
                    T2score+=3
                if TS[i+1]=="d":
                    T2score+=3

        finaloutput = str(T1score)+":"+str(T2score)
        file1 = open(args.outPath+"/"+Filename[:-4]+"_s23522ym.txt","w")
        file1.write(finaloutput)
        file1.close()
