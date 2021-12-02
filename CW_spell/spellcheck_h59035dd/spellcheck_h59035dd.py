import os
import sys


inputFolder = sys.argv[2]
outputFolder = sys.argv[3]
wordsFile = sys.argv[1]
for file in os.listdir(inputFolder):
    input = open(inputFolder + "/" + file, "r")

    data = input.read()

    upper = 0 #counts uppercase characters
    for element in data:# goes through all characters
        if element.isupper():#checks if character is upper
            upper += 1
    data = data.lower()#removes all uppercase characters

    length = len(data)#length of file

    symbols = ".,?!:;-–[]{}()'\"" #lists of symbols
    i = 0
    punctuation = 0#counts punctuation
    while i < length: #removes all punctuation
        for j in symbols:
            if(data[i] == j):
                if[data[i] == "."]:# I assumed that ellipsis is ...(3 dots in a row)
                    if (i + 2 >= length):#checks if there arent enough chracters for ellipsis
                        data = data[:i] + data[i+1:] #removes current character from file
                        i -= 1 #makes sure we check dont skip anything
                        length -= 1#makes sure that we dont go beyond legth of string
                        punctuation += 1
                        continue#makes sure we dont go over string length in next elif
                    elif(data[i+1] == "." and data[i+2] == "."):#checks for ellipsis
                        data = data[:i] + data[i+3:]
                        i-= 1
                        length -= 3#makes sure that we dont go beyond legth of string
                        punctuation += 1
                    else:
                        data = data[:i] + data[i+1:]
                        i -= 1
                        length -= 1#makes sure that we dont go beyond legth of string
                        punctuation += 1
                else:
                    data = data[:i] + data[i+1:]
                    i -= 1
                    length -= 1
                    punctuation += 1
        i += 1

    i = 0
    numbers = 0#counts numbers
    num = "0123456789"
    while i < length:#removes all numbers and counts them
        for j in num:
            if(data[i] == j):
                data = data[:i] + data[i+1:]#removes number
                i -= 1#makes sure we go through all numbers
                length -= 1
                numbers += 1
        i += 1
    wordsCount = 0
    words = data.split()#makes a list of words in input text
    with open(wordsFile) as f:
        englishList = [line.rstrip('\n') for line in f]#remove \n from file,
    correct = 0
    for word in words:
        wordsCount += 1#counts number of words
        for i in englishList:#checks if word is correct
            if word == i:
                correct += 1
                continue

    if(os.path.isfile(outputFolder + "/" + file[0:len(file) - 4] + "_h59035dd.txt")):
        output = open(outputFolder + "/" + file[0:len(file) - 4] + "_h59035dd.txt", "w")
    else:
        output = open(outputFolder + "/" + file[0:len(file) - 4] + "_h59035dd.txt", "x")
    output.write("h59035dd")
    output.write("\nFormatting ###################")
    output.write("\nNumber of upper case letters changed: " + str(upper))
    output.write("\nNumber of punctuations removed: " + str(punctuation))
    output.write("\nNumber of numbers removed: " + str(numbers))
    output.write("\nSpellchecking ###################")
    output.write("\nNumber of words: " + str(wordsCount))
    output.write("\nNumber of correct words: " + str(correct))
    output.write("\nNumber of incorrect words: " + str(wordsCount - correct))
    input.close()
    output.close()
