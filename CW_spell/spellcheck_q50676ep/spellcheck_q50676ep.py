import os, re, sys

lowerCase = {
    "A": "a",
    "B": "a",
    "C": "a",
    "D": "a",
    "E": "a",
    "F": "a",
    "G": "a",
    "H": "a",
    "I": "a",
    "J": "a",
    "K": "a",
    "L": "a",
    "M": "a",
    "N": "a",
    "O": "a",
    "P": "a",
    "Q": "a",
    "R": "a",
    "S": "a",
    "T": "a",
    "U": "a",
    "V": "a",
    "W": "a",
    "X": "a",
    "Y": "a",
    "Z": "a",

}

numbers =["0","1","2","3","4","5","6","7","8","9"]
UpperCase = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
punctuation= [",",".","!","?","'",'"',";",":","-"]
EnglishWords = open(sys.argv[1], "r")
correctSpelling = EnglishWords.read()
entries = os.listdir(sys.argv[2])

for i in range(len(entries)):
    data = open(sys.argv[2] +"/" + entries[i])
    dataRead = ""
    wholeFile =data.read()
    data.close()
    print(wholeFile)
    fullWord= ""
    letter= ""
    correctWords = 0
    incorrectWords = 0
    totalWords = 0
    caseChange= 0
    numberGone= 0
    punctuationGone= 0
    data = open(sys.argv[2] +"/" + entries[i])
    while dataRead != wholeFile:
        currentCharacter=data.read(1)
        dataRead = dataRead + currentCharacter
        if currentCharacter == " ":
            totalWords = totalWords + 1
            if fullWord in correctSpelling:
                correctWords = correctWords + 1
                #print("correctWords")
            else:
                incorrectWords = incorrectWords + 1
                #print(incorrectWords)
            fullWord = ""
        elif currentCharacter in UpperCase:
            caseChange= caseChange + 1
            #print(currentCharacter)
            newCharacter = lowerCase[currentCharacter]
            #print(currentCharacter)
            fullWord = fullWord + newCharacter
        elif currentCharacter in numbers:
            numberGone = numberGone + 1
            #print(numberGone)
        elif currentCharacter in punctuation:
            punctuationGone= punctuationGone + 1
            #print(punctuationGone)
        else:
            fullWord = fullWord +currentCharacter
    finalOutput = open(sys.argv[3] + "/" + str(i) + "_P3_q50676ep.txt" , "w")
    finalOutput.write("q50676ep")
    finalOutput.close()
    finalOutput = open(sys.argv[3] + "/" + str(i) + "_P3_q50676ep.txt" , "a")
    finalOutput.write("\nFormatting ###########")
    finalOutput.write("\nNumber of upper case letters change: " + str(caseChange))
    finalOutput.write("\nNumber of punctuations removed: " + str(punctuationGone))
    finalOutput.write("\nNumber of numbers removed: " +str(numberGone))
    finalOutput.write("\nSpellchecking ###########")
    finalOutput.write("\nNumber of words: " + str(totalWords))
    finalOutput.write("\nNumber of correct words: " + str(correctWords))
    finalOutput.write("\nNumber of incorrect words: " + str(incorrectWords))
    finalOutput.close()
    print("Iteration" + str(i))














    print("Looping")
