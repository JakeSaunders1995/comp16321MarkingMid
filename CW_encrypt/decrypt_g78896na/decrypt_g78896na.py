#This program will decript the hex, morse or ceaser cipher into normal text
import os
import argparse

def line_formatter(raw_input_line):
    #Input line will contain a preamble whether the text is encrypted in hex, morse or ceaser cipher.
    #The line will be decoded and the spaces will be removed and sent to the appropriate function
    if raw_input_line[0] == 'H':
        replacedLine = raw_input_line.replace("HEX:", "")#.replace(" ", "")
        print("After removal of Hex: : ", replacedLine)
        hex_decrypted_line = hex_decrypt(replacedLine)
        return hex_decrypted_line

    if raw_input_line[0] == "M":
        if raw_input_line[10] == ":":
            replacedLine = raw_input_line.replace("MORSE CODE:", "")
            print("After removel of Morse Code::" + replacedLine)
            morse_decrypted_line = morse_decrypt(replacedLine)
            return morse_decrypted_line

    if raw_input_line[0] == 'C':
        if raw_input_line[17] == ":":
            replacedLine = raw_input_line.replace("CAESAR CIPHER(+3):", "")
            print("After removal of Caesar Cipher(+3): " + replacedLine )
            caesar_decrypted_line = caesar_decrypt(replacedLine)
            return caesar_decrypted_line

        



def hex_decrypt(hex_input_line):
    hex_dictionary = {"09":"\t", "0A":"\n", "0B":"\v", "0D":"\r", "20":" ", "21":"!", "22":"\"", "23":"#", "24":"$", "25":"%", "26":"&", "27":"'",
    "28":"(", "28":")", "2A":"*", "2B":"+", "2C":",", "2D":"-", "2E":".", "2F":"/", "30":"0", "31":"1", "32":"2", "33":"3", "34":"4", "35":"5",
    "36":"6", "37":"7", "38":"8", "39":"9", "3A":":", "3B":";", "3C":"<", "3D":"=", "3E":">", "3F":"?", "40":"@", "41":"A", "42":"B", "43":"C", 
    "44":"D", "45":"E", "46":"F", "47":"G", "48":"H", "49":"I", "4A":"J", "4B":"K", "4C":"L", "4D":"M", "4E":"N", "4F":"O", "50":"P", "51":"Q",
    "52":"R", "53":"S", "54":"T", "55":"U", "56":"V", "57":"W", "58":"X", "59":"Y", "5A":"Z", "5B":"[", "5C":"\\", "5D":"]", "5E":"^", "5F":"_",
    "60":"`", "61":"a", "62":"b", "63":"c", "64":"d", "65":"e","66":"f", "67":"g", "68":"h", "69":"i", "6A":"j", "6B":"k", "6C":"l", "6D":"m",
    "6E":"n", "6F":"o", "70":"p", "71":"q", "72":"r", "73":"s", "74":"t", "75":"u", "76":"v", "77":"w", "78":"x", "79":"y", "7A":"z", "7B":"{",
    "7C":"|", "7D":"}", "7E":"~", "7F":"\b"}

    hex_decrypted_str = ""
    hex_input_list = hex_input_line.split(" ")
    print("Hex input list: ")
    print(hex_input_list)

    for decrypt in hex_input_list:
        hex_decrypted_str = hex_decrypted_str + hex_dictionary[decrypt]

    return hex_decrypted_str

def caesar_decrypt(caesar_input_line):
    caesar_decrypted_str = ""
    length_caesar_input_line = len(caesar_input_line)
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    count = 0
    while count < length_caesar_input_line:
        input_char_position = alphabets.find(caesar_input_line[count])
        print("Character position : " + str(input_char_position))
        print("The decrypted character is: " + alphabets[input_char_position - 3])
        if caesar_input_line[count] == " ":
            caesar_decrypted_str = caesar_decrypted_str + " "
        elif caesar_input_line[count] != " ":
            caesar_decrypted_str = caesar_decrypted_str + alphabets[input_char_position - 3]
        count = count + 1
    print("The decrypted caeser string is: " + caesar_decrypted_str)
    return caesar_decrypted_str






    


   


def morse_decrypt(morse_input_line):
    morse_dictionary = {".-":"a", "-...":"b", "-.-.":"c", "-..":"d", ".":"e", "..-.":"f", "--.":"g", "....":"h", "..":"i", ".---":"j", "-.-":"k",
            ".-..":"l", "--":"m", "-.":"n", "---":"o", ".--.":"p", "--.-":"q", ".-.":"r", "...":"s", "-":"t", "..-":"u", "...-":"v", ".--":"w", 
            "-..-":"x", "-.--":"y", "--..":"z", ".----":"1", "..---":"2", "...--":"3", "....-":"4", ".....":"5", "-....":"6", "--...":"7", "---..":"8",
            "----.":"9", "-----":"0", ".-.-.-":".", "--..--":",", "---...":":", "..--..":"?", ".----.":"'", "-....-":"-", "-..-.":"/", "-.--.-":"(", 
            ".-..-.":"??"}
    length_morse_input_line = len(morse_input_line)
    morse_lst = morse_input_line.split("/")
    print("Morse List[0]: ")
    print(morse_lst)
    print("Morse List[0] Ends: ")
    #print(morse_lst[0])
    #print("morse_lst[0] ends")
    #print("Morse List [0][0]")
    #print(morse_lst[0][0])
    #print("Morse List [0] [0] ends")

    #morse_lst.remove(" ")
    test_morse_word = ""
    morse_decrypted_line = ""
    morse_word_final = ""

    for morse_lst_lst in morse_lst:
        morse_word = morse_lst_lst.split(" ")
        #print("morse_word: ")
        #print(morse_word)

        #morse_char will contain a single character such as .... for character 'h'
        for morse_char in morse_word:
            print("The morse_char is: " + morse_char)
            print("The length of morse_char is: " + str(len(morse_char)))
            if len(morse_char) > 0:
                print("Decryption of morse_char is: " + morse_dictionary[morse_char])
                morse_decrypted_line = morse_decrypted_line + morse_dictionary[morse_char]
            elif len(morse_char) == 0:
                morse_decrypted_line = morse_decrypted_line + " "

        

        #count = 0
        #print("The length of morse_word is: " + str(len(morse_word)))
        #while count < len(morse_word):
         #   for morse_char in morse_word:
          #      if len(morse_char) > 0:
           #         morse_decrypted_line = morse_decrypted_line + morse_dictionary[morse_char]

            #count = count + 1
            #morse_decrypted_line = morse_decrypted_line + " "



                    
            #while(1):
            #    i=0


            #while i < (len(morse_char)-1):
            #    if morse_char[i] != '.' or morse_char[i] != '-':
                    #morse_char.remove[i]
                
            #morse_word_final = morse_word_final + morse_char
            #print("morse_word: ")
            #print(morse_word[1])
            
        #print("The morse_word_final is: " + morse_word_final)

        #for morse_char in morse_word:
        #print("morse_word[0] :", morse_word[0].replace(" ", ""))
        #print("Decrypted morse_word[0]: ", morse_dictionary[morse_word[0]])
        #print("morse_word[1] :", morse_word[1])
        #morse_lst_lst.replace(" ", "")
        #print(morse_lst_lst)
        #print(morse_dictionary[morse_lst_lst])
        #print("morse_word: ")
        #for morse_char in morse_word:
        #    if morse_char != '.' or morse_char != '-':
        #        print("Space")
        #print(morse_word)
    
    list_count = 0
        
        #while list_count < len(morse_word):

    while list_count < 1:
        #print("Inside while : " + morse_word[list_count].replace(" ", "") + " " + str(list_count))
        #morse_decrypted_line = morse_decrypted_line + morse_dictionary[morse_word[0].replace(" ", "")]
        list_count = list_count + 1
    #morse_decrypted_line = morse_dictionary["...."]
    print("The decrypted line: " + morse_decrypted_line)
    return morse_decrypted_line



    


#input_line_hex = "Hex:31 32 30 32 39 71 69 46 3C 3F 6C 4E"

#file_input_line_hex = "Hex:31 32 30 32 39 71 69 46 3C 3F 6C 4E 53 6f 6c 76 69 6e 67 20 68 65 78 20 69 73 20 76 65 72 79 20 65 61 73 79 20 69 6e 20 70 79 74 68 6F 6E"

#To handle hexadecimal characters in any form lower or upper cases.
#input_line_hex = file_input_line_hex.upper()

#input_line_morse = "Morse Code:.... --- .-- . ...- . .-. / ... --- .-.. ...- .. -. --. / -- --- .-. ... . / -.-. --- -.. . / -- .- -.-- / -... . / - .... . / -- --- ... - / -.. .. ..-. ..-. .. -.-. ..- .-.. -"

#output_line = line_formatter(input_line_hex).lower()

#output_line = line_formatter(input_line_morse)
#print(output_line)


#Processing command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("input_file_path", type = str)
parser.add_argument("output_file_path", type = str)
args = parser.parse_args()
print(args.input_file_path)
print(args.output_file_path)
input_file_arr = os.listdir(args.input_file_path)
print(input_file_arr)


#Number of files in the input folder
number_of_files = len(input_file_arr)
count = 0
while count < number_of_files:
    #file_handle = open("/home/csimage/python_cde/experiments_python/mid-term/decryption/midterm_files(1)/midterm_files/Example_inputs/Example_inputs_program2/test_file3.txt", "r")
    file_handle = open((args.input_file_path + "/" + input_file_arr[count]), "r")
    input_line = file_handle.read().upper()
    file_handle.close()

    print("Input Line from File: " + input_line)

    output_line = line_formatter(input_line).lower()
    print(output_line)
    file_handle = open((args.output_file_path + "/" + str(input_file_arr[count]).replace(".txt", "") + "_" + "g78896na") + ".txt", "w")
    file_handle.write(output_line)
    file_handle.close()
    count = count + 1

