import sys
import os
import re

english_words_path = sys.argv[1][2:]
input_folder = sys.argv[2][2:]
output_folder = sys.argv[3][2:]
folder_list = os.listdir(input_folder)
folder_list.sort()
output_txt_files = []




for i in range(len(folder_list)):
    output_txt_files.append("test_file" + str(i+1) + "_s50548ma.txt")

with open(english_words_path,"r") as english_words_file:
    word_db = english_words_file.readlines()

for i in range(len(folder_list)):
    upper_case = 0
    numbers = 0
    punctuation = 0
    words = 0
    correct = 0
    incorrect = 0
    with open(input_folder+"/"+folder_list[i],"r") as input_file:
        db = input_file.readline()

    for letter in db:
        if letter == " ":
            words += 1
        elif letter.isalpha():
            if letter.isupper():
                upper_case +=1
            letter = letter.lower()
        elif letter.isdigit():
            numbers += 1
        else:
            punctuation += 1
        
    db = re.sub(r'[^\w\s]','',db)
    db = re.sub(r'[0-9]','',db)
    db = re.sub(r'\s{2,}',' ',db)
    db = db.lower()
    db = db.split()
    for word in db:
        for dic in word_db:
            if word == dic:
                correct += 1
            else:
                incorrect +=1
    with open(output_folder + "/" + output_txt_files[i],"w") as output_file:
        output_file.writelines("s50548ma" + "\n")
        output_file.writelines("Formatting #################" + "\n")
        output_file.writelines("NUmber of upper case letters changed: "+ str(upper_case) +"\n")
        output_file.writelines("Number of punctuation removed: "+ str(punctuation) + "\n")
        output_file.writelines("Number of numbers removed: " + str(numbers) + "\n")
        output_file.writelines("Spellchecking #################" + "\n")
        output_file.writelines("Number of words:" + str(len(db)) +"\n")
        output_file.writelines("Number of correct words" +str(correct)+ "\n")
        output_file.writelines("Number of incorrect words" + str(incorrect) + "\n")

                
    print(db)
    print()