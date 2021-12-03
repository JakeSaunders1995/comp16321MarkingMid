import sys
import os 
mo = sys.argv[1]
che = sys.argv[2]

for m1 in os.listdir(mo):

    a = []
    b = []
    T1 = []
    T2 = []
    m = 0
    td = 0
    tu = 0

    f = open(mo+"/"+m1, "r")
    for i in f :
        a.append(i)
    f.close()


    for i in a :
        c = i.replace("T", "")
        b.append(c)


    sb = "".join(b)



    for i in range(int(len(sb)/2)):
        if sb[m] == "1" :
            if sb[m+1] == "t" :
                tu += 5
            if sb[m+1] == "c" :
                tu += 2
            if sb[m+1] == "p" :
                tu += 3
            if sb[m+1] == "d" :
                tu += 3
       
        if sb[m] == "2" :
            if sb[m+1] == "t" :
                td += 5
            if sb[m+1] == "c" :
                td += 2
            if sb[m+1] == "p" :
                td += 3
            if sb[m+1] == "d" :
                td += 3
        m += 2


    cm = che + "/" + m1[:-4] + "g71830mc.txt"
    chek = open(cm, "w")
    chek.write(str(tu) + ':' + str(td))
    chek.close()


