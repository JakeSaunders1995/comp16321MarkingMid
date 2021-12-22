import argparse,os,re
parser = argparse.ArgumentParser(description='Process the score of the rugby.')
parser.add_argument("dir", nargs='+',help='directory containing files')
args = parser.parse_args()
storedfile = os.listdir(args.dir[0])
for i in range (0,len(storedfile)):
    prefix = storedfile[i].replace(".txt", "")
    filename = args.dir[0]+"/"+storedfile[i]
    scorefile = open(filename,"r")
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
    writefilepos = str(args.dir[1]) + "/" + prefix + "_g92198jz.txt"
    writefile = open(writefilepos,"w")
    outcome = str(T1score)+":"+str(T2score)
    writefile.write(outcome)
    