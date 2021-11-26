from argparse import ArgumentParser
import os
import re

def format(text):
    full_text = "Formatting ###################\n"
    new_text = ""
    num_upper = 0
    num_punc = 0
    num_num = 0
    c = 0
    if '...' in text:
        text = text.replace('...', '')
        num_punc +=1
    for char in text:
        if char.isupper():
            num_upper += 1
            new_text = new_text + char.lower()
            continue
        elif char in ['.', ':', ';', '?', ',', '!', '...', "'", '"', '[', ']', '{', '}', '(', ')', '/', '-', '–']:
            num_punc += 1
            continue
        elif char in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            num_num += 1
            continue
        new_text = new_text + char
    new_text = re.sub('\\s+', ' ', new_text)
    full_text = full_text + "Number of upper case words changed: " + str(num_upper) + "\n" + "Number of punctuations removed: " + str(num_punc) + "\n" + "Number of numbers removed: " + str(num_num)
    return new_text, full_text

def spellcheck(text):
    full_text = "Spellchecking ###################\n"
    text = text.split(" ")
    num_cor = 0
    num_inc = 0
    word_count = 0
    for word in text:
        if word == "":
            continue

        if word in dic:
            num_cor += 1

        elif word not in dic:
            num_inc +=1
        word_count += 1
    full_text = full_text + "Number of words: " + str(word_count) + "\n" + "Number of correct words: " + str(num_cor) + "\n" + "Number of incorrect words: " + str(num_inc)
    return full_text

parser = ArgumentParser()
parser.add_argument('EnglishWords')
parser.add_argument('input_folder')
parser.add_argument('output_folder')
args = parser.parse_args()

eng_file = args.EnglishWords
dirname_i = args.input_folder
dirname_o = args.output_folder

with open(eng_file) as f:
    dic = f.read().split("\n")

for filename in os.listdir(args.input_folder):
   with open(os.path.join(dirname_i, filename)) as f:
       text = f.read()

       variable1 = format(text)
       text = variable1[0]

       variable2 = spellcheck(text)

       filename_o = filename.split(".")[0] + "_y44694jk.txt"
       with open(os.path.join(dirname_o, filename_o), 'w') as f_o:
           f_o.write("y44694jk"+"\n")
           f_o.write(variable1[1]+"\n")
           f_o.write(variable2)
