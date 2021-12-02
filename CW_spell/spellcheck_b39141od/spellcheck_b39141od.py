import sys
import os

files = os.listdir(sys.argv[2])

f = open(sys.argv[1],'r')
englishWords = f.read().split("\n")
f.close()

for file in files:

    f = open(os.path.join(sys.argv[2], file),'r')
    text = f.read()
    text = text.replace("\n"," ")
    text = text.split(" ")
    f.close()


    corrected = []

    upperCases = 0
    punctuations = 0
    numbers = 0
    correct = 0
    incorrect = 0

    for word in text:
        newWord = ""
        i = 0
        while i < len(word):
            char = word[i]
            if char in "0123456789":
                numbers += 1
                i += 1
                continue
            elif char == "." and word[i:i+3] == "...":
                punctuations += 1
                i += 3
                continue
            elif char in ".?!,:;-–(){}[]'\"":
                punctuations += 1
                i += 1
                continue
            elif char.lower() != char:
                upperCases += 1
                char = char.lower()
                newWord += char
                i += 1
                continue
            elif char in "abcdefghijklmnopqrstuvwxyz":
                newWord += char
                i += 1
                continue
            else:
                i += 1
                continue

#        for char in word:
#            if char in "0123456789":
#                numbers += 1
#                continue
#            elif char in ".?!,:;-–(){}[]'\"…":
#                punctuations += 1
#                continue
#            elif char.lower() != char: #if lowercase isnt same as regular then char must be uppercase
#                upperCases += 1
#                newWord += char.lower()
#            elif char in 'abcdefghijklmnopqrstuvwxyz': #should be fine now, but make sure
#                newWord += char
#            else:
#                continue
        if newWord != "": #make sure new word isnt empty
            corrected.append(newWord)
    for word in corrected:
        if word in englishWords:
            correct += 1
        else:
            incorrect += 1

    output =["b39141od","Formatting ###################",
    "Number of upper case letters changed: "+str(upperCases),
    "Number of punctuations removed: "+str(punctuations),
    "Number of numbers removed: "+str(numbers),
    "Spellchecking ###################",
    "Number of words: "+str(len(corrected)),
    "Number of correct words: "+str(correct),
    "Number of incorrect words: "+str(incorrect)]

    output = "\n".join(output)
    o = o = open(os.path.join(sys.argv[3], file[:-4]+"_b39141od.txt"),'w')
    o.write(output)
    o.close()
