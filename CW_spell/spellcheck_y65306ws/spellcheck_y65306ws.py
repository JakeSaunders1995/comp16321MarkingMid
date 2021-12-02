import argparse, re
parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("output")
args = parser.parse_args()
inputFile = args.input
outputFile = args.output
file = open(inputFile, "r")
text = ""
for line in file:
    text += line
file = open(outputFile, "w")
file.write("Formatting ###################\n")
length = len(text)
for x in range(0,9):
    text = text.replace(str(x),"")
file.write("Number of numbers removed: " + str(length - len(text)) + "\n")
length = len(text)
text = re.sub(r'[^\w\s]', '', text)
file.write("Number of punctuation's removed: " + str(length - len(text)) + "\n")
upperCount = 0
newWord = False
for x in range(len(text)):
    if text[x] == " ":
        newWord = True
        continue
    if text[x].isupper() == True and newWord == True:
        upperCount += 1
        newWord = False
text = text.lower()
file.write("Number of uppercase words transformed: " + str(upperCount)+ "\n")
file.write("Spellchecking ###################\n")
wordCount = 0
wordList = list(str())
word = ""
for x in range(len(text)):
    if text[x] == " ":
        wordList.append(word)
        wordCount += 1
        word = ""
    else:
        word += text[x]
wordList.append(word)
wordCount += 1
file.write("Number of words in file: " + str(wordCount)+ "\n")
englishWords = list(str())
fileTwo = open("/home/csimage/16321_python_coursework_y65306ws/EnglishWords.txt", "r")
for line in fileTwo:
    englishWords.append(line.replace("\n", ""))
correct = False
correctCount = 0
for x in range(len(wordList)):
    for y in range(len(englishWords)):
        if wordList[x] == englishWords[y]:
            correct = True
    if correct == True:
        correctCount += 1
    correct = False 
file.write("Number of correct words in file: " + str(correctCount) + "\n")
file.write("Number of incorrect words in file: " + str(wordCount-correctCount))