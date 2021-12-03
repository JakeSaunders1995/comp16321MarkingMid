import argparse
import string
import os

parser = argparse.ArgumentParser()
parser.add_argument('dictionary', type=argparse.FileType("r"))
parser.add_argument('input')
parser.add_argument('output')
args = parser.parse_args()

input_folder = args.input
output_folder = args.output
dictionary = args.dictionary.read()
dictionary_split = dictionary.split()


for file in os.listdir(input_folder):
    if file.endswith(".txt"):
        f = open(input_folder + "/" + file)

        input_file_read = f.read()
        input_lower = input_file_read.lower()
        input_file_split = input_file_read.split()
        input_lower_split = input_lower.split()

        capitalLetter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        capital_counter = ''
        for word in input_file_split:
            for letter in word:
                if letter in capitalLetter:
                    capital_counter += letter + ' '

        punctuation_counter = ''
        dots_list = []
        for word in input_lower_split:
            if word not in dictionary_split:
                for letter in word:
                    if letter in string.punctuation:
                        if letter not in ["@", "#", "."]:
                            input_lower = input_lower.replace(letter, "")
                            punctuation_counter += letter
        for letters in input_lower_split:
            for dots in letters:
                if dots == "." and letters not in dots_list:
                    dots_list.append(letters)
                    input_lower = input_lower.replace(dots, "")

        numbers_list = '1234567890'
        numbers_removed_counter = ''
        for words in input_lower_split:
            for letters in words:
                if letters in numbers_list:
                    input_lower = input_lower.replace(letters, '')
                    numbers_removed_counter += letters

        input_reformed = input_lower.split()
        wrong_words_counter = []
        for item in input_reformed:
            if item not in dictionary_split:
                wrong_words_counter.append(item)
            for word in wrong_words_counter:
                for letter in word:
                    if letter in ["@", "#"]:
                        wrong_words_counter.remove(word)

        output = os.path.join(output_folder, file.replace(".txt", "_p15748aa.txt"))
        output_file = open(output, "w")
        output_file.write(f'''[p15748aa]
Formatting ###################
Number of upper case letters changed: {len(capital_counter.split())}
Number of punctuations removed: {len(punctuation_counter)+len(dots_list)}
Number of numbers removed: {len(numbers_removed_counter)}
Spellchecking ###################
Number of words: {len(input_reformed)}
Number of correct words: {len(input_reformed) - len(wrong_words_counter)}
Number of incorrect words: {len(wrong_words_counter)}
        ''')
        output_file.close()
        print(input_lower)
