import argparse
import os,sys

def calculate_sore(file):
    arr =file.read()
    i=0;score_1=0;score_2=0
    while(i<len(arr)):
        if(arr[i]=='1'):
            score_1+=rules(arr[i+1])
        elif(arr[i]=='2'):
            score_2+=rules(arr[i+1])
        i+=1
    result=str(score_1) + ":" + str(score_2)
    return result
            
def rules(char):
    if (char == 't'): return 5
    elif (char =='c'): return 2
    elif(char=='p'or'd'): return 3

parser = argparse.ArgumentParser()
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
        f_output.write(calculate_sore(f_input))
        
