import argparse, os
# get folder and file names
parser = argparse.ArgumentParser()
parser.add_argument('english_words_file')
parser.add_argument('input_folder')
parser.add_argument('output_folder')
args = parser.parse_args()

# get English words
f = open(args.english_words_file)
all_words = [i.strip() for i in f.readlines()]
f.close()

file_list = [i for i in os.listdir(args.input_folder) if os.path.isfile(f'{args.input_folder}/{i}')]

for file_name in file_list:
    # read input file
    f = open(f'{args.input_folder}/{file_name}')
    input_str = f.read()
    f.close()
    # variable setup
    proc_str = ""
    output = []
    CASE_CHANGE = 0
    PUNCTUATION_REMOVAL = 0
    NUMBER_REMOVAL = 0
    output.append('q17766yl')
    output.append('Formatting ###################')
    while input_str:
        char = input_str[0:1]
        if ord(char) <= 122 and ord(char) >= 97: # lower case english letter
            proc_str += char
            input_str = input_str[1:]
        elif ord(char) <= 90 and ord(char) >= 65: # upper case english letter
            proc_str += char.lower()
            CASE_CHANGE += 1
            input_str = input_str[1:]
        elif char.isdigit(): # number
            NUMBER_REMOVAL += 1
            input_str = input_str[1:]
        elif char in ' \n': # pass through as space
            proc_str += ' '
            input_str = input_str[1:]
        elif char in '?!,:;-–—[](){}\'"':
            PUNCTUATION_REMOVAL += 1
            input_str = input_str[1:]
        elif char == '.':
            if input_str.startswith('...'):
                PUNCTUATION_REMOVAL += 1
                input_str = input_str[3:]
            elif input_str.startswith('. . .'):
                PUNCTUATION_REMOVAL += 1
                input_str = input_str[5:]
            else:
                PUNCTUATION_REMOVAL += 1
                input_str = input_str[1:]
        else: # skip
            input_str = input_str[1:]
    output.append(f'Number of upper case letters changed: {CASE_CHANGE}')
    output.append(f'Number of punctuations removed: {PUNCTUATION_REMOVAL}')
    output.append(f'Number of numbers removed: {NUMBER_REMOVAL}')
    # spellchecking
    output.append('Spellchecking ###################')
    word_list = [i for i in proc_str.split(' ') if i]
    output.append(f'Number of words: {len(word_list)}')
    WORD_INCORRECT = 0
    WORD_CORRECT = 0
    for word in word_list:
        if word in all_words:
            WORD_CORRECT += 1
        else:
            WORD_INCORRECT += 1
    output.append(f'Number of correct words: {WORD_CORRECT}')
    output.append(f'Number of incorrect words: {WORD_INCORRECT}')
    # write output file
    if '.' in file_name:
        file_name_part = file_name.split('.')
        file_extension = file_name_part.pop(-1)
        new_file_name = f'{".".join(file_name_part)}_q17766yl.{file_extension}'
    else:
        new_file_name = f'{file_name}_q17766yl'
    f = open(f'{args.output_folder}/{new_file_name}', 'w')
    f.write("\n".join(output))
    f.write('\n')
    f.close()