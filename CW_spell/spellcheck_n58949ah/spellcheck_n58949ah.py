"""

Adil Hanney 8/11/2021
"""

from os import listdir, path
from argparse import ArgumentParser, Namespace

from typing import List


ALPHABET = "abcdefghijklmnopqrstuvwxyz"
DIGITS = "0123456789"
PUNCTUATION = ".?!,:;(){}[]'\"-‐‒–—―−"  # not including ellipsis in this string


def getArgs() -> (str, str, str):
    argParser: ArgumentParser = ArgumentParser()
    argParser.add_argument("english_words_filepath")
    argParser.add_argument("input_folder")
    argParser.add_argument("output_folder")
    args: Namespace = argParser.parse_args()
    return args.english_words_filepath, args.input_folder, args.output_folder


if __name__ == "__main__":
    english_words_filepath, input_folder, output_folder = getArgs()

    with open(english_words_filepath) as f:
        EnglishWords: List[str] = [line.strip() for line in f.readlines()]

    for filename in listdir(input_folder):
        with open(path.join(input_folder, filename)) as f:
            input_text = f.read()

        # Here we use a list of chars instead of a string, so memory isn't reallocated after each iteration
        sanitised_chars: List[str] = []
        count_uppercase: int = 0
        count_numbers: int = 0
        count_punctuation: int = 0

        for i in range(len(input_text)):
            char = input_text[i]
            if char in ALPHABET:
                sanitised_chars.append(char)
            elif char.lower() in ALPHABET:
                sanitised_chars.append(char.lower())
                count_uppercase += 1
            elif char in DIGITS:
                count_numbers += 1
            elif char in PUNCTUATION:
                count_punctuation += 1
                if i >= 2 and all(input_text[j] == "." for j in (i, i-1, i-2)):  # check for ellipsis
                    count_punctuation -= 2  # only count ellipsis as one punctuation
            elif char == "\n":
                sanitised_chars.append(" ")
            else:
                sanitised_chars.append(char)

        words = ("".join(sanitised_chars)).split(" ")
        count_words: int = len(words)
        count_correct: int = 0
        for word in words:
            if word.strip() == "":
                count_words -= 1
            elif word in EnglishWords:
                count_correct += 1

        output = f"""n58949ah
Formatting ###################
Number of upper case letters changed: {count_uppercase}
Number of punctuations removed: {count_punctuation}
Number of numbers removed: {count_numbers}
Spellchecking ###################
Number of words: {count_words}
Number of correct words: {count_correct}
Number of incorrect words: {count_words - count_correct}"""

        filename = filename.rsplit(".", 1)[0] + "_n58949ah.txt"  # username needs to be in output filename
        with open(path.join(output_folder, filename), "w") as f:
            f.write(output)
