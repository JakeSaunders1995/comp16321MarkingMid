import argparse,os
parser = argparse.ArgumentParser()
parser.add_argument("Inputfilepath")
parser.add_argument("Outputfilepath")
args = parser.parse_args()

def getnames():#get the name list of the files
    global filenamelist
    filenamelist = sorted(os.listdir(args.Inputfilepath))
getnames()

def getname():#get the output name list of the files
    global outputlist
    outputlist = sorted(os.listdir(args.Outputfilepath))
getname()


def numbercount():#Determine the score of each team based on the scoring types and quantity
    global T1,T2,listscore,num,t,c,p,d,content
    listscore = list(content)
    while num < len(listscore):
        if listscore[num] == "1":
            num += 1#work
            if listscore[num] == "t":
                T1 +=5
            elif listscore[num] == "c":
                T1 += 2
            elif listscore[num] == "p":
                T1 += 3
            elif listscore[num] == "d":
                T1 += 3
            num +=2
        elif listscore[num] == "2":
            num += 1
            if listscore[num] == "t":
                T2 +=5
            elif listscore[num] == "c":
                T2 += 2
            elif listscore[num] == "p":
                T2 += 3
            elif listscore[num] == "d":
                T2 += 3
            num += 2
#compare  T1 and T2 , reset  T1,T2 in zero
def Compare():
    if T1 > T2:#Compare the scores to determine a winner
        print("T1 is the winner")
    elif T1 == T2:
        print("Draw")
    elif T1 < T2:
        print("T2 is the winner")

resultlist = []
outputnum = 0
 #create newpath and connect the two def
for file in filenamelist:
    num = 1
    T1 = 0
    T2 = 0
    newpath = args.Inputfilepath + '/' + file
    f = open(newpath,"r")#python3 rugby [username].py [input file path] [output file path]
    content = f.read()
    numbercount()
    Compare()
    result=str(T1)+":"+str(T2)
    resultlist.append(result)
    rename = file.split(".")
    path = args.Outputfilepath + '/' + rename[0] + "_" +  "[user_name].txt"
    f = open(path,'w')
    f.write(resultlist[outputnum])
    outputnum += 1
    os.rename(path,args.Outputfilepath + '/' + rename[0] + '_'+'g60486zz.txt')
