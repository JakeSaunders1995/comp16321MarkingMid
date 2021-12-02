import argparse
import os
import re

inputs = argparse.ArgumentParser()
inputs.add_argument('dictionary')
inputs.add_argument('input_path') #nargs = number of arguments plus - one or more
inputs.add_argument('output_path')

arguments = inputs.parse_args()

files = []
for file in os.listdir(arguments.input_path):
    files.append(os.path.join(arguments.input_path, file))


for input_file in files:

    f = open(input_file, 'r')
    text = f.readlines()
    f.close()

    i = -1
    while input_file[i] != '/':
        i -= 1

    filename = input_file[i:-4]

    for line in text:
        list_char = []
        for i in range(0, len(line)):
            list_char.append(line[i])

    numbers_removed = 0
    punctuation_removed = 0
    uppercase_changed = 0
    correct_words = 0
    incorrect_words = 0

    i = 0
    while i < len(list_char):
        char = list_char[i]
        if re.match('\d', char):
            numbers_removed += 1
            list_char.remove(char) #make sure this doesnt remove all
            i -= 1
        elif re.match('[^\w\s]', char):
            punctuation_removed += 1
            list_char.remove(char)
            i -= 1
        elif re.match('[A-Z]', char):
            uppercase_changed += 1
            list_char[i] = char.lower()
        i += 1


    new_text = ''.join(list_char)

    list_words = new_text.split(' ')
    while '' in list_words:
        list_words.remove('')

    f = open(arguments.dictionary, 'r')
    dictionary = f.read().splitlines()
    f.close()

    for word in list_words:
        if word in dictionary:
            correct_words += 1
        else:
            incorrect_words += 1

    output_file = arguments.output_path + '/' + filename + '_k78886jb.txt'

    f = open(output_file, 'w')
    f.write('k78886jb\n')
    f.write('Formatting ###################\n')
    f.write('Number of upper case words changed: ' + str(uppercase_changed) + '\n')
    f.write('Number of punctuations removed: ' + str(punctuation_removed) + '\n')
    f.write('Number of numbers removed: ' + str(numbers_removed) +'\n')
    f.write('Spellchecking ###################\n')
    f.write('Number of words: ' + str(len(list_words)) + '\n')
    f.write('Number of correct words: ' + str(correct_words) + '\n')
    f.write('Number of incorrect words: '+ str(incorrect_words) + '\n')
    f.close()
