import os
import sys
def getFiles():
    basepath = sys.argv[1]
    files = []
    for entry in os.listdir(basepath):
        if os.path.isfile(os.path.join(basepath, entry)):
            files.append(entry)
    return files

def outputFiles(output, filename):
    filename = filename[:len(filename)-4]
    f=open(sys.argv[2]+"\\"+filename+"_x33731ed.txt", "w+")
    f.write(output)
    f.close

def rugbyScore(inp):
    T1Score = 0
    T2Score = 0
    length = len(inp)
    length /= 3
    for i in range(int(length)):
        team = inp[i*3+1]
        goal = inp[i*3+2]
        #print(team+":"+goal)
        if(team=="1"):
            if(goal=="t"):
                T1Score+=5
            elif(goal=="c"):
                T1Score+=2
            else:
                T1Score+=3
            #print("T1Score = "+str(T1Score))
        else:
            if(goal=="t"):
                T2Score+=5
            elif(goal=="c"):
                T2Score+=2
            else:
                T2Score+=3
            #print("T2Score = "+str(T2Score))
    return str(T1Score)+":"+str(T2Score)

files = getFiles()
for i in files:
    f = open(sys.argv[1]+"\\"+i,"r")
    inp = f.read()
    outputFiles(rugbyScore(inp), i)
    f.close()
print("done :)")
