#Spellchecker
import argparse
import os
import string
import re

parser=argparse.ArgumentParser(description='English words and Input File and output file')
parser.add_argument("english_words")
parser.add_argument("source_file")
parser.add_argument("target_file")
args=parser.parse_args()

cwd=os.getcwd()
print(cwd)

english_words=args.english_words
print(english_words)
english_words=open(english_words,"r")
english_words=english_words.read()
english_words=english_words.split("\n")


input_file=args.source_file
print(input_file)

output_file=args.target_file
print(output_file)



dirs=os.listdir(input_file)
for file in dirs:
    print(file)
    upperCase=0
    punctuation=0
    numbers=0
    total_words=0
    correct_words=0
    incorrect_words=0
    new_text=""

    os.chdir(str(cwd)+"/"+str(input_file))
    text=open(file,"r")
    text=text.read()
    text=text+" "

    for i in range(0,len(text)):
        character=text[i]
        if character.isupper()==True:
            character=character.lower()
            upperCase+=1
            new_text=new_text+character
        elif character in string.punctuation:
            if character==".":
                if text[i-1]=="." and text[i+1]==".":
                    pass
                elif text[i+1]==".":
                    continue
                elif text[i-1]==".":
                    continue

            punctuation+=1

        elif character=="…":
            punctuation+=1


        elif character.isdigit()==True:
            numbers+=1
        else:
            new_text=new_text+character
    new_text=new_text.split()
    total_words=len(new_text)
    for i in range(0,total_words):
        word=new_text[i]
        if word in english_words:
            correct_words+=1
        else:
            incorrect_words+=1
            print(word)




    username="d47007el"
    format="Formatting ###################"
    upperCase_changed="Number of upper case letters changed: " + str(upperCase)
    punctuation_removed="Number of punctuations removed: " + str(punctuation)
    number_removed="Number of numbers removed: " + str(numbers)
    spellCheck="Spellchecking ###################"
    number_words="Number of words: " + str(total_words)
    number_correct_words="Number of correct words: " + str(correct_words)
    number_incorrect_words="Number of incorrect words: " + str(incorrect_words)

    os.chdir(str(cwd)+"/"+str(output_file))
    file=file[0:-4]
    print(file)
    file=str(file + "_d47007el.txt")
    file=open(file,"w")
    file.write(username + "\n")
    file.write(format + "\n")
    file.write(upperCase_changed + "\n")
    file.write(punctuation_removed + "\n")
    file.write(number_removed + "\n")
    file.write(spellCheck + "\n")
    file.write(number_words + "\n")
    file.write(number_correct_words + "\n")
    file.write(number_incorrect_words + "\n")
