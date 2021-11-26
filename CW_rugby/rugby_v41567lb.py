import argparse
import os

parser=argparse.ArgumentParser()
parser.add_argument("inpdir", type=str)
parser.add_argument("outdir", type=str)
args=parser.parse_args()


dir1=getattr(args, "inpdir")
dir2=getattr(args, "outdir")


def points(type):
    if type=="t":
        return int(5)
    elif type=="c":
        return int(2)
    elif type=="p":
        return int(3)
    elif type=="d":
        return int(3)

for file in os.listdir(dir1):
    print(file)
    infile=open(dir1+"/"+file,"r")
    scores=list(infile.read())
    infile.close()
    t1=0
    t2=0
    for i in range(0,len(scores)-1,3):
        if scores[i+1]=="1":
            t1=t1+points(scores[i+2])
        elif scores[i+1]=="2":
            t2=t2+points(scores[i+2])
    outname=file.replace(".txt","_v41567lb.txt")
    outp=open(dir2+"/"+outname,"w")
    outp.write(str(t1)+":"+str(t2))
    outp.close()
