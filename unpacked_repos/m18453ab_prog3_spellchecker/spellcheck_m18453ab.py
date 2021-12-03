import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("words_file_path")
parser.add_argument("input_folder_path")
parser.add_argument("output_folder_path")

def get_stats(text, english_words):
    stats = ['m18453ab']

    # formatting
    stats.append('Formatting ###################')
    punctuation_ct = 0
    upper_letters_ct = 0
    numbers_ct = 0
    punctuation = ".?!,:;-–—[]{}()\'\""

    text = list(text)
    for i in range(len(text)):
        # ellipsis
        if i < len(text) - 2:
            if text[i] == '.' and text[i + 1] == '.' and text[i + 2] == '.':
                text[i] = ''
                text[i + 1] = ''
                text[i + 2] = ''
                punctuation_ct += 1

        if len(text[i]) == 0:
            continue

        if text[i].isupper():
            upper_letters_ct += 1
            text[i] = text[i].lower()

        if text[i].isalpha():
            continue

        if text[i] in punctuation:
            punctuation_ct += 1
            text[i] = ''
        elif text[i].isdigit():
            numbers_ct += 1
            text[i] = ''
        else:
            text[i] = ' '

    stats.append("Number of upper case letters changed: " + str(upper_letters_ct))
    stats.append("Number of punctuations removed: " + str(punctuation_ct))
    stats.append("Number of numbers removed: " + str(numbers_ct))

    # spellchecking
    stats.append('Spellchecking ###################')

    text = "".join(text)
    text = text.split(" ")
    text = [word for word in text if len(word)]
    words_ct = len(text)
    bad_words_ct = 0

    for word in text:
        bad_words_ct += (word not in english_words)

    stats.append("Number of words: " + str(words_ct))
    stats.append("Number of correct words: " + str(words_ct - bad_words_ct))
    stats.append("Number of incorrect words: " + str(bad_words_ct))

    return stats


def main():
    args = parser.parse_args()

    for file_name in os.listdir(args.input_folder_path):
        if file_name.endswith('.txt'):
            # read file contents
            input_file_path = os.path.join(args.input_folder_path, file_name)
            with open(input_file_path, encoding="utf-8") as f:
                text = f.read()

            # read english words
            with open(args.words_file_path) as f:
                english_words = f.read().split('\n')

            # solve problem
            stats = get_stats(text, english_words)

            # write results
            output_file_name = file_name[:-4] + '_m18453ab.txt'
            output_file_path = os.path.join(args.output_folder_path, output_file_name)
            with open(output_file_path, 'w') as f:
                f.write('\n'.join(stats))


if __name__ == "__main__":
    main()