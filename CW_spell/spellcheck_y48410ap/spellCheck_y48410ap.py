import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("english")
parser.add_argument("input")
parser.add_argument("output")
parser = parser.parse_args()

english_words_file = open(parser.english, 'r')
english_words = english_words_file.read()
english_words = english_words.splitlines()

input_folder = parser.input + '/'
output_folder = parser.output + '/'


for input_file in os.scandir(input_folder):
    input_file = input_file.path
    
    output_file = open(output_folder + os.path.basename(input_file)[:-4] + "_y48410ap.txt", 'w')
    input_file = open(input_file, 'r')

    text = input_file.read()

    alph = "abcdefghijklmnopqrstuvwxyz "
    Alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    punctuations = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~\t\n\r\x0b\x0c'

    number_number = 0
    upper_number = 0
    punctuation_number = 0

    for number in numbers:
        number_number += text.count(number)
        
    for letter in Alph:
        upper_number += text.count(letter)
        
    for punctuation in punctuations:
        punctuation_number += text.count(punctuation)

    output = 'y48410ap\n'
    output += "Formatting ###################" + '\n'
    output += "Number of upper case words changed: " + str(upper_number) + '\n'
    output += "Number of punctuations removed: " + str(punctuation_number) + '\n'
    output += "Number of numbers removed: " + str(number_number) + '\n'

    text = text.lower()
    text = list(filter(lambda x: alph.find(x) != -1, text))
    text = ''.join(text)
    text = text.split(' ')
    text = list(filter(lambda x : x!='', text))

    total_words = len(text)
    correct_words = 0

    for word in text:
        if word in english_words:    
            correct_words+=1

    incorrect_words = total_words - correct_words

    output += "Spellchecking ###################" + '\n'
    output += "Number of words: " + str(total_words) + '\n'
    output += "Number of correct words: " + str(correct_words) + '\n'
    output += "Number of incorrect words: " + str(incorrect_words) + '\n'

    output_file.write(output)

    input_file.close()
    output_file.close()

english_words_file.close()