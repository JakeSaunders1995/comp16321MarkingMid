import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("files", type=str, nargs="+")
path = parser.parse_args()

scanned_folder = os.scandir(path.files[0])
full_paths = []
for i in scanned_folder:
    if i.is_file():
        full_paths.append(i.path)
full_paths = sorted(full_paths)

for file_num, current_file in enumerate(full_paths):
    file = open(current_file,"r")
    input_text = file.read()
    file.close()

    input_text = input_text.strip("\n")
    input_text = input_text.split(":")
    output_string = ""
    if input_text[0] == "Hex":
        input_text[1] = input_text[1].split()
        for hex in input_text[1]: output_string+=chr(int(hex,16))
    elif input_text[0] == "Caesar Cipher(+3)":
        ignored_punctuation = " .?!,:;—‐(){}\'\"…[]@#<>/"
        for i in input_text[1]: output_string+=str(chr(ord(i)-3)) if (not i in ignored_punctuation) else i
    elif input_text[0] == "Morse Code":
        input_text[1] = input_text[1].split()
        morse_code_dict = {".-":"a", "-...":"b", "-.-.":"c", "-..":"d",".":"e" ,"..-.":"f" ,"--.":"g" ,"....":"h",
                        "..":"i", ".---":"j", "-.-":"k", ".-..":"l", "--":"m", "-.":"n", "---":"o", ".--.":"p",
                        "--.-":"q", ".-.":"r", "...":"s", "-":"t", "..-":"u", "...-":"v", ".--":"w","-..-":"x",
                        "-.--":"y", "--..":"z", "-----":"0", ".----":"1", "..---":"2", "...--":"3", "....-":"4",
                        ".....":"5", "-....":"6", "--...":"7", "---..":"8", "----.":"9"}
        for i, morse_code in enumerate(input_text[1]):
            if input_text[1][i] in morse_code_dict:
                output_string+= morse_code_dict[morse_code]
            elif morse_code == "/":
                output_string+=" "
            else:
                output_string+=morse_code
    file = open(path.files[1]+"/test_file"+str(file_num+1)+"_h54023kc.txt","w")
    output_string = output_string.lower()
    file.write(output_string)
    file.close()
