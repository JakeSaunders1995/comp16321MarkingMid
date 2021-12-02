import os
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("words")
parser.add_argument("input")
parser.add_argument("output")

args = parser.parse_args()

with open(args.words, "r") as f:
    english_words = f.read()
    list_of_english_words = english_words.split("\n")

for file in sorted(os.listdir(args.input)):
    with open(args.input + "/" + file, "r") as f1:
        raw_text = f1.read()
        formatted_text = ""
        upper_case_letters = 0
        punctuations = 0
        numbers = 0
        for char in raw_text:
            if char.isalpha() or char == " ":
                if char.isupper():
                    upper_case_letters += 1
                formatted_text += char.lower()
            elif char.isdigit():
                numbers += 1
            else:
                if char != "\n":
                    punctuations += 1
        list_of_words = formatted_text.split(" ")
        if "" in list_of_words:
            list_of_words = list(filter(lambda x: x != "", list_of_words))
        incorrect_words = 0
        for word in list_of_words:
            if word not in list_of_english_words:
                incorrect_words += 1
        correct_words = len(list_of_words) - incorrect_words        
        total_words = len(list_of_words)

        with open(args.output + "/" + file.replace(".txt", "") + "_j29815fa.txt", "w") as f2:
            f2.write("j29815fa\nFormatting ###################\nNumber of upper case letters changed: " + 
                        upper_case_letters.__str__() + "\nNumber of punctuations removed: " + 
                        punctuations.__str__() + "\nNumber of numbers removed: " + 
                        numbers.__str__() + "\nSpellchecking ###################\nNumber of words: " + 
                        total_words.__str__() + "\nNumber of correct words: " + 
                        correct_words.__str__() + "\nNumber of incorrect words: " + incorrect_words.__str__())
