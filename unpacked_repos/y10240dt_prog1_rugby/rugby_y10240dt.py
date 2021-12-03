import os
import argparse


parser = argparse.ArgumentParser(description="rugby")
parser.add_argument('inp')
parser.add_argument('out')
args = parser.parse_args()


def execute(file):
    f = open(file)
    inp = f.read()
    f.close()
    inplst = []
    lo=0
    hi=3
    team1=0
    team2=0
    for x in range (0,(len(inp)//3)):
        inplst.append(inp[lo:hi])
        lo +=3
        hi+=3
    for x in range(0,(len(inp)//3)):
        if int(inplst[x][1])==1:
            if inplst[x][2]=="t":
                team1 +=5
            elif inplst[x][2]=="c":
                team1 +=2
            elif inplst[x][2]=="p":
                team1 +=3
            elif inplst[x][2]=="d":
                team1 +=3
        elif int(inplst[x][1])==2:
            if inplst[x][2]=="t":
                team2 +=5
            elif inplst[x][2]=="c":
                team2 +=2
            elif inplst[x][2]=="p":
                team2 +=3
            elif inplst[x][2]=="d":
                team2 +=3
    return str(team1)+":"+str(team2)


dir = args.inp
spath = args.out
for file in os.listdir(dir):
    if file.endswith(".txt"):                   #iterates through input folder and executes the function on any .txt file
        toexe= os.path.join(args.inp, file)
        x = execute(toexe)
        fname = file.replace(".txt","")
        fname += "_y10240dt.txt"
        path = os.path.join(spath, fname)                       #write file on a specific path
        nf = open(path, "w")
        nf.write(x)
        nf.close()
