import os
import argparse

#to get the input information.
def commandSystem(state):
    parser = argparse.ArgumentParser(description='Path of the Input and Output')
    parser.add_argument('inputFolder', type=str, help='Input Folder Path')
    parser.add_argument('outputFolder', type=str, help='Output Folder Path')
    args = parser.parse_args()

    folderIput = args.inputFolder
    dirsIput = os.listdir(folderIput)
    
    if state == 1:
        for file1 in dirsIput:  
            filePath = os.path.join(folderIput, file1)
            fileCotent = open(filePath, "rt")
            content = fileCotent.read()
            fileCotent.close()
            content_lis.append(content)
        return content_lis

    if state == 0:
        folderOput = args.outputFolder
        for file1 in dirsIput:
            file2 = file1[:-4] + "_c29824zl.txt"
            outputPath = os.path.join(folderOput, file2)
            path_lis.append(outputPath)
        return path_lis

def hexadecimalCode(target):
    lis_num = list(target.split(' '))
    i = 0 
    finalResult = ""
    while i < len(lis_num):
        if lis_num[i] != '\n':
            result = chr(int(lis_num[i], 16))
            finalResult = finalResult + result
        i += 1
    return finalResult.lower()

def caesarCode(target):
    lis_scentence = list(target.split(' '))
    i = 0
    finalResult = ""
    while i < len(lis_scentence):
        lis_word = lis_scentence[i]
        result = ""
        letterPosition = 0
        lis_special = ["a", 'b', "c"]
        while letterPosition < len(lis_word):
            wordChar = lis_word[letterPosition]
            if wordChar != '\n':
                charValue = ord(wordChar)
                if wordChar not in lis_special: 
                    charValue -= 3
                    result += chr(charValue)
                else:
                    charValue += 23
                    result += chr(charValue)
            letterPosition += 1
        result += " "
        i += 1
        finalResult += result
    return finalResult

def morseCode(target):
    morseDict = {
        ".-": "a", "-...": "b", "-.-.": "c", "-..": "d", ".": "e",
        "..-.": "f", "--.": "g", "....": "h", "..": "i", ".---": "j",
        "-.-": "k", ".-..": "l", "--": "m", "-.": "n", "---": "o",
        ".--.": "p", "--.-": "q", ".-.": "r", "...": "s", "-": "t",
        "..-": "u", "...-": "v", ".--": "w", "-..-": "x", "-.--": "y", "--..": "z",

        "-----": "0", ".----": "1", "..---": "2", "...--": "3", "....-": "4",
        ".....": "5", "-....": "6", "--...": "7", "---..": "8", "----.": "9",

        ".-.-.-": ".", "---...": ",", "--..--": ",", "-.-.-.": ";", "..--..": "?", 
        "-...-": "=", ".----.": "'", "-..-.": "/", "-.-.--": "!", "-....-": "-", 
        "..--.-": "_", ".-..-.": "", "-.--.": "(", "-.--.-": ")", "...-..-": "$", 
        ".-...": "&", ".--.-.": "@", ".-.-.": "+", 
    }
    
    lis_scentence = list(target.split('/'))
    i = 0
    finalResult = ""
    while i < len(lis_scentence):
        lis_target = lis_scentence[i]
        lis_target = list(lis_scentence[i].split(' '))
        result = ""
        for item in lis_target:
            if item != '\n':
                if item in morseDict.keys():
                    result = result + morseDict[item]
        result = result + ' '
        finalResult = finalResult + result
        i += 1
    return finalResult


content_lis = []
path_lis = []
count = 0
finalResult = ""
commandSystem(1)
commandSystem(0)
while count < len(content_lis):
    singleText = content_lis[count]
    if singleText[0] == "H" or singleText[0] == "h":
        wordlist = list(singleText.split(':'))
        f = open(path_lis[count], "w")
        f.write(hexadecimalCode(wordlist[1]))
        f.close()
    elif singleText[0] == "C" or singleText[0] == "c":
        wordlist = list(singleText.split(':'))
        f = open(path_lis[count], "w")
        f.write(caesarCode(wordlist[1]))
        f.close()
    elif singleText[0] == "M" or singleText[0] == "m":
        wordlist = list(singleText.split(':'))
        f = open(path_lis[count], "w")
        f.write(morseCode(wordlist[1]))
        f.close()
    count += 1