import os
import sys
import string


#assign input
dict = sys.argv[1]
dict = open(dict, "r")
the_dict = dict.read()
english_list = the_dict.split()
input_folder = sys.argv[2]
output_folder = sys.argv[3]

if not os.path.isdir(output_folder):
    os.mkdir(output_folder)

for file in os.listdir(input_folder):
    with open(os.path.join(input_folder, file), "r") as inputf:
        text = inputf.read()

    input_list = ""
    input_list = text.split()
    count5 = 0
    upperCase = 0
    count_nums_removed = 0
    count_punc_removed = 0
    num_elipsis = 0
    charechters = [ch for ch in text]
    input_without_numbers = ""


    # number of elipsis
    for word in input_list:
        if word == "...":
            num_elipsis +=1

    # remove numebrs(CORRECT DONT TOUCH IT)
    for letter in charechters:
         if (letter == "1" or letter == "2" or letter == "3" or letter == "4" or letter == "5" or letter == "6"
                 or letter == "7" or letter == "8" or letter == "9" or letter == "0"):
             letter = ""
             count_nums_removed += 1
         else:
             input_without_numbers += letter
    count_nums_removed = len(text)-len(input_without_numbers)


    # removing punctuation (CORRECT)
    punct = '''(-{!;):'"/\,~—}.*#?@[]$%^&<>_'''
    input_wo_pun = ""
    length_without_pun = 0
    for char in input_without_numbers:
        if char not in punct:
            input_wo_pun = input_wo_pun + char
            length_without_pun +=1
        else:
            count_punc_removed +=1

    count_punc_removed = count_punc_removed - (num_elipsis * 3)
    num_of_words = len(input_wo_pun.split())


    # count upper case(CORRECT)
    for term in input_without_numbers:
        if (term.isupper()):
            upperCase +=1



    # for counting correct and inccorect (CORRECT)
    correct = 0
    incorrect = 0
    input_wo_pun = input_wo_pun.lower()
    list_words = input_wo_pun.split()
    for word in list_words:
        if word not in english_list:
            incorrect +=1
        else:
            correct+=1



    with open(os.path.join(output_folder, os.path.basename(file)[:-4] + "_s58860aa.txt"), "w")as output_file:
        output_file.write(str("s58860aa\n") + str("Formatting ###################\n") + str("Number of upper case letters changed: ") + str(upperCase)
                          + str("\nNumber of punctuations removed: ") + str(count_punc_removed) +str("\nNumber of numbers removed: ")
                          + str(count_nums_removed) + str("\nSpellchecking ###################\n")
                          + str("Number of words: ") + str(num_of_words) + str("\nNumber of correct words: ") + str(correct)
                          + str("\nNumber of incorrect words: ") + str(incorrect))