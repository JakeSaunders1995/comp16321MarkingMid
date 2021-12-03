import sys
import os

def solve(input_str, file, engFile):
    file.write('Formatting ###################\n')
    upper = 0
    punc = 0
    numb = 0
    str = ''
    for i in input_str:
        if (i >= 'A' and i <= 'Z'):
            str += i.lower()
            upper = upper + 1
        elif (i >= '0' and i <= '9'):
            numb = numb + 1
        elif (i >= 'a' and i <= 'z') :
            str += i
        elif (i > chr(32) and i < chr(127)):
            punc = punc + 1
        else :
            str += i
    # file.write(str)
    file.write('Number of upper case letters changed: {}\n'.format(upper))
    file.write('Number of punctuations removed: {}\n'.format(punc))
    file.write('Number of numbers removed: {}\n'.format(numb))
    file.write('Spellchecking ###################\n')
    # print(engFile.read())
    engMap = engFile.read().split()
    inputMap = str.split()
    incorrect = 0
    for i in inputMap:
        if not (i in engMap):
            incorrect += 1
    file.write('Number of words: {}\n'.format(len(inputMap)))
    file.write('Number of correct words: {}\n'.format(len(inputMap) - incorrect))
    file.write('Number of incorrect words: {}\n'.format(incorrect))
    return 

if __name__ == '__main__':
    englishWords = sys.argv[1]
    input_folder = sys.argv[2]
    output_folder = sys.argv[3]
    myName = 't28063tz'
    # print(input_folder, output_folder)
    all_files = []
    for i in os.listdir(os.getcwd() +'/' + input_folder):
        all_files.append(i)
    for fileName in all_files:
        file = open(os.getcwd() + '/' + input_folder + '/' + fileName , "r")
        engFile = open(os.getcwd() + '/' + englishWords, "r")
        input_str = file.read()
        file.close()
        output_file = fileName.split('.txt')[0] + '_' + myName + '.txt'
        file = open(os.getcwd() + '/' + output_folder + '/' + output_file, "w")
        file.write(myName + '\n')
        solve(input_str, file, engFile)
        file.close()
#python3 spellcheck_t28063tz.py ./EnglishWords.txt ./Example_inputs_program3 ./test_out
