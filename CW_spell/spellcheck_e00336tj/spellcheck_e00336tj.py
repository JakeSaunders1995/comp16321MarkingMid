import sys, re
username = "_e00336tj"
fileList = []
index = 0
for file in sys.argv[1:]:
    if username in file:
        index = sys.argv[1:].index(file.replace(username,""))
        filePair = [sys.argv[1:][index],file]
        fileList.append(filePair)
    if "EnglishWords.txt" in file:
        words = open(file,'r').read()
        wordlist = words.split('\n')
puncFilter = r'[.\-?!,…:;",\'0123456789\[\]\{\}\(\)]'
punctuation='''-?!,…:;"'.,\[\]\{\}\(\)'''
numbers = '0123456789'
#… deal with this and fullstops
for pair in fileList:
    finalList = []
    inputFile = open(pair[0],'r')
    inputstring = inputFile.read()
    outputFile = open(pair[1],'w')
    Uppercase_num, Numbers_num, Punctuation_num, Correct_words = 0,0,0,0
    Punctuation_num += len(re.findall(r'\.\.\.', inputstring)) + len(re.findall(r'\. \. \.', inputstring))
    inputstring = re.sub(r'\.\.\.','', inputstring)
    inputstring = re.sub(r'\. \. \.','', inputstring)
    inputwords = inputstring.split(" ")
    for i in range(len(inputwords)):
        finalword = re.sub(puncFilter,'',inputwords[i].lower())
        finalword = re.sub(r'[\n]','',finalword)
        if (finalword != '') and (finalword != '\n'):
            finalList.append(finalword)
        for j in range(len(inputwords[i])):
            word = inputwords[i]
            letter = word[j]
            if letter.isupper():
                Uppercase_num +=1
            if letter in punctuation:
                Punctuation_num +=1
            if letter in numbers:
                Numbers_num+=1
    length = len(finalList)
    for i in finalList:
        if i in wordlist:
            Correct_words+=1
    outputString =  'e00336tj' + '\nFormatting ################### \nNumber of upper case words changed: ' + str(Uppercase_num) + '\nNumber of punctuations removed: ' + str(Punctuation_num) + '\nNumber of numbers removed: ' + str(Numbers_num) + '\nSpellchecking ################### \nNumber of words: ' + str(length) + '\nNumber of correct words: ' + str(Correct_words) + '\nNumber of incorrect words: ' + str(length - Correct_words)
    outputFile.write(outputString)
    inputFile.close()
    outputFile.close()
   