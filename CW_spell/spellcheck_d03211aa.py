import os
import argparse
import sys

username = "_d03211aa"

parser = argparse.ArgumentParser()

parser.add_argument('englishWords')

parser.add_argument('inputs')

parser.add_argument('outputs')

args = parser.parse_args()


files = sorted(os.listdir(args.inputs))


for filename in files:
    file = open(args.inputs.strip("./") + '/' + filename)

    text = ""
    for line in file:
        text += line

    

    words_list = text.split()
    file = open(args.english_words, "r")
    english_words = file.read()

    upper_words = 0
    alphabet = ['a', 'b', 'c', 'd', 'e',
                'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o',
                'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z']
    punctuation = 0
    punctuation_str = '''!()-[]{};:'"\,<>./?$%^&*_~'''
    numbers = 0
    numbers_str = "0123456789"
    correct_words = 0
    incorrect_words = 0

    for num in range(len(words_list)):
        letters_list = [char for char in words_list[num]]


        if "'" in letters_list:
            quotation_index = letters_list.index("'")
            if quotation_index != 0 and quotation_index != (len(letters_list) - 1):
                if letters_list[quotation_index - 1] == 'n' and letters_list[quotation_index + 1] == 't':
                    letters_list[quotation_index - 1] = ''

                for i in range(quotation_index + 1, len(letters_list)):
                    if letters_list[i] in alphabet:
                        letters_list[i] = ''

        for i in range(len(letters_list)):
            if letters_list[i] == '':
                continue

            if letters_list[i] in punctuation_str:
                letters_list[i] = ''
                punctuation += 1

            if letters_list[i].isupper() and letters_list[i] != '':
                letters_list[i] = letters_list[i].lower()
                upper_words += 1

            if letters_list[i] in numbers_str and letters_list[i] != '':
                letters_list[i] = ''
                numbers += 1

        word = ''.join(letters_list)

        if word != '':
            if word in english_words:
                correct_words += 1
            else:
                incorrect_words += 1
                

    words_count = correct_words + incorrect_words

    if filename[-4:] == ".txt": 
        edited_filename = filename[:len(filename) - 4] + username + ".txt"
    else:
        edited_filename = filename + username

    file = open(args.outputs.strip("./") + '/' + edited_filename, "w")

    file.write(username[1:] + '\n')
    file.write("Formatting " + "###################" + '\n')
    file.write("Number of upper case letters changed: " + str(upper_words) + '\n')
    file.write("Number of punctuations removed:" + str(punctuation) + '\n')
    file.write("Number of numbers removed:" + str(numbers) + '\n')
    file.write("Spellchecking " + "###################" + '\n')
    file.write("Number of words:" + str(words_count) + '\n')
    file.write("Number of correct words:" + str(correct_words) + '\n')
    file.write("Number of incorrect words:" + str(incorrect_words) + '\n')

    file.close()
