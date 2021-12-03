#This program will take a file EnglishWords.txt as one input for veryfying whether the words in another input file is correct.
#This program will also remove the punctuation marks, convert upper case to lower case etc,.
#This program will consider the ellipsis (...) as a punctuation mark
import os
import argparse

def formatter(formatter_input_line, english_words):
    #print("The formatter input line: " + formatter_input_line)
    number_of_upper = 0
    number_of_punctuations = 0
    number_of_numbers = 0
    formatter_output = ""
    spell_check_output = ""

    for numbers in formatter_input_line:
        if numbers.isdigit():
            formatter_input_line = formatter_input_line.replace(numbers, "")
            number_of_numbers = number_of_numbers + 1
    print("The number of numbers is: " + str(number_of_numbers) + "\n")


    #only_alpha = ''.join([i for i in formatter_input_line if not i.isdigit()])
    #print("Only alphabets and no numbers: " + only_alpha)
    
    print("Only alphabets and no numbers: " + formatter_input_line + "\n")
    
    #Removing punctuation by traversing the string's element one by one.
    #If a punctuation is found, it will be removed and the space where the
    #punctuation is found will be deleted. 
    #Deleting ellipsis
    number_of_punctuations = formatter_input_line.count("...")
    formatter_input_line.replace("...", "")
    punctuation_str = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    str_without_punc = ""
    for punctuation_marks_upper in formatter_input_line:
        #print("punctuation_marks: " + punctuation_marks)
        if punctuation_marks_upper in punctuation_str:
            formatter_input_line  = formatter_input_line.replace(punctuation_marks_upper, "")
            number_of_punctuations = number_of_punctuations + 1

        if punctuation_marks_upper.isupper():
            formatter_input_line  = formatter_input_line.replace(punctuation_marks_upper, punctuation_marks_upper.lower())
            number_of_upper = number_of_upper + 1

    print("The Number of punctuations removed: " + str(number_of_punctuations) + "\n")

    print("The Number of upper case to lower case: " + str(number_of_upper) + "\n")

    formatter_output = str(number_of_upper) + " " + str(number_of_punctuations) + " " + str(number_of_numbers) 

    spell_check_output = spellchecker(formatter_input_line, english_words)

    #formatter_output = formatter_output 

    return [formatter_output, spell_check_output]


def spellchecker(spell_checker_line, english_words):
    spell_checker_lst = spell_checker_line.split()
    number_of_words = 0
    number_of_correct_words = 0
    number_of_incorrect_words = 0
    spell_checker_output = ""
    number_of_words = len(spell_checker_lst)
    print("Number of words: " + str(number_of_words))

    for lst_ele in spell_checker_lst:
        if lst_ele in english_words:
            number_of_correct_words = number_of_correct_words + 1

    number_of_incorrect_words = number_of_words - number_of_correct_words
 
    print("Number of correct words and incorrect words: " + str(number_of_correct_words) + ":" + str(number_of_incorrect_words))

    spell_checker_output = spell_checker_output + str(number_of_words) + " " + str(number_of_correct_words) + " " + str(number_of_incorrect_words)
    return spell_checker_output












#Processing command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("EnglishWordsFilePath", type = str)
parser.add_argument("input_file_path", type = str)
parser.add_argument("output_file_path", type = str)
args = parser.parse_args()
print(args.EnglishWordsFilePath)
print(args.input_file_path)
print(args.output_file_path)
input_file_arr = os.listdir(args.input_file_path)
print(input_file_arr)

file_handle = open(args.EnglishWordsFilePath, "r")
english_words = file_handle.read()
file_handle.close()
#print("English Words: " + english_words + "\n")

#Number of files in the input folder
number_of_files = len(input_file_arr)
formatter_output_line_final = ""
spell_checker_output_final = ""
count = 0

while count < number_of_files:
    #file_handle = open((args.output_file_path + "/" +"test_file" + str(count + 1) +  "_g78896na.txt"), "w")
    file_handle = open((args.output_file_path + "/" + (str(input_file_arr[count])).replace(".txt", "") + "_g78896na.txt"), "w")
    file_handle.write("g78896na\n")
    file_handle.close()
    count = count + 1

count = 0

while count < number_of_files:
    file_handle = open((args.input_file_path + "/" + input_file_arr[count]), "r")
    input_line = file_handle.read()
    file_handle.close()

    print("Input Line from File: " + args.input_file_path + "/" + input_file_arr[count] + ": " + input_line + "\n")

    formatter_output_line = formatter(input_line, english_words)
    #print("From main part: " + args.input_file_path + "/" + input_file_arr[count] + ": " + str(formatter_output_line) + "\n")

    print("From main part: " + args.input_file_path + "/" + input_file_arr[count] + ": ")
    print(formatter_output_line)
    print("\n")

    print(formatter_output_line[0])
    formatter_output_line_arr1 = formatter_output_line[0].split()
    print(formatter_output_line_arr1)
    formatter_output_line_arr2 = formatter_output_line[1].split()
    print(formatter_output_line_arr2)


    #formatter_output_line_final = formatter_output_line_final + formatter_output_line + " "

    #file_handle = open((args.output_file_path + "/" + "test_file" + str(count + 1)  + "_g78896na.txt"), "a")
    file_handle = open((args.output_file_path + "/" + str(input_file_arr[count]).replace(".txt", "")  + "_g78896na.txt"), "a")
    #file_handle.write(str(formatter_output_line))
    file_handle.write("Formatting ###################\n")
    file_handle.write("Number of upper case letters changed: " + formatter_output_line_arr1[0] + "\n")
    file_handle.write("Number of punctuations removed: " + formatter_output_line_arr1[1] + "\n")
    file_handle.write("Number of numbers removed: " + formatter_output_line_arr1[2] + "\n")
    file_handle.write("Spellchecking ###################\n")
    file_handle.write("Number of words: " + formatter_output_line_arr2[0] + "\n")
    file_handle.write("Number of correct words: " + formatter_output_line_arr2[1] + "\n")
    file_handle.write("Number of incorrect words: " + formatter_output_line_arr2[2] + "\n")
    file_handle.close()
    count = count + 1

output_file_arr = os.listdir(args.output_file_path)
print("The list of files in the output file path is: ")
print(output_file_arr)
print(output_file_arr[0])
output_file_arr[0] = output_file_arr[0].replace(".txt", "")
print(output_file_arr[0])
print("The formatter output line final: " + formatter_output_line_final)



