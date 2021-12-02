import argparse
import os
#variable decleration
parser = argparse.ArgumentParser()
ints = ['0','1','2','3','4','5','6','7','8','9']
puncs = ['!','"','#','$','%','&',"'","/",'(',')','*','+',',','-','.','...','/',':',';','<','=','>','?','@','[','\\',']','^','_','`','{','|','}','~']#!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~
parser.add_argument('words', metavar='i', type=str)
parser.add_argument('input', metavar='i', type=str)
parser.add_argument('output', metavar='o', type=str)
paths = parser.parse_args()
words = open(paths.words, 'r')
wordsString = words.read()
words.close()
wordsString = wordsString.split('\n')
#SPELLER
def Speller(stringInTemp):
    stringInArr = []
    nums = 0
    numpunc = 0
    wordsCorrect = 0
    wordsInCorrect = 0
    capitals = 0
    for i in range(len(stringInTemp)):
        flag = False
        for char in stringInTemp[i]:
            for num in ints:
                if num in char:
                    flag = True
            if not flag:
                stringInArr.append(char)
            else:
                nums += 1
    for i in range(len(stringInArr)):
        for char in stringInArr:
            if char in puncs:
                stringInArr.remove(char)
                numpunc += 1
    for i in range(len(stringInArr)):
        if stringInArr[i] != ' ':
            if stringInArr[i] != stringInArr[i].lower():
                stringInArr[i] = stringInArr[i].lower()
                capitals += 1
    wordCheck = []
    wordCheck = ''.join(stringInArr).split(' ')
    for char in wordCheck:
        if char == '' or char == "\n":
            wordCheck.remove(char)
    print(wordCheck)
    for word in wordCheck:
        if word != '':
            if word in wordsString:
                wordsCorrect += 1
            else:
                wordsInCorrect += 1
                print(word)
    return([capitals,numpunc,nums,wordsCorrect,wordsInCorrect])


#SPELLER

#FILE SCANNING
files = os.scandir(paths.input)
for entry in files:
    path = ''
    if paths.input[-1] != "/":
        path = paths.input +"/"
    else:
        path = paths.input
    fileInput = open(path+"/"+entry.name)
    stringIn = fileInput.read()
    out = Speller(stringIn)
    fileInput.close()
    if paths.output[-1] != "/":
        path = paths.output +"/"
    else:
        path = paths.output
    fileOutput = open(path + "/" + entry.name.replace('.txt','') + "_n54133hu.txt",'w')
    fileOutput.writelines("n54133hu"+'\n')
    fileOutput.writelines("Formatting ###################"+'\n')
    fileOutput.writelines("Number of upper case letters changed: "+ str(out[0])+'\n')
    fileOutput.writelines("Number of punctuations removed: "+str(out[1])+'\n')
    fileOutput.writelines("Number of numbers removed: "+str(out[2])+'\n')
    fileOutput.writelines("Spellchecking ###################"+'\n')
    fileOutput.writelines("Number of words: "+str(out[3] + out[4])+'\n')
    fileOutput.writelines("Number of correct words: "+str(out[3])+'\n')
    fileOutput.writelines("Number of incorrect words: "+str(out[4]))
    fileOutput.close()
