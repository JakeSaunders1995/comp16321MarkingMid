import argparse
import os

def open_file(file_path, array=True):
    file = open(file_path,"r")
    output = file.readlines() if array else file.read()
    file.close()
    return output

parser = argparse.ArgumentParser()
parser.add_argument("files", type=str, nargs="+")
path = parser.parse_args()

all_words = open_file(path.files[0])
for i in range (0,len(all_words)):
    all_words[i] = all_words[i].strip("\n")

scanned_folder = os.scandir(path.files[1])
full_paths = []
for i in scanned_folder:
    if i.is_file():
        full_paths.append(i.path)
full_paths = sorted(full_paths)

for file_num, current_file in enumerate(full_paths):

    text = open_file(current_file,False)
    removed_numbers = "1234567890"
    removed_punc = ".?!,:;—‐(){}\'\"…[]@#<>/"
    # period, question mark, exclamation point, comma, colon, semicolon, dash, hyphen, brackets,
    # braces, parentheses, apostrophe, quotation mark, and ellipsis. +more symbols

    upper_count = 0
    punc_count = 0
    number_count = 0
    for i in text:
        if 65<=ord(i)<=90:
            upper_count+=1
        elif i in removed_punc:
            punc_count+=1
        elif i in removed_numbers:
            number_count+=1

    for i in removed_numbers:
        text = text.replace(i,"")
    for i in removed_punc:
        text = text.replace(i,"")

    text = text.replace("  "," ")
    text = text.lower()
    #print(text)

    words_array= text.split()
    correct_words = 0
    for i in words_array:
        if i in all_words: correct_words += 1

    output_text = "h54023kc\nFormatting " + "#"*19+ "\nNumber of upper case words transformed: "+ str(upper_count) + "\nNumber of punctuation’s removed: "+ str(punc_count)+"\nNumber of numbers removed: "+ str(number_count) +"\nSpellchecking "+"#"*19 +"\n"+"Number of words in file: "+ str(len(words_array)) + "\nNumber of correct words in file:"+ str(correct_words) + "\nNumber of incorrect words in file:"+ str(len(words_array)-correct_words)
    #print(output_text)

    file = open(path.files[2]+"/test_file"+str(file_num+1)+"_h54023kc.txt","w")
    file.write(output_text)
    file.close()
