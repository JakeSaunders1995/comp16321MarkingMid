import sys
import os 
mo = sys.argv[1]
che = sys.argv[2]

for m1 in os.listdir(mo):


    MC = {
        ".-" : "a", "-..." : "b", "-.-." : "c", "-.." : "d", "." : "e", "..-." : "f", "--." : "g", "...." : "h", ".." : "i", ".---" : "j", "-.-" : "k", ".-.." : "l", 
        "--" : "m", "-." : "n", "---" : "o", ".--." : "p", "--.-" : "q", ".-." : "r", "..." : "s", "-" : "t", "..-" : "u", "...-" : "v", ".--" : "w", "-..-" : "x", 
        "-.--" : "y", "--.." : "z", ".----" : "1", "..---" : "2", "...--" : "3", "....-" : "4", "....." : "5", "-...." : "6", "--..." : "7", "---.." : "8", 
        "----." : "9", "-----" : "0", ".-.-.-" : ".", "..--.." : "?", "-.-.--" : "!", "--..--" : ",", "---..." : ":", "-.-.-." : ";", "-....-" : "-", "-.--." : "(", "-.--.-" : ")", 
        ".----." : "'", ".-..-." : "''", "/" : " "
    }

    ab = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    a = []
    c = []
    a1 = []
    a2 = []
    b2 = []
    


    f = open(mo+"/"+m1, "r")
    for i in f:
        a.append(i)
    f.close()



    def MCD (t) :
        global tf
        to = ""
        for i in b1 :
        
            to += i
    
        b = []
        tf = ""
        
        for i in to :
            
            if i != " " : 
                a1.append(i)
                
            else : 
                b = "".join(a1)
                del a1[:]
                c.append(b)
        for i in c:
            tf += MC[i]
        
        

    def HD (t) :
        global tf
        tf = bytearray.fromhex(t).decode()

    def CC(t) :
        global tf
        tf = ""
        for i in t :
            if i != " " :
                for j in range (len(ab)) :
                    if i == ab[j] :
                        nl = (j-3)
                        nc = ab[nl]
                        tf += nc
            else :
                tf += i
        
        
        



    for i in a :
        b2 +=i

    if b2[0] == "H":
        for i in a :
            b1 = i.replace ("Hex:", "")
        HD(b1)
    if b2[0] == "M":
        for i in a :
            b1 = i.replace ("Morse Code:", "")
        MCD(b1)
    if b2[0] == "C":
        for i in a :
            b1 = i.replace ("Caesar Cipher(+3):", "")
        CC(b1)

    cm = che + "/" + m1[:-4] + "g71830mc.txt"
    chek = open(cm, "w")
    chek.write(tf)
    chek.close()

