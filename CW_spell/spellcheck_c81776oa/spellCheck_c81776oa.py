import sys, os
englishWords = []
with open(sys.argv[1], 'r') as f:
    for line in f:
        englishWords.append(line.strip())

output = []
listofFiles = os.listdir(sys.argv[2])
listofFiles.sort()
for files in listofFiles:
    with open(sys.argv[2]+"/"+files, 'r') as f:
        sentence = f.read()
        numbercounter = 0
        punctuationcounter = 0
        uppercasecounter = 0
        for char in sentence:
            if ord(char) >= 48 and ord(char)<=57:
                numbercounter +=1
            elif ord(char) >= 65 and ord(char) <= 90:
                uppercasecounter += 1
            elif char == "." or char == "?" or char == "!" or char == "," or char == ":" or char == ";" or char == "-" or char == "(" or char == ")" or char == "{" or char == "}" or char == "[" or char == "]" or char == "'" or char == '"' :
                punctuationcounter +=1

        sentence = sentence.lower()
        index = 0
        sentence = sentence.strip()
        while index < len(sentence):
            if (ord(sentence[index]) < 97 or ord(sentence[index]) > 122) and ord(sentence[index]) != 32 and ord(sentence[index]) != 10:
                sentence = sentence.replace(sentence[index],"")
                index -= 1
            index +=1

        tempword = ""
        totalWords = 0
        correctWords = 0
        incorrectWords = 0
        wordIsIncorrect = False
        sentence += " "
        for char in sentence:
            if char != " ":
                tempword += char
            else:
                if tempword != "" and tempword != " ":
                    wordIsIncorrect = True
                    for x in englishWords:
                        if tempword == x:
                            correctWords += 1
                            wordIsIncorrect = False
                    if wordIsIncorrect:
                        incorrectWords += 1
                    tempword = ""
                    totalWords += 1

        finaltext="c81776oa\nFormatting ###################\nNumber of upper case letters changed: " + str(uppercasecounter)+ "\nNumber of punctuations removed: " + str(punctuationcounter)+ "\nNumber of numbers removed: " + str(numbercounter)+ "\nSpellchecking ###################\nNumber of words: " + str(totalWords)+ "\nNumber of correct words: " + str(correctWords)+ "\nNumber of incorrect words: " + str(incorrectWords)
        output.append(finaltext)

for i in range(0,len(output)):
    listofFiles[i] = listofFiles[i][:-4]
    with open(sys.argv[3]+"/"+listofFiles[i]+"_c81776oa.txt", 'w') as f:
        string = output[i]
        f.write(string)
