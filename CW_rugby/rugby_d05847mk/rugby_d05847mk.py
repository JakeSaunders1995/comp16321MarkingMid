import os
import argparse
parser=argparse.ArgumentParser()
parser.add_argument("inp")
parser.add_argument("otp")
args=parser.parse_args()
inputpath=args.inp
outputpath=args.otp
os.chdir(inputpath)
arr=os.listdir()

def scorecalc():
    t1,t2,c=0,0,0
    f=open(inpfile,"r")
    file=f.read()
    for y in file[1:len(file):3]:
        team.append(y)
    for z in file[2:len(file):3]:
        iscore.append(z)
    lt=len(team)
    for i in iscore:
        if i=='t':
            ascore.append(5)
        elif i=='c':
            ascore.append(2)
        elif i=='p':
            ascore.append(3)
        elif i=='d':
            ascore.append(3)
    while c<lt:
        if team[c]=='1':
            t1+=ascore[c]
        if team[c]=='2':
            t2+=ascore[c]
        c+=1
    if t1>t2:
        winner="Team 1"
    elif t2>t1:
        winner="Team 2"
    elif t1==t2:
        winner="Both- It's a draw"
    return t1, t2, winner

def output():
    t1, t2, winner= scorecalc()
    opfilename=inpfile.replace(".txt","")+"_d05847mk.txt"
    opcon=(str(t1)+":"+str(t2))
    os.chdir(outputpath)
    with open(opfilename,"w") as f:
        f.write(opcon)
    os.chdir(inputpath)

for inpfile in arr:
    team=[]
    iscore=[]
    ascore=[]
    if inpfile.endswith(".txt"):
        output()
