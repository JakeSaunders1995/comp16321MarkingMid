import argparse
import os,sys

def hex(input):
    input=input.split(' ')
    output=""
    for i in range(len(input)):
        input[i]=chr(int(input[i],16))
        output +=input[i]
    return output

def caesar(input):
    output=""
    for i in range(len(input)):
        if(input[i]!=' '):
            ASCII_input =ord(input[i])
            ASCII_input -=3
            output+=chr(ASCII_input)
        else:
            output+=input[i]
    return output

def morse(input):
    morse_map=[
        ['.-','a'],['-...','b'],['-.-.','c'],['-..','d'],                               #0-3
        ['.','e'],['..-.','f'],['--.','g'],['....','h'],                                 #4-7
        ['..','i'],['.---','j'],['-.-','k'],['.-..','l'],['--','m'],['-.','n'],         #8-13  
        ['---','o'],['.--.','p'],['--.-','q'],['.-.','r'],['...','s'],['-','t'],        #14-19
        ['..-','u'],['...-','v'],['.--','w'],['-..-','x'],['-.--','y'],['--..','z'],    #20-25
        ['-----','0'],['.----','1'],['..---','2'],['...--','3'],['....-','4'],          #26-30
        ['.....','5'],['-....','6'],['--...','7'],['---..','8'],['----.','9'],          #31-35
        ['.-.-.-','.'],['..--..','?'],['-.-.--','!'],['--..--',','],['---...',':'],     #36-40
        ['-.-.-.',';'],['-....-','-'],['-.--.','('],['-.--.-',')'],['.-..-.','"'],      #41-45
        ['/',' ']                                                                       #46
    ]
    input=input.split()
    output=""
    for i in range(len(input)):
        for j in range(len(morse_map)):
            if(input[i]==morse_map[j][0]):
                output+=morse_map[j][1]
    return output

def selection(sign,content):
    if(sign == "Hex"):
        return hex(content)
    elif(sign == "Caesar Cipher(+3)"):
        return caesar(content)
    elif(sign == "Morse Code"):
        return morse(content)
    
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
        input_tuple =(f_input.read()).split(":")
        input_sign =input_tuple[0]
        input_content =input_tuple[1]
        f_output.write(selection(input_sign,input_content))
