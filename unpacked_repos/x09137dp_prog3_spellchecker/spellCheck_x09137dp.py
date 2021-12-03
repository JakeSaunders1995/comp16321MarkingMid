import os
import sys
import glob

username = "x09137dp"

english = open(sys.argv[1], 'r')
dictionary = english.read().splitlines()

alphabet = "abcdefghijklmnopqrstuvwxyz"
digits =   "0123456789"
punctuations = [".", "?", "!", ",", ":",
                ";", "-", "(", ")", "{",
                "}", "[", "]", "'", '"',
                "—"]

for file in glob.iglob(sys.argv[2] + "/**"):
    input = open(file, 'r') #Opens input file in read only mode

    proofRead = []
    modText = ""

    upper = 0
    symbols= 0
    numbers = 0
    dotCounter = 0 #used to check if punctuation is an ellipsis

    #Removes numbers and punctuation from text
    text = input.read()
    for char in text:
        if char.casefold() in alphabet or char == " ":
            modText = modText + char
            if char in alphabet:
                dotCounter = 0
            #Finds all capital letters in text
            if char not in alphabet and char != " ":
                upper += 1
        elif char in digits: #Finds all numbers in text
            numbers += 1
            dotCounter = 0
        elif char in punctuations: #Finds all punctuation in text
            if char == ".":
                dotCounter +=1
                if dotCounter == 3: #Identifies if punctuation was an ellipsis
                    symbols -= dotCounter - 1
            else:
                dotCounter = 0
            symbols += 1
        if char == "/":
            modText = modText + " "

    modText = modText.lower() #Changes text to lowercase
    modText = ' '.join(modText.split()) #Removes extra whitespace from the text

    #Splits text into a list of words
    word = ""
    for char in modText:
        if char != " ":
            word = word + char
        else:
            proofRead.append(word)
            word = ""
    proofRead.append(word) #adds last word in text to the list

    correctWords = 0
    incorrectWords = 0

    for word in proofRead:
        if word in dictionary:
            correctWords += 1
        else:
            incorrectWords += 1

    path, filenameExt = os.path.split(file)
    filename, extentsion = os.path.splitext(filenameExt)

    outputPath = os.path.join(sys.argv[3], filename + "_" + username + ".txt")
    output = open(outputPath, 'w') #Creates and opens output file in write mode

    output.write(username + "\n")
    output.write("Formatting ###################\n")
    output.write("Number of upper case letters changed: " + str(upper) + "\n")
    output.write("Number of punctuations removed: " + str(symbols) + "\n")
    output.write("Number of numbers removed: " + str(numbers) + "\n")
    output.write("Spellchecking ###################\n")
    output.write("Number of words: " + str(len(proofRead)) + "\n")
    output.write("Number of correct words: " + str(correctWords) + "\n")
    output.write("Number of incorrect words: " + str(incorrectWords) + "\n")

    output.close()
    input.close()
