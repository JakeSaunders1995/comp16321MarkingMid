import sys
import string
import os
from collections import Counter

INPUT_FOLDER = sys.argv[2]
OUTPUT_FOLDER = sys.argv[3]
DIRECTORY = os.listdir(INPUT_FOLDER)

print (DIRECTORY)

#----------------Read text file ---------------
f = open(sys.argv[1],"r")
words = f.read()
f.close()
def calculate(text):
    #--------------Initializing of variables-------------------
    username = "p29365al"
    num_of_words = 0
    num_numbers = 0
    num_punctuations = 0
    num_upper_case_words = 0
    num_of_incorrect_words = 0
    num_of_correct_words = 0
    punc_occurrences = 0
    num_occurrences = 0
    upper_case_occurrences = 0
    #---------------End of intializing of variables-----------------

    #-------------------Start of Formatting Section-------------------------------------------
    length = len(text)
    count = 0
    num_upper_case_words = 0
    while count < (length) :
        for i in text[count]:
            if i in string.ascii_uppercase:
                upper_case_occurrences = text.count(text[count]) + upper_case_occurrences
                num_upper_case_words = num_upper_case_words + 1
                text = text.replace(text[count],text[count].lower())
            if i in string.punctuation:
                punc_occurrences = text.count(text[count]) + punc_occurrences
                text = text.replace(text[count]," ")
                num_punctuations += 1
        if text[count].isdigit():
            num_occurrences = text.count(text[count]) + num_occurrences
            text = text.replace(text[count]," ")
            num_numbers = num_numbers + 1
        count = count + 1
        remove_spaces = " ".join(text.split())
    word = text.split()
    #-------------------End of Formatting Section---------------------------------------------

    #----------Start of Spellchecking Section----------
    for x in range (len(word)):
        if word[x] not in words.split():
            num_of_incorrect_words = num_of_incorrect_words + 1
        if word[x] in words.split():
            num_of_correct_words = num_of_correct_words + 1
    #----------End of Spellchecking Section------------
    return (username, upper_case_occurrences, punc_occurrences, num_occurrences, num_of_incorrect_words, num_of_correct_words)


if __name__ == '__main__':
    for i in range(len(DIRECTORY)):
        t = open(INPUT_FOLDER + "/" + DIRECTORY[i])
        text = t.readline()
        t.close()
        username, upper_case_occurrences, punc_occurrences, num_occurrences, num_of_incorrect_words, num_of_correct_words = calculate(text)
        output_file = "test_file"+str(i+1)+"_"+(username)+".txt"
        output_file = OUTPUT_FOLDER + "/" + output_file
        with open (output_file, "a") as file:
            file.write (username + "\n")
            file.write ("Formating ################### \n")
            file.write ("Number of upper case words changed: " + str(upper_case_occurrences) + '\n')
            file.write ("Number of punctuations removed: " + str(punc_occurrences) + '\n')
            file.write ("Number of numbers removed: " + str(num_occurrences) + '\n')
            file.write ("Spellchecking ################### \n")
            file.write ("Number of words: " + str(num_of_correct_words + num_of_incorrect_words) + '\n')
            file.write ("Number of correct words: " + str(num_of_correct_words) + '\n')
            file.write ("Number of incorrect words: " + str(num_of_incorrect_words) + '\n')