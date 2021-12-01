import sys
import os

        

def score(v):
    t1 = int(0)
    t2 = int(0)
    j = int(0)
    while j < len(v) :
        if (v[j] == "1") :
            if (v[j+1] == "c") :
                t1 = t1 + 2
            elif(v[j+1] == "t") :
                t1 = t1 + 5
            elif(v[j+1] == "p") :
                t1 = t1 + 3
            elif(v[j+1] == "d") :
                t1 = t1 + 3
        if (v[j] == "2") :
            if (v[j+1] == "c") :
                t2 = t2 + 2
            elif(v[j+1] == "t") :
                t2 = t2 + 5
            elif(v[j+1] == "p") :
                t2 = t2 + 3
            elif(v[j+1] == "d") :
                t2 = t2 + 3
        j = j + 1
    output = str(sys.argv[2]) + "/" +str("output")
    o = open( output, "w")
    o.write(str(t1) + ":" + str(t2))

def main():
    f1 = sys.argv[1]
    files = os.listdir(f1)
    z = ""
    for x in files:
        z = str(f1) + "/" + str(x)
        if z[-3:] == "txt":
            f = open(z)
            s = f.read()
            score(v)
        z = ""

if __name__ == "__main__":
    main()