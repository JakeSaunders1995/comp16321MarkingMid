import sys
import os
import string

input_path = sys.argv[1]
output_path = sys.argv[2]

for file_name in os.listdir(input_path):
    with open(input_path + "/{}".format(file_name), "r") as f:
        cipher_string = f.read()
        f.close()
        encrypt_method, cipher_text = tuple(cipher_string.split(":"))
        plain_text = ""
            
        if encrypt_method.lower() == "hex":
            
            hex_list = cipher_text.split()
            for char in range(len(hex_list)):
                dec_chars = int(hex_list[char], 16)
                plain_text += chr(dec_chars)
            plain_text = plain_text.lower()

        elif encrypt_method.lower() == "caesar cipher(+3)":
            
            caesar_string = cipher_text.strip()
            cipher_list = []
            cipher_words = caesar_string.split(" ")
            for words in cipher_words:
                cipher_list.append(words)
            for cipher_pos in range(len(cipher_list)):
                cipher_text_str = cipher_list[cipher_pos]
                cipher_text_char_list = [char for char in cipher_text_str]
                for i in range(len(cipher_text_char_list)):
                    cipher_text_char = cipher_text_char_list[i]
                    if cipher_text_char not in list(string.digits) and cipher_text_char != " " and cipher_text_char != "," and cipher_text_char != ";" and cipher_text_char != "(" and cipher_text_char != ")" and cipher_text_char != "." and cipher_text_char != "?" and cipher_text_char != ":" and cipher_text_char != "-" and cipher_text_char != "'" and cipher_text_char != "{" and cipher_text_char != "}" and cipher_text_char != "[" and cipher_text_char != "]" and cipher_text_char != '"' and cipher_text_char != "...":
                        ASCIIValue = ord(cipher_text_char)
                        ASCIIValue -= 3
                        plain_text += chr(ASCIIValue)
                    else:
                        plain_text += cipher_text_char
                plain_text += " "
                cipher_pos += 1
            plain_text = plain_text.lower()

        elif encrypt_method.lower() == "morse code":

            morse_code_dict = {'A':'.-', 'B':'-...',
                        'C':'-.-.', 'D':'-..', 'E':'.',
                        'F':'..-.', 'G':'--.', 'H':'....',
                        'I':'..', 'J':'.---', 'K':'-.-',
                        'L':'.-..', 'M':'--', 'N':'-.',
                        'O':'---', 'P':'.--.', 'Q':'--.-',
                        'R':'.-.', 'S':'...', 'T':'-',
                        'U':'..-', 'V':'...-', 'W':'.--',
                        'X':'-..-', 'Y':'-.--', 'Z':'--..',
                        '1':'.----', '2':'..---', '3':'...--',
                        '4':'....-', '5':'.....', '6':'-....',
                        '7':'--...', '8':'---..', '9':'----.',
                        '0':'-----', ', ':'--..--', '.':'.-.-.-',
                        '?':'..--..', ' ':'/', '-':'-....-',
                        '(':'-.--.', ')':'-.--.-','!':'-.-.--'}

            message = ""
            morse_to_letter = {morse: letters for letters, morse in morse_code_dict.items()}
            morse_string = cipher_text.strip()
            morse_list = morse_string.split(" ")
            for char in range(len(morse_list)):
                message += morse_to_letter[morse_list[char]]
            plain_text = message.lower() 
        
        file_name = os.path.basename(input_path + "/{}".format(file_name))
        
        new_file_name = os.path.join(output_path, file_name.split(".")[0] + "_u95206ma.txt")
        decrypt_text = open(new_file_name, "w+")
        decrypt_text.write(plain_text)
        decrypt_text.close()        
            






