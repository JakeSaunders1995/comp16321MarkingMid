import sys
import os

english = sys.argv[1]
in_dir = sys.argv[2]
out_dir = sys.argv[3]

files = os.listdir(in_dir)

for file in files:
    address = in_dir + "/" + file
    text_file = open(address, "r")
    for text in text_file:
            text = text.rstrip()
    text_file.close()

    uppercase = 0
    for letter in text:
        if letter.isupper():
            uppercase += 1

    text = text.lower()

    current = ''
    words = []
    numbers = 0
    punctuation = 0
    no_words = 0
    no_cwords = 0

    for letter in text:
        if letter.isupper():
            uppercase += 1

        if letter == ' ':
            if current == '':
                continue
            else:
                words.append(current)
                current = ''
            continue

        if not letter.isalpha():
            if letter.isnumeric():
                numbers += 1
            else:
                punctuation += 1
            continue
        else:
            current += letter
    words.append(current)

    for word in words:
        english_words = open(english, "r")
        for line in english_words:
            line = line.rstrip()
            if word == line:
                no_cwords += 1

    no_words = len(words)
    no_iwords = no_words - no_cwords

    name_len = len(file) - 4
    output_add = out_dir + "/" + file[:name_len] + "_g45512id.txt"
    check_file = open(output_add, "w")
    check_file.write("g45512id")
    check_file.write("\nFormatting ###################")
    check_file.write("\nNumber of upper case words changed: " + str(uppercase))
    check_file.write("\nNumber of punctuations removed: " + str(punctuation))
    check_file.write("\nNumber of numbers removed: " + str(numbers))
    check_file.write("\nSpellchecking ###################")
    check_file.write("\nNumber of words: " + str(no_words))
    check_file.write("\nNumber of correct words: " + str(no_cwords))
    check_file.write("\nNumber of incorrect words: " + str(no_iwords))
    check_file.close