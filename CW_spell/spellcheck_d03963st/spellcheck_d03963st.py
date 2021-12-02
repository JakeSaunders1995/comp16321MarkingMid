import sys
import re
import os

eng_words = (open(sys.argv[1], "r")).read()

input_directory = sys.argv[2]

for input_file in os.listdir(input_directory):
    with open(os.path.join(input_directory, input_file), "r") as file:
        extract = file.read()

        cap_lst = []
        num_lst = []
        pun_lst = []
        mod_lst = []

        for char in list(extract):
            if char.isupper():
                char = char.lower()
                cap_lst.append(char)

            if char in "1234567890":
                char = ""
                num_lst.append(char)

            punctuation = [".", "?", "!", ":", ";", "-", "—", "(", ")", "{", "}", "[", "]", "'", ",", "\"", "…"]
            if char in punctuation:
                char = ""
                pun_lst.append(char)

            mod_lst.append(char)
            mod_extract = "".join(mod_lst)

        extract_lst = mod_extract.split()
        eng_lst = re.sub("[^\w]", " ", eng_words).split()

        correct_word_lst = []
        incorrect_word_lst = []
        word_lst = []

        for word in extract_lst:
            if word in eng_lst:
                correct_word_lst.append(word)
            else:
                incorrect_word_lst.append(word)
            word_lst.append(word)

        output_directory = sys.argv[3]
        output_file = output_directory + "/" + input_file[0:-4] + "_d03963st.txt"
        with open(output_file, "w+") as f:
            f.write("""d03963st
Formatting ###################
Number of upper case letters changed: {0}
Number of punctuations removed: {1}
Number of numbers removed: {2}
Spellchecking ###################
Number of words: {3}
Number of correct words: {4}
Number of incorrect words: {5}""".format(len(cap_lst), len(pun_lst), len(num_lst), len(word_lst), len(correct_word_lst), len(incorrect_word_lst)))
