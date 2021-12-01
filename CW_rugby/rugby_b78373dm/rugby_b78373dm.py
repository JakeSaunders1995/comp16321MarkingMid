import sys
import os

def convert(x):
    if x=="t":
        return 5
    elif x=="c":
        return 2
    elif x=="p" or x=="d":
        return 3

folder_to_read = sys.argv[1]
folder_to_write = sys.argv[2]

try:
    os.mkdir(folder_to_write)
except OSError:
    print("")



for filename in os.listdir(folder_to_read):
    if filename.endswith(".txt"):

        scores=open(folder_to_read+"/"+filename).read()


        team1=0
        team2=0
        index=0

        while index<len(scores)-1:
            points=convert(scores[index+2])
            if scores[index+1]=="1":
                team1+=points
            elif scores[index+1]=="2":
                team2+=points
            index+=3

        if team1>team2:
            winner=team1
        elif team1<team2:
            winner=team2
        else:
            winner="draw"

        

        result=open(folder_to_write+"/"+filename[0:-4]+"_b78373dm.txt","w")

        result.write(str(team1)+":"+str(team2))

    



    
