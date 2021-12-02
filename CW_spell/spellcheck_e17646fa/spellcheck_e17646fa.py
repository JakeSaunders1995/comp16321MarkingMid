import sys,os

eng = open(sys.argv[1])
english = eng.read()
eng.close()



output =[]
index =0
#assign directory
directory = os.listdir(sys.argv[2])
directory.sort()

# f = open ("test_file2.txt", "r")
# input = f.read()
# f.close()


numbercount= 0
PunNum = 0
UpCaNum = 0
LoCaNum = 0
CoWoNum = 0
InCoWoNum = 0


def spell(input):
    Pun ='''!()-[]{};:'",<>./?#%^&*_~'''
    PunNum = 0
    for P in input:
        if P in Pun:
            input = input. replace(P,"")
            PunNum += 1
    numbercount = 0
    for C in input:
        if C.isdigit():
            input = input.replace(C,"")
            numbercount += 1

    UpCaNum = 0
    for U in input:
        if U.isupper():
            UpCaNum += 1

    LoCase = input.lower()
    LoLst = LoCase. split()
    countwords = len(LoLst)

    dictionarylist = english.split()
    CoWoNum = 0
    InCoWoNum = 0
    for word in LoLst:
        if word in dictionarylist:
            CoWoNum += 1
        else:
            InCoWoNum += 1


    output=""
    output+= 'e17646fa\n'
    output+='Formatting #################\n'
    output+='Number of upper case words changed: '+str(UpCaNum)+'\n'
    output+='Number of punctuations removed: '+str(PunNum)+'\n'
    output+='Number of numbers removed: '+str(numbercount)+'\n'
    output+="Spellchecking ####################\n"
    output+='Numbers of words: '+str(countwords)+'\n'
    output+='Number of correct words: '+str(CoWoNum)+'\n'
    output+='Number of incorrect words: '+str(InCoWoNum)

    return output

for files in directory:
    with open(sys.argv[2]+"/"+files, 'r') as u:
        string = u.read()
        with open(sys.argv[3]+"/"+files[:-4]+ '_e17646fa.txt','w+') as h:
            h.write(spell(string))
