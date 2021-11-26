import sys, os

# read command line arguments
inputDirectory = sys.argv[1]
outputDirectory = sys.argv[2]

# define variables
alphabet = list("abcdefghijklmnopqrstuvwxyz")
morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

# decrypt a letter encoded using a caeser cipher
def ConvertFromCaeser(letter, distance = 3):
    if letter in alphabet:
        newIndex = alphabet.index(letter) - distance
        if newIndex < 0: newIndex = 26 - abs(newIndex)
        return alphabet[newIndex]
    return letter

# decrypt data depending on encryption method
def GetOutput(dataType, cipherText):
    outputText = ""
    if dataType == "H":
        words = cipherText.split(" ")
        for word in words:
            outputText += chr(int(word, 16))
    elif dataType == "C":
        words = cipherText.split(" ")
        for word in words:
            for letter in word: outputText += ConvertFromCaeser(letter)
            outputText += " "
        outputText = outputText[0:len(outputText) - 1]
    else:
        words = cipherText.split(" / ")
        for word in words:
            letters = word.split(" ")
            for letter in letters:
                if letter in morse:
                    outputText += alphabet[morse.index(letter)]
            outputText += " "
        outputText = outputText[0:len(outputText) - 1]
    return outputText

# go through each file in input folder, write
# output to file in output folder
for root, dirs, files in os.walk(inputDirectory):
    for fileName in files:
        inputPath = inputDirectory + "/" + fileName
        outputPath = outputDirectory + "/" + fileName[:-4] + "_a98056wl.txt"

        file = open(inputPath)
        data = file.readline().replace("\n", " ").strip().split(":")
        file.close()
        outputText = GetOutput(data[0][0], data[1])

        file = open(outputPath, "w")
        file.write(outputText)
        file.close()
