import os
import argparse
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("english_txt_file", help="enter english dictionary")
    parser.add_argument("in_file", help="enter input file")
    parser.add_argument("out_file", help="enter output file")
args = parser.parse_args()
input_file = str(args.in_file)
for k in os.listdir(input_file):
    txt_position = k.find('.txt')
    input_file_name = k[0:txt_position]
    file = open(f'{args.in_file}/{k}','r')
    theScore = []
    for line in file:
        line = line.rstrip()
        theScore.append(line)
    text_input = theScore[0]
    length_of_text = len(text_input)
    spellCheck_output = ''
    capital_alphabets = 'ABCDEFGHIJKLMNOPQRSTTUVWXYZ'
    caps_spellcheck = 0
    punctuations_removed = 0
    numbers_removed = 0
    number_of_ellipses = text_input.count('...')
    for r in range(length_of_text):
        if text_input[r] == '.' or text_input[r] == ',' or text_input[r] == ';' or text_input[r] == '?' or text_input[r] == ',' or text_input[r] == ';' or text_input[r] == '!' or text_input[r] == ':' or text_input[r] == '-' or text_input[r] == '(' or text_input[r] == ')' or text_input[r] == '[' or text_input[r] == ']' or text_input[r] == '{' or text_input[r] == '}' or text_input[r] == '"' or text_input[r] == "'" or text_input[r] == '/':
            punctuations_removed += 1
            continue
        elif text_input[r] == '1' or text_input[r] == '2' or text_input[r] == '3' or text_input[r] == '4' or text_input[r] == '5' or text_input[r] == '6' or text_input[r] == '7' or text_input[r] == '8' or text_input[r] == '9' or text_input[r] == '0':
            numbers_removed += 1
        else:
            spellCheck_output = spellCheck_output + text_input[r]

        if text_input[r] in capital_alphabets:
            caps_spellcheck += 1
        spellCheck_output = spellCheck_output.lower()
    punctuations_removed = punctuations_removed - 2*number_of_ellipses
    file = open(args.english_txt_file, "r")
    theWords= []
    for line in file:
        line = line.rstrip()
        theWords.append(line)
    list_of_words = spellCheck_output.split(' ')
    updated_list_of_words = []
    for r in list_of_words:
        if r == '':
            continue
        elif r == ' ':
            continue
        else:
            updated_list_of_words = updated_list_of_words + [r]

    incorrect_words = 0
    for r in updated_list_of_words:
        if r not in theWords:
            incorrect_words += 1
    line = [f'm55182va\nFormatting ###################\nNumber of upper case letters changed: {caps_spellcheck}\nNumber of punctuations removed: {punctuations_removed}\nNumber of numbers removed: {numbers_removed}\nSpellchecking ###################\nNumber of words: {int(len(updated_list_of_words))}\nNumber of correct words: {int(len(updated_list_of_words)) - int(incorrect_words)}\nNumber of incorrect words: {incorrect_words}']
    with open(os.path.join(args.out_file, f'{input_file_name}_m55182va.txt'), 'w') as f:
        f.writelines(line)
