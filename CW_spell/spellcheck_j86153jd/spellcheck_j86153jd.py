#import modules
import argparse
import os
#arguments
parser = argparse.ArgumentParser()
parser.add_argument("english", help="The english words file filepath")
parser.add_argument("input", help="The input filepath")
parser.add_argument("output", help="The output filepath")
input_output=parser.parse_args()
input_file=input_output.input
output_file=input_output.output
english_file=input_output.english
files = os.listdir(input_file)

#functions
def conv_array_letter(string):
    array=[]
    for i in range(0,len(string)):
        array.append(string[i])
    return array


def conv_array_word(string):
    array=[]
    temp_store=""
    for i in range(0,len(string)):
        if string[i]!=" ":
            temp_store+=string[i]
        else:
            array.append(temp_store)
            temp_store=""
    array.append(temp_store)
    return array



#importing english words text file
english=open(english_file,'r')
english_words=english.read()
english.close()

#main

for file in files:
    file_path=input_file+'/'+file
    spellcheck_file=open(file_path,'r')
    spellcheck_words=spellcheck_file.read()
    spellcheck_file.close()
    spellcheck_array=conv_array_letter(spellcheck_words)
    formated_file=""
    punct_remove=0
    upper_remove=0
    num_remove=0
    spell_wrong=0
    #formatting the text
    for letter in spellcheck_array:
        if letter.isupper():
            letter=letter.lower()
            upper_remove+=1
        if letter.isdigit():
            letter=""
            num_remove+=1
        if letter!=" " and not(letter.isdigit() or letter.isalpha()):
            letter=""
            punct_remove+=1
        formated_file+=letter
    words_array=conv_array_word(formated_file)
    for word in words_array:
        if word not in english_words:
            spell_wrong+=1

    #open output file
    out_temp=file.rstrip(".txt")
    out_filepath=output_file+"/"+out_temp+"_j86153jd.txt"
    out_file=open(out_filepath,'w')
    out_file.write("j86153jd\n")
    out_file.write("Formatting ########################### \n")
    out_file.write("Number of upper case words transformed: " + str(upper_remove) + "\n")
    out_file.write("Number of punctuation’s removed: " + str(punct_remove) + "\n")
    out_file.write("Number of numbers removed: " + str(num_remove) + "\n")
    out_file.write("Spellchecking ###################\n")
    out_file.write("Number of words in file: "+ str(len(words_array))+"\n")
    out_file.write("Number of correct words in file: "+ str(len(words_array)-spell_wrong)+"\n")
    out_file.write("Number of incorrect words in file: "+ str(spell_wrong)+"\n")
#close output file
    out_file.close()
