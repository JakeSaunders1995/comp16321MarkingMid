import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="input file path")
parser.add_argument("input", help="input folder path")
parser.add_argument("output", help="output folder path")
args = parser.parse_args()

EwordPath = args.filename
inputPath = args.input
outputPath = args.output

inputFiles = sorted(os.listdir(inputPath))
outputFiles = sorted(os.listdir(outputPath))

file_num = 0
for x in inputFiles:
    file_num += 1
    input_file = inputPath + '/' + x
    with open(input_file) as inputFile:
        content = inputFile.read()
    inputFile.close()

    with open(EwordPath) as wordsFile:
        EnglishWords = wordsFile.readlines()
    wordsFile.close()

    # create english word list
    Eword_list = []
    for line in EnglishWords:
        word = line.strip()
        Eword_list.append(word)
    alpabet = 'abcdefghijklmnopqrstuvwxyz'
    upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    num = '0123456789'
    formatFile = ''
    upper_count = 0
    remove_num = 0
    remove_pun = 0
    P = 0
    # format the content
    while P < len(content):
        if content[P] in alpabet:
            formatFile += content[P]
            P += 1
        elif content[P] == ' ':
            formatFile += content[P]
            P += 1
        elif content[P] == '\n' or content[P] == '\t':
            formatFile += ' '
            P += 1
        elif content[P] in upper_case:
            Upper = content[P]
            Lower = Upper.lower()
            upper_count += 1
            formatFile += Lower
            P += 1
        elif content[P] in num:
            remove_num += 1
            P += 1
        elif content[P] == '.':
            if P < (len(content)-2) and content[P+1] == '.' and content[P+2] == '.':
                remove_pun += 1
                P += 3
            else:
                remove_pun += 1
                P += 1
        else:
            remove_pun += 1
            P += 1

    # create list of words in file
    fileWord_list = formatFile.split()

    # check the word
    incorrectWord = []
    for w in fileWord_list:
        if w not in Eword_list:
            incorrectWord.append(w)

    output = ''
    output += "n20773yz"
    output += "\nFormatting ###################"
    output += "\nNumber of upper case letters changed: " + str(upper_count)
    output += "\nNumber of punctuations removed: " + str(remove_pun)
    output += "\nNumber of numbers removed: " + str(remove_num)
    output += "\nSpellchecking ###################"
    output += "\nNumber of words: " + str(len(fileWord_list))
    output += "\nNumber of correct words: " + str(len(fileWord_list)-len(incorrectWord))
    output += "\nNumber of incorrect words: " + str(len(incorrectWord))

    if file_num > len(outputFiles):
        output_file = outputPath + '/' + x.replace('.txt', '_n20773yz.txt')
    else:
        output_file = outputPath + '/' + outputFiles[file_num - 1]
    outputFile = open(output_file, "w")
    outputFile.write(output)
    outputFile.close()
    os.rename(output_file, outputPath + '/' + x.replace('.txt', '_n20773yz.txt'))
