import sys
import os

path = sys.argv[2]
for file in os.listdir(path):
    file_path = os.path.join(os.getcwd(), path) + "/" + file
    if os.path.isfile(file_path):

        unchecked_file = open(file_path, 'r')
        unchecked_text = unchecked_file.read()
        unchecked_file.close()

        unchecked_array = []
        for character in unchecked_text:
            unchecked_array.append(character)

        #alpha_lower_upper = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "
        numbers = "0123456789"
        punctuation = [".", "?", "!", ",", ":", ";", "/", "-", "—", ")", "(", "{", "}", "[", "]", "'", '"', "..."]

        text_alpha_symbols = ""
        #text_punctuation_numbers = ""
        punctuation_total = 0
        numbers_total = 0

        for character in unchecked_array:
            if character in numbers:
                numbers_total += 1
            elif character in punctuation:
                punctuation_total += 1
            else:
                text_alpha_symbols += character

        #for character in text_punctuation_numbers:
        #    if character in numbers:
        #        numbers_total += 1
        #    else:
        #        punctuation_total += 1

        word_alpha_array = text_alpha_symbols.split(" ")
        lower_word_array = []
        upper_case_total = 0
        for word in word_alpha_array:
            lower_word = word.lower()
            if lower_word != "" and lower_word != "\n":
                lower_word_array.append(lower_word)

            if word != lower_word:
                for i in range(len(word)):
                    if word[i] != lower_word[i]:
                        upper_case_total += 1

        english_words_path = os.path.join(os.getcwd(), sys.argv[1])
        english_words_file = open(english_words_path, 'r')
        english_words = english_words_file.read()
        english_words = english_words.split("\n")
        english_words_file.close()

        unchecked_formatted_word_array = text_alpha_symbols.split(" ")
        word_total = len(lower_word_array)
        correct_word_total = 0
        incorrect_word_total = 0
        for word in lower_word_array:
            if word not in english_words:
                print(word)
                incorrect_word_total += 1
            else:
                correct_word_total += 1

        spellCheck_output = (f"""f92301jb
Formatting ###################
Number of upper case letters changed: {str(upper_case_total)}
Number of punctuations removed: {str(punctuation_total)}
Number of numbers removed: {str(numbers_total)}
Spellchecking ###################
Number of words: {str(word_total)}
Number of correct words: {str(correct_word_total)}
Number of incorrect words: {str(incorrect_word_total)}""")



        output_file_name = os.path.join(os.getcwd(), sys.argv[3]) + "/" + file[:-4] + "_f92301jb.txt"
        output_file = open(output_file_name, "w")
        output_file.write(spellCheck_output)
        output_file.close()
