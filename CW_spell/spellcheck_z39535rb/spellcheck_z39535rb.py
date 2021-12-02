import argparse
import os


parser = argparse.ArgumentParser(
    description="file path, recommend to use absolute path")
parser.add_argument("wordFilePath", type=str, help="English words file path")
parser.add_argument("inputPath", type=str, help="input folder path")
parser.add_argument("outputPath", type=str, help="output folder path")
args = parser.parse_args()

# method to create file path
checkFilePath = args.wordFilePath

inputPath = args.inputPath
fileList = os.listdir(inputPath)
fileList.sort()

outputPath = args.outputPath

# english spelling checking document
checkList = []
with open(checkFilePath) as wordList:
    for checkWord in wordList:
        checkWord = checkWord.rstrip()
        checkList.append(checkWord)
    wordList.close()


# actual functionality
for file in fileList:
    with open(inputPath + "/" + file) as f:
        text = f.readline()
        textSplit = text.split()

        upperCase = 0
        punctuation = 0
        numbers = 0

        words = 0
        correctWords = 0
        incorrectWords = 0

        for word in textSplit:
            final = ''

            # Formatting
            for char in word:
                if 65 <= ord(char) <= 90:
                    upperCase += 1
                    final += chr(ord(char) + 32)
                elif 33 <= ord(char) <= 47 or 58 <= ord(char) <= 64 or 91 <= ord(char) <= 96 or 123 <= ord(char) <= 126:
                    punctuation += 1
                    final += ''
                elif 48 <= ord(char) <= 57:
                    numbers += 1
                    final += ''
                elif 97 <= ord(char) <= 122:
                    final += char

            # Spellchecking
            if len(final) > 0:
                words += 1
                if final in checkList:
                    correctWords += 1
                else:
                    incorrectWords += 1

    # output the result
    with open(outputPath + '/' + file[:-4] + '_z39535rb.txt', 'w') as s:
        s.write('z39535rb' +
                '\nFormatting ###################' +
                '\nNumber of upper case words changed: ' + str(upperCase) +
                '\nNumber of punctuations removed:' + str(punctuation) +
                '\nNumber of numbers removed: ' + str(numbers) +
                '\nSpellchecking ###################' +
                '\nNumber of words: ' + str(words) +
                '\nNumber of correct words: ' + str(correctWords) +
                '\nNumber of incorrect words: ' + str(incorrectWords))
    s.close()
    f.close()
