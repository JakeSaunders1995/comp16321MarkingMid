import sys
import os

n = len(sys.argv) #total arguments
print("Total arguments passed:", n)

print("\nName of Python script:", sys.argv[0]) #printing the python script

input_directory = sys.argv[1]
output_directory = sys.argv[2]

for filename in os.listdir(input_directory):
    if filename.endswith(".txt"):             #Opening the input file
        morse_to_eng = {
            '....' : 'h', '.-' : 'a', '-...' : 'b',
            '-.-.' : 'c', '-..' : 'd', '.' : 'e', '..-.' : 'f',
            '--.' : 'g', '..' : 'i', '.---' : 'j', '-.-' : 'k', '.-..' : 'l',
            '--' : 'm', '-.' : 'n', '---' : 'o', '.--.' : 'p', '--.-' : 'q',
            '.-.' : 'r', '...' : 's', '-' : 't', '..-' : 'u', '...-' : 'v',
            '.--' : 'w', '-..-' : 'x', '-.--' : 'y', '--..' : 'z', '.-.-.-' : '.',
            '..--..' : '?', '--..--' : ',', '/' : ' '
        }                                                             #dictionary for morse code to english conversion

        input_file = open(os.path.join(input_directory,filename),"r") #Opening The required file for input
        test_str = input_file.read()                                  #Reading File Data
        final_str = ""
        input_file.close()                                            #Closing the input file

        x=filename
        x = x.replace(".txt", "_j34330vk.txt")
        output__file = open(os.path.join(output_directory, x), "w") #Opening the input file

        input_data = test_str.split(":" , 1)                      #Splitting data to get data from the file seperate from encryption type
        content = input_data[1]
        content_list = content.split(" ")                         #Creating a list from the file data 

        if input_data[0] == "Hex":                                #Checking if the data is encrypted in the form of hex
            code_in_list = content.split(" ")
            for i in code_in_list:
                solved = bytes.fromhex(i).decode('utf-8')         #Converting data from hex to english
                final_str += solved
                final_str=final_str.lower()                               #Adding data to final string
            output__file.write(final_str)
                
        elif input_data[0] == "Caesar Cipher(+3)":                #Checking if the data is encrypted in the form of cipher
            for j in content_list:
                for i in j:  
                    if i in ['a','b','c']:
                        ascii_value = ord(i)
                        ascii_value += 23
                                                         #converting data from caesar cipher to english
                    else:
                        ascii_value = ord(i)
                        ascii_value -= 3
                    final_str += chr(ascii_value)
                final_str += " "
            output__file.write(final_str)                         #Adding data to final string

        elif input_data[0] == "Morse Code":                       #Checking if the data is encrypted in the form of morse code
            for i in content_list:                                #converting data from morse code to english
                if i in morse_to_eng.keys():
                    final_str += morse_to_eng[i]
            output__file.write(final_str)                         #Adding data to final string
                

        output__file.close()                                      #Closing the output file

    else:
        continue
