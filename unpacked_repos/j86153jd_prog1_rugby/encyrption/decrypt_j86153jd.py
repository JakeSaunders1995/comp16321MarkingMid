#import modules
import argparse
import os
#arguments
parser = argparse.ArgumentParser()
parser.add_argument("input", help="The input filepath")
parser.add_argument("output", help="The output filepath")
input_output=parser.parse_args()
input_file=input_output.input
output_file=input_output.output
files = os.listdir(input_file)

#dictonarys
# Dictionary representing morse code chart
MORSE_CODE_DICT = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0', '--..--': ', ', '.-.-.-': '.', '..--..': '?', '-..-.': '/', '-....-': '-', '-.--.': '(', '-.--.-': ')', '/': ' '}


#functions
def det_type(code):
    letter=""
    iter=0
    type=""
    while letter!=":":
        letter=code[iter]
        type+=letter
        iter+=1
    return type

#removes spaces and puts each element in an array
def conv_array(string):
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
#just seperated solving morse to make this easier for me
def solve_morse(code):
    #manualy translate endocded thing to check formating
    out=''
    for letter in code:
        out+= MORSE_CODE_DICT[letter]
    return out
#same thing as morse, just makes it easier for me
def solve_caesar(code,type):
    shift=type[14]+type[15]
    out=""
    if shift[0]=="+":
        for i in code:
            for x in range(0,len(i)):
                out+=chr(ord(i[x])-int(shift[1]))
            out+=" "
    elif shift[0]=='-':
        for i in code:
            for x in range(0,len(i)):
                out+=chr(ord(i[x])+int(shift[1]))
            out+=" "
    return out


def solve_hex(code):
    out=""
    for item in code:
        out+=bytes.fromhex(item).decode('utf-8')
    return out

def output(out):
    out_temp=file.rstrip(".txt")
    out_filepath=output_file+"/"+out_temp+"_j86153jd.txt"
    out_file=open(out_filepath,'w')
    out_file.write(out)
    out_file.close()



#main
#loop to check all files

for file in files:
    file_path=input_file+'/'+file
    encrpted_file=open(file_path,'r')
    code=encrpted_file.read()
    type=det_type(code)
    code_no_type=code.replace(type,"")
    code_array=conv_array(code_no_type)
    if "Morse Code" in type:
        decrypt_code=solve_morse(code_array)
        output(decrypt_code)
    elif "Hex" in type:
        decrypt_code=solve_hex(code_array)
        output(decrypt_code)
    elif "Caesar Cipher" in type:
        decrypt_code=solve_caesar(code_array,type)
        output(decrypt_code)
