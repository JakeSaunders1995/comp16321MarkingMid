import argparse, os

def dir_path(string):
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)

parser = argparse.ArgumentParser()
parser.add_argument('english_words_file', type=argparse.FileType('r'))
parser.add_argument('input_folder', type=dir_path)
parser.add_argument('output_folder', type=dir_path)
files = parser.parse_args()

english_words_file = files.english_words_file
english_words_list = english_words_file.read().split('\n')

for file in os.listdir(files.input_folder):
    filepath = files.input_folder + '/' + file
    input_file = open(filepath, 'r')
    text = input_file.read()
    input_file.close()

    text_formatted = ''
    upper_count = 0
    num_count = 0
    punct_count = 0
    for i in range(len(text)):
        character = text[i]
        if character.isalpha():
            if character.isupper():
                upper_count += 1
            text_formatted += character.lower()
        elif character == ' ':
            text_formatted += ' '
        elif character.isnumeric():
            num_count += 1
        elif character == '.' and i + 1 != len(text): # If the final character is being indexed, indexing i + 1 would cause it to break, final full stop is accounted for by final elif
            if text[i + 1] != '.': # This will only activate on full stops or third dots of ellipses
                punct_count += 1
        elif character != '\n' and character not in ['#', '@']:
            punct_count += 1

    text_formatted_list = text_formatted.split()
    correct_count = 0
    incorrect_count = 0
    for word in text_formatted_list:
        if word in english_words_list:
            correct_count += 1
        else:
            incorrect_count += 1

    output_list = ['h37701dk', 'Formatting ###################']
    output_list.append('Number of upper case letters changed: ' + str(upper_count))
    output_list.append('Number of punctuations removed: ' + str(punct_count))
    output_list.append('Number of numbers removed: ' + str(num_count))
    output_list.append('Spellchecking ###################')
    output_list.append('Number of words: ' + str(correct_count + incorrect_count))
    output_list.append('Number of correct words: ' + str(correct_count))
    output_list.append('Number of incorrect words: ' + str(incorrect_count))
    output = '\n'.join(output_list)

    filename = os.fsdecode(file)
    filename = filename.replace('.txt', '_h37701dk.txt')
    output_filepath = files.output_folder + '/' + filename
    output_file = open(output_filepath, 'w+')
    output_file.write(output)
    output_file.close()
