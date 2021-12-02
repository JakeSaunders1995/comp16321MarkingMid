import os
import argparse
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('English_dic', help = 'enter english dic')
    parser.add_argument("put_in_file", help="enter a file")
    parser.add_argument("put_out_file", help="enter a file")
args = parser.parse_args()
input_file = args.put_in_file
for j in os.listdir(input_file):
    text_pos = j.find('.txt')
    input_file_heading = j[0:text_pos]
    file = open(f'{args.put_in_file}/{j}', 'r')
    transfer =[]
    for line in file:
        line=line.rstrip()
        transfer.append(line)
    # First Part of the question
    text=transfer[0]
    punctuations = ['?', '!', ',', "'", ';', ':', '-', '(', ')', '[', ']', '{', '}', '"', "'", '.']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    number_count = 0
    punctuations_count = 0
    capital_letter_count = 0
    num_of_ellipsis = text.count('...')
    for r in text:
        if r in punctuations:
            punctuations_count += 1
        elif r in numbers:
            number_count += 1
        elif r in capital_letters:
            capital_letter_count += 1
    punctuations_count = punctuations_count - (2*num_of_ellipsis)


    # Second part of the question
    spell_check = ''
    z = 0
    for r in text:
        if r == '...':
            text=text.replace(r, '')
        elif r in punctuations:
            text=text.replace(r,'')
        elif r in numbers:
            text=text.replace(r,'')
        else:
            spell_check += text[z]
            z += 1
        spell_check=spell_check.lower()


    # For removing Spaces from the edited program
    for r in spell_check:
        spell_check=spell_check.replace('  ', ' ')
    for r in spell_check:
        spell_check=spell_check.replace('   ', ' ')
    for r in spell_check:
        spell_check=spell_check.replace('    ', ' ')
    if spell_check[-1] == ' ':
        new_spell_check = spell_check[:-1]
    else:
        new_spell_check = spell_check


    # Number of Words in File
    new_spell_check_words = new_spell_check.split(' ')
    len_new_spell_check_words = len(new_spell_check_words)


    # Number of Correct Words
    new_file = open(args.English_dic, 'r')
    words_new_file = []
    for line in new_file:
        line = line.rstrip()
        words_new_file.append(line)

    correct_word_count = 0
    for words in new_spell_check_words:
        if words in words_new_file:
            correct_word_count += 1


    # Number of Incorrect Words
    incorrect_word_count = len_new_spell_check_words - correct_word_count


    # print(capital_letter_count)
    # print(punctuations_count)
    # print(number_count)
    # print(len_new_spell_check_words)
    # print(correct_word_count)
    # print(incorrect_word_count)
    l = (f'b26193dm\nFormatting ###################\nNumber of upper case letters changed: {capital_letter_count}\nNumber of punctuations removed: {punctuations_count}\nNumber of numbers removed: {number_count}\nSpellchecking ###################\nNumber of words: {len_new_spell_check_words}\nNumber of correct words: {correct_word_count}\nNumber of incorrect words: {incorrect_word_count}')
    line = [l]
    with open(os.path.join(args.put_out_file, f'{input_file_heading}_b26193dm.txt'), 'w') as f:
        f.writelines(line)    