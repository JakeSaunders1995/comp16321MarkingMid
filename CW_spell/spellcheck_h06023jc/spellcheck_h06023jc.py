import argparse, os, string

myparser = argparse.ArgumentParser(description='Rugby score calculator')

myparser.add_argument('english_words_path')
myparser.add_argument('input_file_path')
myparser.add_argument('output_file_path')

args = myparser.parse_args()

english_dictionary_path = args.english_words_path
input_path = args.input_file_path
output_path = args.output_file_path

with open(english_dictionary_path, 'r') as f:
        eng_dict = f.read().splitlines()

for file in os.listdir(input_path):
    with open(os.path.join(input_path, file), 'r') as f:
        fileText = f.read()
        filename = os.path.basename(f.name)[:-4]

    formatted_string = ""
    digits_count = 0
    punctuation_count = 0
    upper_count = 0

    for char in fileText:
        if char.isdigit() == True:
            digits_count += 1
        if char in string.punctuation:
            punctuation_count += 1
        if char.isupper() == True:
            upper_count += 1
        if char.isalpha() == True or char.isspace() == True or char == '\n':
            formatted_string += char

    formatted_string = formatted_string.lower()

    words = formatted_string.split()
    word_count = len(words)

    correct_word_count = 0
    incorrect_word_count = 0

    for word in words:
        if word in eng_dict:
            correct_word_count += 1
        else:
            incorrect_word_count += 1

    output_filename = filename + "_h06023jc.txt"

    with open(os.path.join(output_path, output_filename),'w',encoding='utf-8') as f:
        f.write("h06023jc\n")
        f.write("Formatting ###################\n")
        f.write("Number of upper case letters changed: " + str(upper_count) + '\n')
        f.write("Number of punctuations removed: " + str(punctuation_count) + '\n')
        f.write("Number of numbers removed: " + str(digits_count) + '\n')
        f.write("Spellchecking ###################\n")
        f.write("Number of words: " + str(word_count) + '\n')
        f.write("Number of correct words:" + str(correct_word_count) + '\n')
        f.write("Number of incorrect words:" + str(incorrect_word_count) + '\n')
