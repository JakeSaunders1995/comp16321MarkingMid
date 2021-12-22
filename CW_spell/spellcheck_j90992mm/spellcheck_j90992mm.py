import argparse
import os
import string

parser = argparse.ArgumentParser()
parser.add_argument("echo_dictionary")
parser.add_argument("echo_i")
parser.add_argument("echo_o")
args = parser.parse_args()

dictionary = args.echo_dictionary
i_path = args.echo_i
o_path = args.echo_o

os.chdir(i_path)

# Capital
c = 0
# Punctuation
p = 0
# Number
n = 0
# Total Words
w = 0
# Correct Words
cw = 0
# Incorrect Words
iw = 0

global outText

punctuations = string.punctuation
numbers = string.digits
capital = string.ascii_uppercase


def read_text_file(file_path):
    with open(file_path, 'r') as f:
        uText = f.read()
        spell_check(uText)


def get_words(file_name):
    word_arr = []
    with open(file_name, 'r') as f:
        for line in f:
            word_arr.append(line.replace("\n", ""))
    return word_arr


def spell_check(uText):
    english_words = get_words(dictionary)
    for char in uText:
        if char in punctuations:
            uText = uText.replace(char, "")
            global p
            p += 1      
        if char in numbers:
            uText = uText.replace(char, "")
            global n
            n += 1
        if char in capital:
            uText = uText.replace(char, char.lower())
            global c
            c += 1
    word = uText.split(" ")
    for wor in word:
        global w
        
        if wor in ["\n", ""]: #check if this is alright
            continue
        
        if wor in english_words:
            global cw
            cw += 1
        else:
            global iw
            iw += 1
        w = iw + cw
    output(file_path)


def output(file_path):
    global c, p, n, w, cw, iw
    os.chdir(o_path)
    with open(file_path, 'a') as k:
        k = open(file[:-4] + "_j90992mm.txt", 'w')
        k.write("j90992mm""\nFormatting###################""\nNumber of upper case letters changed:" + str(c) + "\nNumber of punctuations removed:" + str(p) + "\nNumber of numbers removed:" + str(n) + "\nSpellchecking ###################""\nNumber of Words:" + str(w) + "\nNumber of correct words:" + str(cw) + "\nNumber of incorrect words:" + str(iw))
        k.close()
    os.chdir(i_path)
    c = 0
    p = 0
    n = 0
    w = 0
    cw = 0
    iw = 0


# File Repeater
for file in os.listdir():
    file_path = f"{i_path}\{file}"
    read_text_file(file_path)