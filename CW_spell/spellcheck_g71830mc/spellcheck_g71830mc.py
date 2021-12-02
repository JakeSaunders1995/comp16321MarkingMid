import sys
import os 

mo = sys.argv[1]
che = sys.argv[2]
krou = sys.argv[3]

for m1 in os.listdir(che):

    l1=[]
    a = []
    b = []
    c = []
    ab = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z" ]
    pon = [",", "?", "!", ".", ";", ":", "-", "[", "]", "(", ")", "'", "''", "{", "}"]
    ch = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    t = ""
    r = 0
    n = 0 
    p = 0 
    co = 0
    to = 0 


    f1 = open(che+"/"+m1, "r")
    for i in f1 :
        b.append(i)
    f1.close()

    f = open(mo)
    for i in f :
        a.append(i.rstrip("\n"))
    f.close()



    for i in b :
        for j in i :
            
            if j in ch :
                i = i.replace (j , "")
                n+= 1
                
            if j in ab :
                r+=1
                
            if j in pon :
                i = i.replace (j , "")
                p+=1
    
    b2 = i.lower()

    x = b2.split(" ")

    x = [i for i in x if i != ""]

    for i in x :
        for j in a : 
            if i == j :
                co +=1

    inco = len(x) - co
    
    mc = krou+"/"+m1[:-4]+"g71830mc.txt"
    cm = open(mc,"w")

    cm.write("g71830mc" + "\n")
    cm.write("Formatting"+"###################" + "\n")
    cm.write("Number of upper case letters changed :" + str(r) + "\n")
    cm.write("Number of punctuations removed : " + str(p) + "\n")
    cm.write("Number of numbers removed :" + str(n) + "\n")
    cm.write("Spellchecking"+"###################"+"\n")
    cm.write("Number of words :" + str(len(x))+"\n")  
    cm.write("Number of correct words :" + str(co)+"\n")
    cm.write("Number of incorrect words :" + str(inco)+"\n")

    cm.close()
        


