import argparse
import glob

my_parser = argparse.ArgumentParser()

my_parser.add_argument('words_file_path', type = str)
my_parser.add_argument('input', type = str)
my_parser.add_argument('output', type = str)

args = my_parser.parse_args()

text = ''

for input_file_path in glob.glob(args.input + '/*.txt'):
    with open(input_file_path, "r", encoding='utf-8') as f:
        lines = f.readlines()
        text = ' '.join(line.rstrip() for line in lines)

    number_of_uppercase_letters, number_of_punctuations, number_of_numbers = 0, 0, 0

    formatted_text = ''

    punctuations = ['...', '–', '—', '-', '.', '?', '!', ',', ':', ';', '{', '}', '[', ']', '(', ')', '\'', '"']

    for punctuation in punctuations:
        number_of_punctuations += text.count(punctuation)
        text = text.replace(punctuation, '')

    for i in range(len(text)):
        if (text[i] >= 'A') and (text[i] <= 'Z'):
            formatted_text += chr(ord(text[i]) + 32)
            number_of_uppercase_letters += 1
        elif (text[i] >= '0') and (text[i] <= '9'):
            number_of_numbers += 1
        elif (text[i] >= 'a' and text[i] <= 'z') or text[i] == ' ':
            formatted_text += text[i]

    list_of_words = formatted_text.split()

    number_of_correct_words = 0

    with open(args.words_file_path, 'r') as f:
        lines = f.readlines()
        lines = [item.rstrip() for item in lines]
        for word in list_of_words:
            if word in lines:
                number_of_correct_words += 1

    input_file = input_file_path.split('/')[-1]

    with open(f'{args.output}/{input_file[0:-4]}_f05815rb.txt', 'w') as g:
        g.write('f05815rb\n')
        g.write('Formatting ###################\n')
        g.write(f'Number of upper case letters changed: {number_of_uppercase_letters}\n')
        g.write(f'Number of punctuations removed: {number_of_punctuations}\n')
        g.write(f'Number of numbers removed: {number_of_numbers}\n')
        g.write('Spellchecking ###################\n')
        g.write(f'Number of words: {len(list_of_words)}\n')
        g.write(f'Number of correct words: {number_of_correct_words}\n')
        g.write(f'Number of incorrect words: {len(list_of_words) - number_of_correct_words}')
