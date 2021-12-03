import argparse
import os
import re

# file_input = "T1tT2pT2pT1cT1d"
# file_input = "T1tT2tT2tT2pT2c"
# file_input = "T1cT1pT2tT2tT1t"
# file_output = ""

# Parse command line input
parser = argparse.ArgumentParser()
parser.add_argument('words_path', metavar='path', type=str)
parser.add_argument('input_path', metavar='path', type=str)
parser.add_argument('output_path', metavar='path', type=str)
arguments = parser.parse_args()
words_path = arguments.words_path
input_path = arguments.input_path
output_path = arguments.output_path

# file_input = "The alarm went off and Jake rose awake. Rising early had become a daily ritual, one that he could not fully explain. From the outside, it was a wonder that he was able to get up so early each morning for someone who had absolutely no plans to be productive during the entire day."
words = [word.rstrip() for word in open(words_path).readlines()]

PUNCTUATION = (
    '.', '?', '!', ',', ':', ';', '-', '—', '(', ')',
    '"', "'", '…', '`', '_', '~', '[', ']',
    '{', '}', '|', '\\', '/', '<', '>', '£', '$', '%',
    '&', '*', '+', '=', '¬'
)
UPPER_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def format_input(inp):
    count = {'upper case letters transformed': 0, 'punctuations removed': 0, 'numbers removed': 0}
    offset = 0
    for i in range(len(inp)-1, -1, -1):
        i += offset
        if inp[i] in PUNCTUATION:
            if inp[i] == '.' and i > 1:
                if inp[i-2:i] == '..':
                    second_half = inp[i+1] if i != len(inp) - 1 else ""
                    inp = inp[:i-2] + second_half
                    count['punctuations removed'] += 1
                    offset -= 3
                    continue
            inp = inp.replace(inp[i], '', 1)
            count['punctuations removed'] += 1
        elif inp[i] in UPPER_ALPHABET:
            count['upper case letters transformed'] += 1
        elif inp[i] in "0123456789":
            inp = inp.replace(inp[i], '', 1)
            count['numbers removed'] += 1

    inp = inp.lower()
    output = 'b98919gs\nFormatting ###################\n'
    for key in count:
        output += f"Number of {key}: {count[key]}\n"

    return (inp, output)

def spellcheck(inp, result):
    words_inp = inp.split()
    correct = 0
    for word in words_inp:
        if word in words:
            correct += 1
    result += 'Spellchecking ###################\n'
    result += f'Number of words: {len(words_inp)}\n'
    result += f'Number of correct words: {correct}\n'
    result += f'Number of incorrect words: {len(words_inp)-correct}'
    return result

# Function that writes output file
def write_to_file(file_input, file_name):
    # result = f"{t1_score}:{t2_score}"
    formatted_input, output = format_input(file_input)
    # print(f"{file_name}: {file_input}\n {formatted_input}")
    result = spellcheck(formatted_input, output)
    file_name = file_name.replace(".txt", "")

    # Write to output file
    with open(os.path.join(output_path, f"{file_name}_b98919gs.txt"), 'w') as f:
        f.write(result)

# Files
try:
    os.mkdir(output_path)
except OSError as e:
    print(e)

for file in os.listdir(input_path):
    with open(os.path.join(input_path, file), 'r') as f:
        inp = f.read().rstrip()
        write_to_file(inp, file)
