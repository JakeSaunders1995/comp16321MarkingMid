import sys
import os
inpath = rf"{sys.argv[1]}"
outpath = rf"{sys.argv[2]}"
for file in os.listdir(inpath):
    if ".txt" in file:
        f = open(rf"{str(inpath)}/{file}","r")
        testinput = f.read()
        t1 = 0
        t2 = 0
        for i in range(len(testinput)):
            if testinput[i] == '1':
                if testinput[i+1] == 't':
                    t1 += 5
                if testinput[i+1] == 'c':
                    t1 += 2
                if testinput[i+1] == 'p':
                    t1 += 3
                if testinput[i+1] == 'd':
                    t1 += 3
            if testinput[i] == '2':
                if testinput[i+1] == 't':
                    t2 += 5
                if testinput[i+1] == 'c':
                    t2 += 2
                if testinput[i+1] == 'p':
                    t2 += 3
                if testinput[i+1] == 'd':
                    t2 += 3
        g = open(rf"{str(outpath)}/{file[:-4]}_y36340hc.txt","w")
        g.write(f"{t1}:{t2}")