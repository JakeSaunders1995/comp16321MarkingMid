import argparse,os,re
parser = argparse.ArgumentParser(description='Process the score of the rugby.')
parser.add_argument("dir", nargs='+',help='directory containing files')
args = parser.parse_args()
scorefile = open(args.dir[0],"r")
score = scorefile.read()
T1score = 0
T2score = 0
filenum = 1
for x in range(0,len(score)):
    if score[x] == "t":
        if score[x-1] == "1":
            T1score = T1score +5
        elif score[x-1] == "2":
            T2score = T2score +5
    elif score[x] == "c":
        if score[x-1] == "1":
            T1score = T1score +2
        elif score[x-1] == "2":
            T2score = T2score +2
    elif score[x] == "p" or score[x] == "d":
        if score[x-1] == "1":
            T1score = T1score +3
        elif score[x-1] == "2":
            T2score = T2score +3
if T2score > T1score:
    print("Winner is T2")
elif T2score < T1score:
    print("Winner is T1")
else:
    print("its a draw")
writefilepos = str(args.dir[1]) + "/test_file1_g92198jz.txt"
while True:
    if (os.path.exists(writefilepos)):
        filenum = filenum +1
        writefilepos = str(args.dir[1]) + "/test_file"+str(filenum)+"_g92198jz.txt"
    else:
        break
writefile = open(writefilepos,"w")
outcome = str(T1score)+":"+str(T2score)
writefile.write(outcome)
    