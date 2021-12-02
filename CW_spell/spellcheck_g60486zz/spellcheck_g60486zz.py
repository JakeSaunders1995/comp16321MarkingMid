import argparse,os,re
parser = argparse.ArgumentParser()
parser.add_argument("Englishwordsfilepath")
parser.add_argument("Inputfilepath")
parser.add_argument("Outputfilepath")
args = parser.parse_args()

#get names of the files
def getnames():
    global filenamelist
    filenamelist = sorted(os.listdir(args.Inputfilepath))
getnames()

def getname():#get the output name list of the files
    global outputlist
    outputlist = sorted(os.listdir(args.Outputfilepath))
getname()

englishtextfile = open(args.Englishwordsfilepath)
engtxt = englishtextfile.read()
correctlist = []
txtlist = engtxt.splitlines()
for file in filenamelist:
    inputpath = args.Inputfilepath + '/' + file
    f = open(inputpath)
    content = f.read()
    numberofnumbers = len(re.findall("\d",content))
    numberofpun = len(re.findall("[^\w\s]|_",content))
    capitcalnum = len(re.findall("[A-Z]",content))
    text = re.sub("[^\w\s]|_|\d","",content)
    text = re.sub(" +"," ",text)
    text = text.rstrip()
    wordsspace = text.split(" ")
    for x in wordsspace:
        if x == "":
            wordsspace.remove(x)
    numberofwords = len(wordsspace)
    for x in wordsspace:
        x = x.lower()
        for y in  txtlist:
            if re.fullmatch(x, y) != None:
                correctlist.append(x)
    correctnum = len(correctlist)
    correctlist = []
    incorrectnum = numberofwords - correctnum

    result = "g60486zz"+"\n""Formatting ###################"+"\n"+"Number of upper case letters changed: "+str(capitcalnum)+"\n"+"Number of punctuations removed: "+str(numberofpun)+"\n"+"Number of numbers removed: "+str(numberofnumbers)+"\n"+"Spellchecking ###################"+"\n"+"Number of words: "+str(numberofwords)+"\n"+"Number of correct words: "+str(correctnum)+"\n"+"Number of incorrect words: "+str(incorrectnum)+"\n"
    print(result)
    rename = file.split(".")
    path = args.Outputfilepath + '/' + rename[0] + "_" +  "[user_name].txt"
    f = open(path,'w')
    f.write(result)
    os.rename(path,args.Outputfilepath + '/' + rename[0] + '_'+'g60486zz.txt')



