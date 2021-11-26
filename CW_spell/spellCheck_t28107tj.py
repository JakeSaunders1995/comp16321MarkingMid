import sys,os
arguments = sys.argv

punc = ".?!,:;-[]\{}()`\'\"@#~<>£$%^&*"

with open(arguments[1]) as wordFile:
    words = wordFile.read()
words = words.split()

for file in os.listdir(arguments[2]):
    if arguments[2][-1] != "/":
        source = arguments[2]+"/"+file
    else:
        source = arguments[2]+file
    with open(source) as wrongFile:
        checkText = wrongFile.read()
    pCount = 0
    for character in punc:
        pCount += checkText.count(character)
        checkText = checkText.replace(character, "")
    nCount = 0
    for character in "1234567890":
        nCount += checkText.count(character)
        checkText = checkText.replace(character, "")
    checkTextSplit = checkText.split()
    lCount = 0
    for word in checkTextSplit:
        if word != word.lower():
            lCount += 1
    checkText = checkText.lower().split()
    numberOfWords = len(checkText)
    correctWords = 0
    for word in checkText:
        if word in words:
            correctWords += 1
    incorrectWords = numberOfWords - correctWords
    output = """t28107tj
Formatting ###################
Number of upper case words transformed: {}
Number of punctuation’s removed: {}
Number of numbers removed: {}
Spellchecking ###################
Number of words in file: {}
Number of correct words in file: {}
Number of incorrect words in file: {}""".format(lCount,pCount,nCount,numberOfWords,correctWords,incorrectWords)
    if arguments[3][-1] != "/":
        outputLocation = arguments[3]+"/"+file[:-4]+"_t28107tj.txt"
    else:
        outputLocation = arguments[3]+file[:-4]+"_t28107tj.txt"
    with open(outputLocation,"w") as outputFile:
        outputFile.write(output)