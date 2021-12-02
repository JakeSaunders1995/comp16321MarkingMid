import argparse,os,re
parser = argparse.ArgumentParser(description='Decrypt file.')
parser.add_argument("dir", nargs='+',help='directory containing files')
args = parser.parse_args()
storedfile = os.listdir(args.dir[1])
for i in range (0,len(storedfile)):
    prefix = storedfile[i].replace(".txt", "")
    filename = args.dir[1] + "/" + storedfile[i]
    textfile = open(filename,"r")
    englishwordfile = open(args.dir[0],"r")
    englishwords = englishwordfile.readlines()
    englishwordlist = []
    for y in range (0,len(englishwords)):
        englishwords[y] = englishwords[y].replace("\n", "")
    text = textfile.read()
    numberofUpperCase = len(re.findall(r"[A-Z]", text))
    text = text.lower()
    numberofnumber = len(re.findall("\d", text))
    numberofpunctuation = len(re.findall("[^\w\s]|_", text))
    text = re.sub("\d", "", text)
    text = re.sub("[^\w\s]|_", "", text)
    text = re.sub(" +", " ", text)
    word = ""
    text = text + " "
    for x in range(0,len(text)):
        if text[x] != " ":
            word = word+text[x]
        elif text[x] == " ":
            englishwordlist.append(word)
            word = ""
    match = 0
    for w in englishwordlist:
        for v in englishwords:
            if v == w :
                match = match +1
    print(englishwordlist)
    writefilepos = str(args.dir[2]) + "/" + prefix + "_g92198jz.txt"
    writefile = open(writefilepos, "w")
    writefile.writelines("g92198jz\n")
    writefile.writelines("Formatting ###################\n")
    writefile.writelines("Number of upper case words changed: " + str(numberofUpperCase) + "\n")
    writefile.writelines("Number of punctuations removed: " + str(numberofpunctuation)+ "\n")
    writefile.writelines("Number of numbers removed: " + str(numberofnumber)+ "\n")
    writefile.writelines("Spellchecking ###################\n")
    writefile.writelines("Number of words: " + str(len(englishwordlist))+ "\n")
    writefile.writelines("Number of correct words: " + str(match)+ "\n")
    writefile.writelines("Number of incorrect words: " + str(len(englishwordlist)-match)+ "\n")