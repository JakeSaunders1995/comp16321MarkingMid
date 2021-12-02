import os
import sys
import re

import string
input_path = "/home/csimage/python_midterm/16321_python_coursework_m57983ma/midterm_files(1)/midterm_files/Example_inputs/Example_inputs_program2"


sorted_path_list = sorted(os.listdir(input_path))

final_answer_list = []

MORSE_CODE_DICT = {'..-.': 'f', '-..-': 'x',
                 '.--.': 'p', '-': 't', '..---': '2',
                 '....-': '4', '-----': '0', '--...': '7',
                 '...-': 'v', '-.-.': 'c', '.': 'e', '.---': 'j',
                 '---': 'o', '-.-': 'k', '----.': '9', '..': 'i',
                 '.-..': 'l', '.....': '5', '...--': '3', '-.--': 'y',
                 '-....': '6', '.--': 'w', '....': 'h', '-.': 'n', '.-.': 'r',
                 '-...': 'b', '---..': '8', '--..': 'z', '-..': 'd', '--.-': 'q',
                 '--.': 'g', '--': 'm', '..-': 'u', '.-': 'a', '...': 's', '.----': '1', '/':' '}



for filename in sorted_path_list:
   with open(os.path.join(input_path, filename), 'r') as f:
       text = f.readline().split(":") #this makes a the line into a string then makes into a list
       new_list = text[1].split(" ")
       decrypted_message = ""
       for i in new_list:
           if text[0] == "Morse Code":
               decrypted_message += MORSE_CODE_DICT[i]


           elif text[0] == "Hex":
               byte_array = bytearray.fromhex(text[1])
               hex_string = byte_array.decode().lower()





           elif text[0] == "Caesar Cipher(+3)":
               encrypted_message = text[1].lower()
               alphabet = string.ascii_lowercase # "abcdefghijklmnopqrstuvwxyz"
               decrypted_message1 = ""
               key = 3
               for c in encrypted_message:

                   if c in alphabet:
                       position = alphabet.find(c)
                       new_position = (position - key) % 26
                       new_character = alphabet[new_position]
                       decrypted_message1 += new_character
                   else:
                       decrypted_message1 += c


final_answer_list.append(hex_string)
final_answer_list.append(decrypted_message1.strip())
final_answer_list.append(decrypted_message)
print(final_answer_list)



for i,k in enumerate(final_answer_list):


    output = open('/home/csimage/Downloads/midterm_files(1)/midterm_files' + str(i+1)+ '_m57983ma', 'w')
    output.write(k)
