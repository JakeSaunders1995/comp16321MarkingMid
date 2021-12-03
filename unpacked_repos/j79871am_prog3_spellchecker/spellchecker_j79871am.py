import os
f = 0

filepa = input("please input and output file path: ")
filepath= filepa.split()
filepath1 = filepath[0]
outputinp = filepath[1]

realdirect = os.listdir(filepath1)
coolerreal = (filepath1 + ("\\"))
coolerreal.strip()
coolerreal1 = coolerreal + realdirect[0]
reallen = len(realdirect)

while reallen != f:
    path = str(r"C:\Users\mlgmo\Desktop\midterm_files\EnglishWords.txt")
    newfile = open(path, "r")
    cool = newfile.readlines()
    cooler = len(cool)

    i = 0
    sickbeans = coolerreal + realdirect[f]
    newlist15 = []
    rfile = open(sickbeans, "r")
    for line in rfile:
        for character in line:
            newlist15.append(character)
    s = len(newlist15)

    q= 0
    while i != s:
        cray = newlist15[i]
        if cray == (".") or cray == ("?") or cray == ("!") or cray == (",") or cray == (":") or cray == (
                            ";") or cray == ("-") or cray == ("–") or cray == ("—") or cray == ("(") or cray == (
                    ")") or cray == (
                            "{") or cray == ("}") or cray == ("...") or cray == ("'") or cray == ('"') or cray == (
                    "[") or cray == (
                            "]") or cray==("@") or cray ==("#"):
            q= q +1


        i = i +1
    s = s-q+1
    i=0
    n= 0
    m= 0
    while i != s:
        cray = newlist15[i]
        if cray == (".") or cray == ("?") or cray == ("!") or cray == (",") or cray == (":") or cray == (
                            ";") or cray == ("-") or cray == ("–") or cray == ("—") or cray == ("(") or cray == (
                    ")") or cray == (
                            "{") or cray == ("}") or cray == ("...") or cray == ("'") or cray == ('"') or cray == (
                    "[") or cray == (
                            "]") or cray==("@") or cray ==("#"):
            q= q +1
            newlist15.pop(i)
        elif type(cray) == int:
            n = n+1
        elif cray != cray.lower():

            m = m+1
            newlist15[i] = cray.lower()
        i = i +1
    i = 0
    l = 0
    p = 0
    words = 0
    nowords = 0
    states = ("  ").join(newlist15)
    coolest1 = states.replace("  ","")

    coolers = list(coolest1.split())
    sick = len(coolers)
    tin = sick
    nos = 0
    while l != cooler:
        p = 0
        bi = cool[l]


        while p != sick:
            be = coolers[p] + ("\n")

            if be == bi:
                words  = words +1
            else:
                nos = nos +1
            p = p +1
        l = l +1
    nowords = tin - words
    overall = words + nowords
    byte = ("j7987am \n Formatting ############ \n Number of upper case letters changed: " +str(m) +"\n Number of Punctuations removed:" +str(q) +"\n Number of numbers removed: " +str(n) + " \n Spellchecking ################# \n Number of Words: " + str(overall) + " \n Number of correct words" + str(words) + "\n Number of incorrect words: " + str(nowords))
    calc = f + 1
    otfilenam = (("test_file") + (str(calc)) + ("_j79871am.txt"))
    outp = os.path.join(outputinp, otfilenam)
    opres = open(outp, "w")
    opres.write(byte)
    opres.close()


    f = f +1
