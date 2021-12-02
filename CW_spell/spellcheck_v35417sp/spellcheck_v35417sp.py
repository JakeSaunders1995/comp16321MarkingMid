import argparse
import os
import re

parser = argparse.ArgumentParser(
        description="Spellcheck program"
    )
parser.add_argument(
        "english_words"
    )
parser.add_argument(
        "inp_folder"
    )
parser.add_argument(
        "out_folder"
    )
args = parser.parse_args()

if not os.path.isdir(args.out_folder):
    os.mkdir(args.out_folder)

username = "v35417sp"
for input in sorted(os.listdir(args.inp_folder)):
    name = re.match('(.*)\.txt', input).groups()[0]
    name += f"_{username}.txt"

    with open(args.inp_folder + "/" + input, 'r') as f:
        data = f.read()

    with open(args.english_words, 'r') as f:
        words = f.read().strip().splitlines()

    def sum_chars(text, charset):
        return sum([text.count(c) for c in charset])

    def rm_chars(text, charset):
        for c in charset:
            text = text.replace(c, "")
        return text

    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    ascii = "abcdefghijklmnopqrstuvwxyz"
    ascii += ascii.upper()
    numbers = "0123456789"

    count_punc = sum_chars(data, punctuation)
    count_nums = sum_chars(data, numbers)
    count_capital = len(re.findall("[A-Z][a-z]*", data))

    data = rm_chars(data, punctuation)
    data = rm_chars(data, numbers)
    data = data.lower()

    data = ' '.join(data.splitlines()).split(' ')
    data = [i for i in data if i != '']
    count_words = len(data)

    correct, wrong = [], []
    for w in data:
        if len(w) == 0:
            continue
        if w in words:
            correct.append(w)
        else:
            wrong.append(w)

    output = f"""{username}
Formatting ###################
Number of upper case words changed: {count_capital}
Number of punctuations removed: {count_punc}
Number of numbers removed: {count_nums}
Spellchecking ###################
Number of words: {count_words}
Number of correct words: {len(correct)}
Number of incorrect words: {len(wrong)}"""

    f = open(args.out_folder + "/" + name, 'w')
    f.write(output)
    f.close()
