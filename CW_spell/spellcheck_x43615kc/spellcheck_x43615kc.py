import argparse
import os
parser = argparse.ArgumentParser()
parser.add_argument("english_words")
parser.add_argument("input_path")
parser.add_argument("output_path")
args = parser.parse_args()

punctuation = ".?!,:;-–(){}[]'\""
numbers = "0123456789"
file_template = '''x43615kc
Formatting ###################
Number of upper case letters changed: {a}
Number of punctuations removed: {b}
Number of numbers removed: {c}
Spellchecking ###################
Number of words: {d}
Number of correct words: {e}
Number of incorrect words: {f}
'''


def spellcheck_file(path):
    with open(path, "r") as file, open(args.english_words) as words_file:
        english_words = words_file.read().split("\n")
        input_doc = file.read()
        chars_lowered, puncs_removed, nums_removed = 0, 0, 0
        words_in_file, correct_words, incorrect_words = 0, 0, 0
        processed = ""
        input_doc = input_doc.replace("...", ".") # cheeky !!!!!!
        for char in input_doc:
            if char in punctuation:
                puncs_removed += 1
            elif char in numbers:
                nums_removed += 1
            elif char.isupper():
                chars_lowered += 1
                processed += char.lower()
            else:
                processed += char
        processed_chunks = [x for x in processed.split()]
        for chunk in processed_chunks:
            if chunk in english_words:
                correct_words += 1
            else:
                incorrect_words += 1
        words_in_file = correct_words + incorrect_words
        return file_template.format(a=chars_lowered, b=puncs_removed, c=nums_removed, d=words_in_file, e=correct_words, f=incorrect_words)


def main():
    for dir, subdirs, files in os.walk(args.input_path):
        for file in files:
            result = spellcheck_file(os.path.join(dir, file))
            output_path = os.path.join(
                args.output_path, os.path.splitext(file)[0] + "_x43615kc.txt")
            if not os.path.exists(args.output_path):
                os.makedirs(args.output_path)
            with open(output_path, "w") as file:
                file.write(result)


if __name__ == '__main__':
    main()
