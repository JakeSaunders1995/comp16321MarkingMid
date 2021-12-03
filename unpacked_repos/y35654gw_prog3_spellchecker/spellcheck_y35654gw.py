import sys
import os

dictionary_file = sys.argv[1]

f = open(dictionary_file)
english_words = f.read().split("\n")
f.close()

input_folder = sys.argv[2]
output_folder = sys.argv[3]

input_files = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]

for input_file in input_files:
    f = open(os.path.join(input_folder, input_file))
    text = f.read()
    f.close()
    f = open(os.path.join(output_folder, f"{input_file.split('.txt')[0]}_y35654gw.txt"), "w")
    f.write("y35654gw\n")

    f.write("Formatting ###################\n")

    upper_case = 0
    punctuation = 0
    numbers = 0

    i = len(text) - 1
    while (i >= 0):
        if (text[i : i + 3] == "..."):
            punctuation += 1
            text = text[0 : i : ] + text[i + 3 : : ]
        i -= 1

    for i in range(len(text) - 1, -1, -1):
        if (text[i] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            upper_case += 1
            text = text[0 : i : ] + text[i].lower() + text[i + 1 : :]
        elif (text[i] in "0123456789"):
            numbers += 1
            text = text[0 : i : ] + text[i + 1 : :]
        elif (text[i] in "\n"):
            text = text[0 : i : ] + " " + text[i + 1 : :]
        elif (text[i] in ".?!,:;-[]()\{\}'\""):
            punctuation += 1
            text = text[0 : i : ] + text[i + 1 : :]
        elif (text[i] not in "abcdefghijklmnopqrstuvwxyz "):
            text = text[0 : i : ] + " " + text[i + 1 : :]

    f.write(f"Number of upper case letters changed: {upper_case}\n")
    f.write(f"Number of punctuations removed: {punctuation}\n")
    f.write(f"Number of numbers removed: {numbers}\n")

    f.write("Spellchecking ###################\n")

    words_correct = 0
    words_incorrect = 0

    words = text.split(" ")
    words = list(filter(lambda x: x != "", words))
    for word in words:
        if (word in english_words):
            words_correct += 1
        else:
            words_incorrect += 1

    f.write(f"Number of words: {len(words)}\n")
    f.write(f"Number of correct words: {words_correct}\n")
    f.write(f"Number of incorrect words: {words_incorrect}\n")
    
    f.close()