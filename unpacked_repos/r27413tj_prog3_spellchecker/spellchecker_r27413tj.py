import argparse
import os,sys
import re

def rem_punctuation(arr):
    result=""
    outputlist=[]
    pattern_1 =re.compile(r'[a-zA-Z0-9]+')
    for i in range(len(arr)):
        result = pattern_1.findall(arr[i])
        outputlist.append(result)
    return outputlist
        
def count_rem_punction(list_origin,list_removed):
    count=0
    for i in range(len(list_removed)):
        if(list_removed[i][0]!=list_origin[i]):
            count += len(list_origin[i])-len(list_removed[i][0])
    return count
    
def rem_num(list):
    num_list=['0','1','2','3','4','5','6','7','8','9']
    count=0
    for i in range(len(list)):
        for j in range (len(num_list)):
            if(num_list[j] in list[i][0]):
                list[i][0]=(list[i][0]).replace(num_list[j],'')
                count+=1
    return count

def upperTolower(list):
    count=0
    for i in range(len(list)):
        for j in list[i][0]:
            if j.isupper():
                count+=1
        list[i][0]=str(list[i][0]).lower()
    return count

def remove_empty(list):
    for i in list:
        if i==['']:
            list.remove(i)
            
def correctwords(list):
    file=open(path.EnglishWords) 
    dics=file.read()
    count=0
    for i in range(len(list)):
        if list[i][0] in dics:
            count+=1
    return count    

parser = argparse.ArgumentParser()
parser.add_argument('EnglishWords',help ='Englishwords')
parser.add_argument('input_folder', help='input')
parser.add_argument('output_folder',help='output')
path = parser.parse_args()

for input_file in os.listdir(path.input_folder):
    os.chdir(path.input_folder)
    input_filepath=os.path.join(os.getcwd(),input_file)
    with open(input_filepath) as f_input:
        os.chdir(path.output_folder)
        output_file=input_file.replace(".txt","_r27413tj.txt") 
        f_output=open(output_file,"w")
        input=(f_input.read()).split()
        output=rem_punctuation(input)
        num_punctuation =count_rem_punction(input,output)
        num_number =rem_num(output)
        num_upper=upperTolower(output)
        remove_empty(output)
        num_words=len(output)
        num_correct=correctwords(output)
        num_incorrect=num_words-num_correct
        f_output.write("r27413tj\n")
        f_output.write("Formatting ###################\n")
        f_output.write("Number of upper case letters changed: "+str(num_upper))
        f_output.write("\nNumber of punctuations removed: "+str(num_punctuation))
        f_output.write("\nNumber of numbers removed: "+str(num_number))
        f_output.write("\nSpellchecking ###################")
        f_output.write("\nNumber of words: "+str(num_words))
        f_output.write("\nNumber of correct words: "+str(num_correct))
        f_output.write("\nNumber of incorrect words: "+str(num_incorrect))
