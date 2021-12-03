#checked n outputs work - ready to submit. remove prog1 tag First then tag this commit w program 1.
import sys, os
inputfoldername = sys.argv[1]
files = os.listdir(inputfoldername)
print(files)
for filename in files:
    file = open("./"+inputfoldername+"/"+filename,"r")
    inp = file.read()
    file.close()

    c = 0
    t1 = 0
    t2 = 0
    while c!=len(inp):
        if inp[c+1] == "1":
            if inp[c+2] == "t":
                t1=t1+5
            if inp[c+2] == "c" :
                t1=t1+2
            if inp[c+2] == "d" or inp[c+2] == "p":
                t1=t1+3
        else:
            if inp[c+2] == "t":
                t2=t2+5
            if inp[c+2] == "c":
                t2=t2+2
            if inp[c+2] == "d" or inp[c+2] == "p":
                t2=t2+3
        c=c+3
    print(str(t1)+':'+str(t2))

    outputfoldername = sys.argv[2]

    file = open("./"+outputfoldername+"/"+filename[0:len(filename)-4]+'_n62189sd.txt',"w")
    file.write(str(t1)+':'+str(t2))
    file.close()
