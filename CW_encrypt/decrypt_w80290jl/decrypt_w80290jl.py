import argparse
import os
import re

morse_dict = {'.-': 'a',
        '-...': 'b',
        '-.-.': 'c',
        '-..':'d',
        '.':'e',
        '..-.':'f',
        '--.': 'g',
        '....': 'h',
        '..': 'i',
        '.---':'j',
        '-.-': 'k',
        '.-..': 'l',
        '--': 'm',
        '-.': 'n',
        '---': 'o',
        '.--.': 'p',
        '--.-': 'q',
        '.-.': 'r',
        '...': 's',
        '-': 't',
        '..-': 'u',
        '...-': 'v',
        '.--': 'w',
        '-..-': 'x',
        '-.--': 'y',
        '--..': 'z',
        '.----': '1',
        '..---': '2',
        '...--': '3',
        '....-': '4',
        '.....': '5',
        '-....': '6',
        '--...': '7',
        '---..': '8',
        '----.': '9',
        '-----': '0',
        '..--..': '?',
        '-..-.': '/',
        '-.--.-': '()',
        '-....-': '-',
        '.-.-.-': '.',
        '/':' '
        };


def encryption(input_file,output_file):
    src_data = input_file.readline()
    
    split_index = src_data.find(":")
    method_name = src_data[0:split_index]
    encryption_data = src_data[split_index+1:]
    
    
    result = ""
    if method_name == "Hex" :
        hex_data = bytes.fromhex(encryption_data)
        result = str(hex_data,encoding="ASCII")
        result =result.lower()
    elif method_name == "Caesar Cipher(+3)":
        for c in encryption_data:
            if(c==' '):
                result = result + c
            else:
                value = ord(c)
                if (47<value and value <58) or (64<value and value <91) or (96<value and value <123):                 
                    value = ord(c)-3                    
                    if value < 48: #number
                        value = value + 10
                    elif 60<value and value < 65: #upper case
                        value =value + 26
                    elif 93<value and value < 97 : #lower case 
                        value = value +  26
                    else:
                        pass
                    result = result + chr(value)
                    result = result.lower()
    elif method_name == "Morse Code":
        raw_item_list = encryption_data.split(" ")
        for item in raw_item_list:
            result = result + morse_dict[item]
            result = result.lower()
    else:
        pass
    output_file.write(result)

user_name = "w80290jl"

parse = argparse.ArgumentParser()
parse.add_argument("input_file",type = str)
parse.add_argument("output_file",type = str)
args = parse.parse_args()

input_folder = args.input_file
output_folder = args.output_file

if output_folder.endswith('\\') or output_folder.endswith('/'):
    pass
else:
    output_folder = output_folder +"/"
    
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

#print("input_folder:",input_folder)
#print("output_folder:",output_folder)

for root, dirs, files in os.walk(input_folder):
    for f in files:
        input_file_path = os.path.join(root, f)        
        input_file = open(input_file_path,'r')
        
        output_file_name = f.split('.')[0]+"_"+user_name+".txt"
        output_file_path = output_folder + output_file_name
        output_file = open(output_file_path,'w')
        encryption(input_file,output_file)
        input_file.close()
        output_file.close()