import argparse
import os
import re
from pathlib import Path
import string

def remove_punc(word):
    p_removed = 0
    for c in word:
        if (c in string.punctuation):
            print('removing punc',c)
            p_removed +=1
    return p_removed

# Get files
parser = argparse.ArgumentParser(description = "Take the scores of both teams, and store the total scores in another file")

parser.add_argument('english_words', help=".txt file with english words")
parser.add_argument('input_folder', help="The input folder")
parser.add_argument('output_folder', help="The output folder")
files = parser.parse_args()

# Check files exist
englishwords_exist,input_exists, output_exists = os.path.exists(files.english_words),os.path.exists(files.input_folder), os.path.exists(files.output_folder)

if input_exists and output_exists and englishwords_exist:
    pass
else:
    print("Incorrect file paths were entered")
    os._exit(1)

if len(os.listdir(files.input_folder)) == 0:
    print('No files in input folder')
    os._exit(1)

# Sort through english file and put words into an array, lowercased
english_file = open(str(files.english_words),"r")
e_words_array = []
for line in english_file:
    clean_l = line.rstrip()
    e_words_array.append(clean_l.lower())

# Loop through files in the input folder
for filename in os.listdir(files.input_folder):
    if filename.endswith('.txt'):

        # Open the current txt file
        input_filepath = os.path.join(files.input_folder, filename)
        input_file = open(str(input_filepath), "r")

        output_filename = str(Path(filename).stem + "_k77872uk.txt")

        # Make the output file
        output_filepath = os.path.join(files.output_folder, output_filename)
        output_file = open(str(output_filepath), "w")

        uppercase_num = 0
        punc_removed = 0
        numbers_removed = 0
        num_of_words = 0
        num_correct_words = 0
        num_incorrect_words = 0

        # Loop through it
        for line in input_file:
            clean_line = line.rstrip()

            # Put the words on the current line into an array
            words_list = re.split('[ ]',clean_line)

            #Sort through the array of words and check if they're right or not
            correct_words = []
            incorrect_words = []

            for word in words_list:
                lower_word = word.lower()
                num_of_words += 1

                # Check if word has any capital letters
                if (re.search('[A-Z]', word)) :
                    uppercase_num += 1

                # Check if the word has correct spelling
                if lower_word in e_words_array:
                    #add to correct list
                    num_correct_words += 1
                    correct_words.append(lower_word)
                else:
                    # This means there is puctuation in the word, or it has no letters
                    # Check if the word has any letters
                    if (re.search('[a-z]', lower_word)) :
                        punc_removed += remove_punc(lower_word)

                        # Remove punctuation from word
                        word_no_punctuation = lower_word.translate(lower_word.maketrans('', '', string.punctuation))

                        # Check if word without punctuation is correct
                        if word_no_punctuation in e_words_array:
                            num_correct_words += 1
                            correct_words.append(lower_word)
                        # Otherwise put it in the list of incorrect words
                        else:
                            num_incorrect_words += 1
                            incorrect_words.append(lower_word)
                    else:
                        num_of_words -= 1

                        # If it has numbers
                        if (re.search('-?\d+', lower_word)):
                            num_of_num = sum(c.isdigit() for c in lower_word)
                            numbers_removed += num_of_num

                        # If it only has punctuation
                        if any(p in lower_word for p in string.punctuation):
                            punc_removed += remove_punc(lower_word)

        # Write to the output file, then close the files
        output_file.write("k77872uk\nFormatting ###################\nNumber of upper case letters changed: {}\nNumber of punctuations removed: {}\nNumber of numbers removed: {}\nSpellchecking ###################\nNumber of words: {}\nNumber of correct words: {}\nNumber of incorrect words: {}".format(uppercase_num,punc_removed,numbers_removed,num_of_words,num_correct_words,num_incorrect_words))
        input_file.close()
        output_file.close()
