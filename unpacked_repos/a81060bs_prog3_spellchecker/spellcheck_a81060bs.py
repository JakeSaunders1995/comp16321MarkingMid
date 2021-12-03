import sys
import string
import re
# print ('Number of arguments:', len(sys.argv), 'arguments.')
# print('Argument List:', str(sys.argv))

# NOTE: The code below opens files and assigns those files to variables.
d = open(sys.argv[1], 'r')
dictionary = d.read() #dictionary = EnglishWords.txt

in_fl = open(sys.argv[2], 'r')
input_file =in_fl.read() # Text input


number_of_uppercase_words_tranformed = int(0)
number_of_punctuation_removed = int(0)
number_of_numbers_removed = 0
number_of_correct_words = 0
number_of_incorrect_words = 0


# NOTE: Code belowe transformes uppercase letters to lowercase.
for w in input_file:
    if w.isupper():
        number_of_uppercase_words_tranformed +=1

input_file_transformed = input_file.lower()



# NOTE: lists all possible punctuations for a string
punctuations =['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', '...']



# NOTE: removes any PUNCTUATION from input_file_transformed AND ellipses
for x in input_file_transformed:
    if x in punctuations:
        input_file_transformed = input_file_transformed.replace(x, '')
        number_of_punctuation_removed +=1


# NOTE: removes any NUMBERS:
digits = string.digits
for y in input_file_transformed:
    if y in digits:
        number_of_numbers_removed +=1
        input_file_transformed = input_file_transformed.replace(y,'')

# print(input_file_transformed)

words = input_file_transformed.split()
# print(words)
for z in words:
    if z in dictionary:
        number_of_correct_words +=1
    else:
        number_of_incorrect_words +=1




# print(input_file_transformed)

ot_fl = open(sys.argv[3], 'w')
ot_fl.write('''a81060bs''')
ot_fl.write('''
Formatting ###################
Number of upper case letters changed: ''' + str(number_of_uppercase_words_tranformed))


ot_fl.write(
''' \nNumber of punctuation’s removed: ''' +str(number_of_punctuation_removed)
)
ot_fl.write('''\nNumber of numbers removed: ''' + str(number_of_numbers_removed))

ot_fl.write('''\n Spellchecking ###################''')
ot_fl.write('''\nNumber of words: ''' +str(len(input_file_transformed.split())))

ot_fl.write('''\nNumber of correct words: ''' + str(number_of_correct_words))

ot_fl.write('''\nNumber of incorrect words: ''' + str(number_of_incorrect_words))
