#!/usr/bin/env python3
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('inf')
parser.add_argument('outf')
args=parser.parse_args()

path, dirs, files = next(os.walk(args.inf))

fileCount = files
print(path)
for i in files:
    ifile = path+"/" +i
    ofile = args.outf+ "/"+ i[0:-4] + "_k96010wp.txt"
    scores =  [0,0]
    scoring = {'t':5,'c':2,'p':3,'d':3}
    inchars= open(ifile).read()
    print(inchars)
    for i in range(0,len(inchars),3):
        scores[ord(inchars[i+1])-49]+=scoring[inchars[i+2]]

    val = scores[0]-scores[1]
    if(val>0):
        print("team 1 won")
    elif(val<0):
        print("team 2 won")
    else:
        print("alas, it is a draw")

    outfile = open(ofile,"w")
    outfile.write("{0}:{1}".format(scores[0],scores[1]))
    outfile.close()
