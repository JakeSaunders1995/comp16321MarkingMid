import os, re, argparse

from pathlib import Path
DIR = Path(__file__).parent.absolute()
os.chdir(DIR)

parser = argparse.ArgumentParser()
parser.add_argument("words_file", help="The file containing every English word as you do")
parser.add_argument("input_folder", help="The folder that contains the input files for the program")
parser.add_argument("output_folder", help="The folder that will contain the output files for the program")
args = parser.parse_args()
# python3 spellcheck_k42524cm.py ../EnglishWords.txt ../Example_inputs/Example_inputs_program3 ../Example_outputs/Example_outputs_program3

f = open(args.words_file, 'r')
words = dict.fromkeys(f.read().split('\n'))
f.close()

punct = r'''.?!,:;–-(){}[]'"…'''

def Words(ex1):
    ex1 = ex1.replace('...','…').replace('\n', ' ')
    count = {
        'Upper': 0,
        'Punctuation': 0,
        'Numbers': 0,
        'Words': 0,
        'Wrong': 0
    }

    message = ''

    for char in ex1:
        if char in punct:
            count['Punctuation'] += 1
        elif re.match('\d', char):
            count['Numbers'] += 1
        elif char != char.lower():
            count['Upper'] += 1
            message += char.lower()
        else:
            message += char

    text = []
    for word in message.split(' '):
        if word:
            text.append(word)

    count['Words'] = len(text)

    for word in text:
        if word not in words:
            count['Wrong'] += 1

    final = 'k42524cm\n'
    final += 'Formatting ###################\n'
    final += f"Number of upper case letters changed: {count['Upper']}\nNumber of punctuations removed: {count['Punctuation']}\nNumber of numbers removed: {count['Numbers']}\n"
    final += 'Spellchecking ###################\n'
    final += f"Number of words: {count['Words']}\nNumber of correct words: {count['Words']-count['Wrong']}\nNumber of incorrect words: {count['Wrong']}"
    return final

# .?!,:;–-(){}[]'"…

def write(input_file, output_file):
    f = open(input_file, 'r')
    message = f.read()
    f.close()

    message = Words(message)

    f = open(output_file, 'w')
    f.write(message)
    f.close()

for file in os.listdir(args.input_folder):
    output_file = re.sub('\.txt$', '', file)
    file = f'{args.input_folder}/{file}'
    output_file = f'{args.output_folder}/{output_file}_k42524cm.txt'
    write(file, output_file)
