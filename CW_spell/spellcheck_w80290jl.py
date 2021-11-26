import argparse
import os
import re
import sys

def spellchecker(dic_file,input_file,output_file,user_name):
    word_dic = set()
    
    upper_case_count = 0;
    number_count = 0;
    punctuation_count = 0;
    words_count = 0;
    correct_count = 0;
    incorrect_count = 0;
    formated_text=""
    
    src_dic_info = dic_file.readlines()
    for line in src_dic_info:
        line = line.replace('\n','')
        word_dic.add(line) #add into set()
        
    src_data = input_file.readlines()
    
    pattern_upper_case = re.compile(r"[A-Z]")
    pattern_number = re.compile(r"\d")
    pattern_words = re.compile(r"[a-z]+")
    pattern_punctuation = re.compile(r"[^a-z\s\d@#]")#s-space
    for line in src_data:
        find_result = pattern_upper_case.findall(line)
        upper_case_count = upper_case_count + len(find_result)
        
        line = line.lower()
        
        find_result = pattern_number.findall(line)
        number_count = number_count + len(find_result)
        
        for key in find_result:
            line = line.replace(key,"")

        line = line.replace("...", ".")   
        find_result = pattern_punctuation.findall(line)
        punctuation_count = punctuation_count + len(find_result)
        for key in find_result:
            line = line.replace(key,"")
        
        find_result = pattern_words.findall(line)
        words_count = words_count + len(find_result)
        for word in find_result:
            if word in word_dic:
                correct_count = correct_count + 1
            else:
                incorrect_count = incorrect_count + 1
        
        formated_text = formated_text + line;
        
    formated_info = user_name + "\n"
    formated_info =formated_info + "Formatting ###################" + "\n"
    formated_info =formated_info +  "Number of upper case letters changed: " + str(upper_case_count) +"\n"
    formated_info =formated_info +  "Number of punctuations removed: " + str(punctuation_count) +"\n"
    formated_info =formated_info +  "Number of numbers removed: " + str(number_count) +"\n"
    formated_info =formated_info +  "Spellchecking ###################" + "\n"
    formated_info =formated_info +  "Number of words: " + str(words_count) +"\n"
    formated_info =formated_info +  "Number of correct words: " + str(correct_count) +"\n"
    formated_info =formated_info +  "Number of incorrect words: " + str(incorrect_count) +"\n"
    output_file.write(formated_info)
            

user_name = "w80290jl"
dic_path = sys.argv[1]
input_folder = sys.argv[2]
output_folder = sys.argv[3]

if output_folder.endswith('\\') or output_folder.endswith('/'):
    pass
else:
    output_folder = output_folder +"/"


for root, dirs, files in os.walk(input_folder):
    for f in files:
        
        dic_file = open(dic_path,'r')
        
        input_file_path = os.path.join(root, f)        
        input_file = open(input_file_path,'r')
        
        output_file_name = f.split('.')[0]+"_"+user_name+".txt"
        output_file_path = output_folder + output_file_name
        output_file = open(output_file_path,'w')
        spellchecker(dic_file,input_file,output_file,user_name)
        
        dic_file.close()
        input_file.close()
        output_file.close()