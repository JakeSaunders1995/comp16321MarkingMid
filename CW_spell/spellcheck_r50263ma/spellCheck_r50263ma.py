import argparse
import os

parser = argparse.ArgumentParser(description="Calculating the rugby scores")
parser.add_argument("english_words")
parser.add_argument("input_folder")
parser.add_argument("output_folder")
args = parser.parse_args()

words = []
try:
    dictionary = open(args.english_words, "r")
    for line in dictionary:
        line = line.rstrip()
        words.append(line)
except SyntaxError:
    print("Syntax Error")

characters = ["!", "@", "#", "$", "%", "^", "&", "&", "*", "(", ")", "-", "=", "+", "[", "]", "{", "}", ";", ":", "~", "`", "<", ">", ".", ",", "_", "|", "\"", "\'"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

files = os.listdir(args.input_folder)

for f in files:
    if f != ".DS_Store":
        inputFile = open(args.input_folder + "/" + f, 'r')
        outputFileName = f[:-4] + "_r50263ma" + ".txt"
        outputFile = open(args.output_folder + "/" + outputFileName, "w")
        outputFile.write("r50263ma")
        file = inputFile.read()
        splitWords = file.split(" ")
        strippedWords = []
        upperCaseLetters = 0
        numbersInWord = 0
        punctuationsRemoved = 0
        for word in splitWords:
            for letter in word:
                if letter.isupper():
                    upperCaseLetters += 1
                    word = word.lower()
                if letter in numbers:
                    numbersInWord += 1
                    index = word.index(letter)
                    word = word[:index] + word[index+1:]
                if letter in characters:
                    punctuationsRemoved += 1
                    index = word.index(letter)
                    word = word[:index] + word[index+1:]
            if word != "":
                strippedWords.append(word)
        totalWords = len(strippedWords)
        outputFile.write("\nFormatting ##################")
        outputFile.write("\nNumber of upper case words changed: " + str(upperCaseLetters))
        outputFile.write("\nNumber of punctuations removed: " + str(punctuationsRemoved))
        outputFile.write("\nNumber of numbers removed: " + str(numbersInWord))
        outputFile.write("\nSpellchecking ##################")
        numWordsSpeltCorrectly = 0
        numWordsSpeltIncorrectly = 0
        wordsSpeltIncorrectly = []
        for word in strippedWords:
            if word in words:
                numWordsSpeltCorrectly += 1
            else:
                numWordsSpeltIncorrectly += 1
                wordsSpeltIncorrectly.append(word)
        outputFile.write("\nNumber of words: " + str(totalWords))
        outputFile.write("\nNumber of correct words: " + str(numWordsSpeltCorrectly))
        outputFile.write("\nNumber of incorrect words: " + str(numWordsSpeltIncorrectly))
        inputFile.close()
        outputFile.close()
