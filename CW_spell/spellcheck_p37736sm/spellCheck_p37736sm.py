import sys
print("argument list: ", str(sys.argv))

infile = sys.argv[1]
outfile = sys.argv[2]
infile = open(infile, "r")
string = infile.read()
print(string)

#output variables
upperWordsChanged = 0
punctuationRemoved = 0
numNumbersRemoved = 0

numWords = 0
numCorrectWords = 0
numIncorrectWords = 0

englishWords = open("EnglishWords.txt", "r")
englishWords = englishWords.read()
englishWords = englishWords.split()
print(englishWords)


#sanitise inputs
sanitisedString = ""
for i in range(len(string)):
    ASCIIval = ord(string[i])
    if ((ASCIIval > 64 and ASCIIval < 91)):
        upperWordsChanged += 1
        sanitisedString += string[i].lower()
        print("Upper removed: "+string[i])
    elif(ASCIIval > 96 and ASCIIval < 123) or ASCIIval == 32:
        # print(string[i])
        sanitisedString += string[i]
    elif(ASCIIval > 47 and ASCIIval < 58):
        numNumbersRemoved += 1
    else:
        punctuationRemoved += 1
        print("Punctuation Removed: "+string[i])

sanitisedString = sanitisedString.lower()
print(sanitisedString)

wordList = sanitisedString.split(" ")

print(wordList)

for i in range(len(wordList)):
    word = wordList[i]
    if (len(word)==0):
        print("Blank")
    elif(englishWords.count(word)==0):
        print("#incorrect: "+word)
        numIncorrectWords += 1
        numWords += 1
    else:
        print("Correct!: "+word)
        numCorrectWords += 1
        numWords += 1
print(wordList)

#outputs
output = "Formatting ################## \nNumber of upper case words changed : "+str(upperWordsChanged)+"\nNumber of punctuations removed: "+str(punctuationRemoved)+"\nNumber of numbers removed: "+str(numNumbersRemoved)+"\nSpellchecking ################## \nNumber of words: "+str(numWords)+"\nNumber of correct words: "+str(numCorrectWords)+"\nNumber of incorrect words: "+str(numIncorrectWords)
print(output)

#write to output file
outOpen = open(outfile, "w")
outOpen.write(output)
outOpen.close()

print(englishWords.count("tres"))