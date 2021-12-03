import sys
import os


input_folder=sys.argv[1]
output_folder=sys.argv[2]
count=0
for file in os.scandir(input_folder):

    file1=open(file,"r")
    count+=1
    pathname,filename=os.path.split(file)
    string=str(filename)
    string=string[0:len(string)-4]+"_m84249pk.txt"
    file2=open(output_folder+"/"+string,"w")
    scorecard=str(file1.read())

    list=[]
    T1=0
    T2=0
    for i in range(0,len(scorecard),3):
        list.append(scorecard[i:i+3])

    for score in list:
        if score[0:2]=="T1":
            if score[2]=='t':
                T1+=5
            if score[2]=='c':
                T1+=2
            if score[2]=='p':
                T1+=3
            if score[2]=='d':
                T1+=3
        if score[0:2]=="T2":
            if score[2]=='t':
                T2+=5
            if score[2]=='c':
                T2+=2
            if score[2]=='p':
                T2+=3
            if score[2]=='d':
                T2+=3
    file2.write(str(T1)+":"+str(T2))
