import argparse
import os
import string

username = 'g91274qw'

def parse_args():

    parser = argparse.ArgumentParser()
    parser.add_argument('EnglishWords')
    parser.add_argument('input')
    parser.add_argument('output')
    args = parser.parse_args()
    return args.EnglishWords, args.input, args.output





def load_words(filename: str) -> list:
    with open(filename, 'r', encoding='utf-8') as infp:
        words = []
        for line in infp:
            words.append(line.strip())
        return words


def check_words(filename: str, out_file: str):
    word_lib = load_words('EnglishWords.txt')
    with open(filename) as infp:
        content = infp.read()
        upper_case_count = 0
        punc_count = 0
        num_count = 0
        clean_line = []


        for letter in content:
            if letter in string.digits:
                num_count += 1
            elif letter in string.punctuation:
                punc_count += 1
            elif letter in string.ascii_uppercase:
                upper_case_count += 1
                clean_line.append(chr(ord(letter) + (ord('a') - ord('A'))))
            else:
                clean_line.append(letter)
        words = ''.join(clean_line).split(' ')
        correct_count = 0
        incorrect_count = 0
        for word in words:
            if not word:
                continue
            if word.lower() in word_lib:
                correct_count += 1
            else:
                incorrect_count += 1
        with open(out_file, 'w') as outfp:
            outfp.write(username + '\n')
            outfp.write('Formatting ###################\n')
            outfp.write('Number of upper case words changed: {}\n'.format(upper_case_count))
            outfp.write('Number of punctuations removed: {}\n'.format(punc_count))
            outfp.write('Number of numbers removed: {}\n'.format(num_count))
            outfp.write('Spellchecking ###################\n')
            outfp.write('Number of words: {}\n'.format(correct_count + incorrect_count))
            outfp.write('Number of correct words: {}\n'.format(correct_count))
            outfp.write('Number of incorrect words: {}\n'.format(incorrect_count))


if __name__ == '__main__':

    EnglishWords, input, output = parse_args()
    file_list = os.listdir(input)
    for file in file_list:
        input_file = os.path.join(input, file)
        output_folder_path = os.path.abspath(output)
        if not os.path.exists(output_folder_path):
            os.makedirs(output_folder_path)
        output_file = os.path.join(output_folder_path,
                                   os.path.splitext(file)[0] + '_' + username + '.txt')
        check_words(input_file, output_file)
