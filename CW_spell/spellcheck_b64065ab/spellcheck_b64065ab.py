import argparse, os

parser = argparse.ArgumentParser()
parser.add_argument('EnglishWords', type = argparse.FileType('r'))
parser.add_argument('input_directory')
parser.add_argument('output_directory')
args = parser.parse_args()

input_directory = args.input_directory
output_directory = args.output_directory
EnglishWords = args.EnglishWords

numbers = '0123456789'
punctuation = ',.@[]()!#$%^&*-_=+"\'"\{\}:;?></|\\'
upperCase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
dicts = EnglishWords.read()
wordList = dicts.split("\n")

i = 1
for filename in os.scandir(input_directory):
    if filename.is_file():
        f = open(filename.path)
        text = f.read()
        upperCaseCount, punctuationCount, numbersCount = 0, 0, 0
        for char in text:
            if char in numbers:
                numbersCount += 1
                index = text.index(char)
                text=text[:index]+text[index+1:] 
            elif char in punctuation:
                punctuationCount += 1
                index = text.index(char)
                text=text[:index]+text[index+1:]
            elif char in upperCase: 
                upperCaseCount += 1

        text = text.lower()
        text = text.split(" ")


        correctWords, incorrectWords = 0, 0
        for word in text:
            word = word.strip()
            if word in wordList:
                correctWords += 1
            elif word == "" or word == " ":
                pass
            else:
                incorrectWords += 1
        
        cwd = os.getcwd()
        os.chdir(output_directory)
        outputname  = "test_file" + str(i) + "_b64065ab.txt"
        output = open(outputname, "w")
        output.write(
            "b64065ab \nFormatting ###################\nNumber of upper case words changed: "+ str(upperCaseCount) + "\n" + 'Number of punctuations removed: ' + str(punctuationCount) + "\n" + 'Number of numbers removed: ' + str(numbersCount) + "\n" + 'Spellchecking ###################\n' + 'Number of words: ' + str(correctWords+incorrectWords) + "\n" + 'Number of correct words: ' + str(correctWords) + "\n" +  'Number of incorrect words: ' + str(incorrectWords) + "\n"
            )
        # output.write("b64065ab \n")
        # output.write("Formatting ###################\n")
        # output.write('Number of upper case words changed: ' + str(upperCaseCount) + "\n")
        # output.write('Number of punctuations removed: ' + str(punctuationCount) + "\n")
        # output.write('Number of numbers removed: ' + str(numbersCount) + "\n")
        # output.write('Spellchecking ###################\n')
        # output.write('Number of words: ' + str(correctWords+incorrectWords) + "\n")
        # output.write('Number of correct words: ' + str(correctWords) + "\n")
        # output.write('Number of incorrect words: ' + str(incorrectWords) + "\n")

        output.close()
        i += 1
        os.chdir(cwd)
        cwd = ""