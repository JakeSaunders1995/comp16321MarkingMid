import os
import sys
import string

with open(sys.argv[1], "r") as eng_words:
    word_list = [line.rstrip() for line in eng_words]
input_path = sys.argv[2]
output_path = sys.argv[3]

for file_name in os.listdir(input_path):
    with open(input_path + "/{}".format(file_name), "r") as f:
        word_file = f.read().rstrip()
        f.close()

        correct_words = 0
        incorrect_words = 0

        punc = ["—", '!', ",", ":", ";", "/", ".", "-", "?", "...", "(", ")", "{", "}", "[", "]", '"', "'", "_", "…"]
        
        # punctuation removed and counted
        punc_count = 0
        no_punc = ""
        for char in word_file:
            if char in punc:
                punc_count += 1
                continue
            else:
                no_punc += char

        for a in range(len(word_file)):
                if word_file[a : a + 3] == "...":
                    punc_count += 1
                    punc_count -= 3
        
        # num of numbers 
        num_count = 0
        for num in word_file:
            if num.isdigit():
                num_count += 1

        # number of capital letters
        capital_num = sum(1 for capitals in word_file if capitals.isupper())

        # text without punctuation and numbers
        no_num_punc = ''.join(filter(lambda nums: not nums.isdigit(), no_punc))

        text_string = no_num_punc.split(" ")

        total_words = len(text_string)
        for i in range(len(text_string)):
            if text_string[i] == '' or text_string[i] == "@" or text_string[i] == "#":
                total_words -= 1
            else:
                continue

        lower_new_string = no_num_punc.lower()
        new_string = lower_new_string.split()

        for x in range(len(new_string)):
            if new_string[x] in word_list:
                correct_words += 1
            elif new_string[x] == "@" or new_string[x] == "#":
                continue
            else:
                incorrect_words += 1

        final_info = "u95206ma\nFormatting ###################\nNumber of upper case letters changed: " + str(capital_num) + "\nNumber of punctuations removed: " + str(punc_count) + "\nNumber of numbers removed: " + str(num_count) + "\nSpellchecking ###################\nNumber of words: " + str(total_words) + "\nNumber of correct words: " + str(correct_words) + "\nNumber of incorrect words: " + str(incorrect_words)

        file_name = os.path.basename(input_path + "/{}".format(file_name))
            
        new_file_name = os.path.join(output_path, file_name.split(".")[0] + "_u95206ma.txt")
        output_info = open(new_file_name, "w+")
        output_info.write(final_info)
        output_info.close()
    