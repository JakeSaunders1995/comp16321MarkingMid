import sys,os
files = os.listdir(sys.argv[2])
for j in files:
    path = sys.argv[2]+"/"+j
    file = open(path)
    string = file.read()
    file.close()
    toRemove = "0123456789!()?:;.…,[]}{\"\'"
    uLetters=0
    punct=0
    nums=0
    incorrect=0
    res = len(string)
    string=string.replace("...","")
    res -= len(string)
    punct+=int(res/3)
    for i in range(len(toRemove)):
        res = len(string)
        string=string.replace(toRemove[i],"")
        res -= len(string)
        if(i<10):
            nums+=res
        else:
            punct+=res
    for i in string:
        if i.lower()!=i:
            uLetters+=1
    string=string.lower()
    words = [i for i in string.split()]
    with open(sys.argv[1]) as dictionary:
        contents = dictionary.read().split("\n")
        for i in words:
            inFile = False
            for f in contents:
                if f==i:
                    inFile = True
                    continue
            if not inFile:
                print(i)
                incorrect +=1
    path = sys.argv[3]+"/"+j.split(".")[0]+"_e41206gs."+j.split(".")[1]    
    out = open(path, "w")
    temp = "e41206gs"+"\nFormatting ###################"+"\nNumber of upper case words transformed: "+str(uLetters) +"\nNumber of punctuation’s removed: "+str(punct)+"\nNumber of numbers removed: "+str(nums)+"\nSpellchecking ###################"+"\nNumber of words in file: "+str(len(words))+"\nNumber of correct words in file: "+str((len(words)-incorrect))+"\nNumber of incorrect words in file: "+str(incorrect)
    out.write(temp)
    out.close()
