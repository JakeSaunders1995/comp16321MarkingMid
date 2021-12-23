import sys
import os
filles =[]
filles = os.listdir(str(sys.argv[2])) # Get all test files and put in list
for p in filles:
    if not p.startswith('.'):       #Ignores the hidden files
        fpath1 = str(sys.argv[2])
        fullname1 = os.path.join(fpath1,p)      #creates filepath for inputs
        fi1le = open(fullname1, encoding="utf8", errors='ignore')

        fpath = str(sys.argv[3])
        p = str(p)
        pos = int(p.find(".txt"))          
        fname = p[:pos] + "_q86352bb.txt"
        fullname = os.path.join(fpath,fname)       #creates the filename for the outouts 
        f = open(fullname, "w")
        uplet =0
        punct =0
        nums =0
        totWords =0
        correctWords =0
        incorWords =0
        engFile = open(str(sys.argv[1]))
        for i in engFile:
            all = engFile.read().splitlines()
        all += ["a"]
        for d in fi1le:
            d+= " "
            length = len(d)
            pos = 0
            for p in range(0,length):
                if ord(d[p]) > 64 and ord(d[p])<91: #upper case letters 
                    uplet +=1  
            d = d.lower()
            lastspacePos =0
            x = list(d)
            for y in range(0,length-1):
                if ord(x[y]) == 39:
                    x = x[:y] + x[y+1:]   #this gets rid of apostrophe and rejoins the word
                    punct +=1
                if ord(x[y]) <97 or ord(x[y]) > 122:  
                    if ord(x[y]) >47 and ord(x[y]) <58:  # num count
                        nums +=1 
                        x[y] = " "
                    elif ord(x[y]) != 32:    #not a space
                        if ord(x[y]) == 46 and ord(x[y+1]) == 46 and ord(x[y+2]):  # Elipsis code 
                            punct +=1
                            x[y] = " "
                            x[y+1] = " "
                            x[y+2] = " "
                        elif ord(x[y]) == 92 and ord(x[y+1]) == 110:   #\n code 
                            x[y] = " "
                            x[y+1] = " "
                        elif ord(x[y]) != 35 or ord(x[y]) !=64: # will execute for all punct except @ and #
                            punct +=1
                            x[y] = " "      
            while pos < length -1:
                let = x[pos]
                if ord(x[pos]) == 32:
                    if lastspacePos +1 == pos:   #if theres a double space from remvoing punct it will move forward
                        lastspacePos = pos
                    else:
                        if lastspacePos == 0 and totWords==0:  #this is code for the first word
                            newword = x[lastspacePos:pos]
                            word = "".join(newword)
                            totWords += 1
                            lastspacePos = pos
                        else: 
                            word = ""
                            word = "".join(x[lastspacePos+1:pos])
                            totWords += 1
                            lastspacePos = pos
                        if (word) in all:
                            correctWords += 1
                        else:
                            incorWords +=1                      
                pos+=1
        f.write("q86352bb\n")
        f.write("Formatting ###################\n")
        f.write("Number of upper case words transformed: " +str(uplet) +"\n")
        f.write("Number of punctuation’s removed: " + str(punct) +"\n")
        f.write("Number of numbers removed: " + str(nums)+"\n")
        f.write("Spellchecking ###################\n")
        f.write("Number of words in file: " + str(totWords)+"\n")
        f.write("Number of correct words in file: " + str(correctWords)+"\n")
        f.write("Number of incorrect words in file: " + str(incorWords)+"\n")