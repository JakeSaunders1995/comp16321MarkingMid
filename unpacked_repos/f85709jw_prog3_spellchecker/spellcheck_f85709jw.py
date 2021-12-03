import sys
import os

username = "f85709jw"
dictionary = sys.argv[1]
inputPath = sys.argv[2]
outputPath = sys.argv[3]

def isNum(number):
    try:
        float(number)
        return True
    except:
        return False

for inp in os.listdir(inputPath):
    # formatting
    upperTransformed = 0
    puncRemoved = 0
    numsRemoved = 0
    # spellchecking
    numWords = 0
    correctWords = 0
    incorrectWords = 0

    formattedText = ""
    dictionaryWords = []
    with open(dictionary) as d:
        for word in d:
            formattedWord = word[:-1]
            dictionaryWords.append(formattedWord)

    with open(inputPath + '/' + inp) as f:
        for line in f:
            words = line.split(" ")
            for word in words:
                numWords += 1
                formattedWord = ""
                for letter in word:
                    if letter != letter.lower():
                        upperTransformed += 1
                        formattedText += letter.lower()
                        formattedWord += letter.lower()
                    elif isNum(letter):
                        numsRemoved += 1
                    elif ord(letter) > 122 or ord(letter) < 97:
                        puncRemoved += 1
                    else:
                        formattedText += letter
                        formattedWord += letter
                if formattedWord == "":
                    numWords -= 1
                    continue
                if formattedWord in dictionaryWords:
                    correctWords += 1
                else:
                    incorrectWords += 1
                formattedText += " "
        formattedText = formattedText[0:-1]

    if not os.path.exists(outputPath):
        os.makedirs(outputPath)

    with open(outputPath + '/' + inp[0:-4] + '_' + username + '.txt', "w") as f:
        f.write(username + "\n")
        f.write("Formatting ###################\n")
        f.write("Number of upper case words changed: " + str(upperTransformed) + "\n")
        f.write("Number of punctuations removed: " + str(puncRemoved) + "\n")
        f.write("Number of numbers removed: " + str(numsRemoved) + "\n")
        f.write("Spellchecking ###################" + "\n")
        f.write("Number of words: " + str(numWords) + "\n")
        f.write("Number of correct words: " + str(correctWords) + "\n")
        f.write("Number of incorrect words: " + str(incorrectWords) + "\n")



