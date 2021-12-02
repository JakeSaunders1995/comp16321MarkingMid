import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("input_filepath_englishwords", help="input file path of englishwords.txt")
parser.add_argument("input_filepath", help="input file path")
parser.add_argument("output_filepath", help="output file path")
args = parser.parse_args()
args.input_filepath_englishwords = os.path.abspath(args.input_filepath_englishwords)
args.input_filepath = os.path.abspath(args.input_filepath)
args.output_filepath = os.path.abspath(args.output_filepath)

for file_name in os.listdir(args.input_filepath):
    os.chdir(args.input_filepath)

    with open(os.path.join(os.getcwd(), file_name), 'r') as f:
        text1 = open((os.path.join(os.getcwd(), file_name)), "r")
        text = ""
        for line in text1:
            line = line.rstrip()
            text += line

        numbers = "0123456789"
        punc = '''!()-[]{};:'"\,<>./?_…'''
        engwords = []
        file = open(args.input_filepath_englishwords, "r")
        for line in file:
            line = line.rstrip()
            engwords.append(line)

        emp_text = ''
        punc_transformed = 0
        num_rm = 0
        upper_transformed = 0
        incorrect_words = 0
        correct_words = 0

        for i in text:
            emp_text += i

        emp_text = emp_text.replace("...", ".")

        for letter in emp_text:
            if letter in numbers:
                emp_text = emp_text.replace(letter, "")
                num_rm += 1
            if letter in punc:
                emp_text = emp_text.replace(letter, "")
                punc_transformed += 1
            if letter.isupper():
                upper_transformed += 1
        
        emp_text = emp_text.lower()

        numofwordsinfile = 0
        numofwords = emp_text.split()
        for word in range(0, len(numofwords)):
            numofwordsinfile += 1

        for word in numofwords:
            if word in engwords:
                correct_words += 1
            else:
                continue

        incorrect_words = numofwordsinfile - correct_words



    os.chdir(args.output_filepath)
    file_name = file_name[:-4] + "_t17981qx.txt"
    with open(file_name, 'w') as d:
        d.write(str("t17981qx" + "\nFormatting ###################" + "\nNumber of upper case letters changed: " +
                    str(upper_transformed) +
                    "\nNumber of punctuations removed: " + str(punc_transformed) +
                    "\nNumber of numbers removed: " + str(num_rm)
                    + "\nSpellchecking ###################" + "\nNumber of words: " + str(numofwordsinfile) +
                    "\nNumber of correct words: " + str(correct_words) +
                    "\nNumber of incorrect words: " + str(incorrect_words)))











