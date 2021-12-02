import sys
import os

MORSE_CODE_TO_ALPHABET = {
     ".-" : "a", "-..." : "b", "-.-." : "c",
     "-.." : "d", "." : "e", "..-." : "f",
     "--." : "g", "...." : "h", ".." : "i",
     ".---" : "j", "-.-" : "k", ".-.." : "l",
     "--" : "m", "-." : "n", "---" : "o", ".--." : "p",
     "--.-" : "q", ".-." : "r", "..." : "s", "-" : "t",
     "..-" : "u", "...-" : "v", ".--" : "w", "-..-" : "x",
     "-.--" : "y", "--.." : "z", "-----" : "0", ".----" : "1",
     "..---" : "2", "...--" : "3", "....-" : "4", "......" : "5",
     "-...." : "6", "--..." : "7", "---.." : "8", "----." : "9",
     ".-.-.-" : ".", "--..--" : ",", "..--.." : "?", "---..." : ":",
     ".-..-." : '"', ".----." : "'", "-...-" : ":", "-.--.-" : ")", "-.--." : "("  
}

NUMBERS = "0123456789"


folder_path_input = sys.argv[1]
folder_path_output = sys.argv[2]
list_of_files = os.listdir(folder_path_input)


for file_name in list_of_files:
     x = file_name.find(".", 1)
     output_file_name = file_name[:x] + "_v26161ns" + file_name[x:] 
     full_path_input = os.path.abspath(os.path.join(folder_path_input, file_name))
     full_path_output = os.path.abspath(os.path.join(folder_path_output, output_file_name))

     with open(full_path_input, "r") as myFile:
          text = myFile.read()
          result = text.split(":")

     identifier = result[0].upper()
     encoded_message = result[1].rstrip()

     #DECODING HEX
     if identifier == "HEX":
          hexstring = encoded_message
          decoded_message = bytes.fromhex(hexstring)
          decoded_message = decoded_message.decode("ascii")
          decoded_message = decoded_message.lower()

     #DECODING MORSE CODE
     if identifier == "MORSE CODE":

          encoded_message += " "
          temp = ""
          decoded_message= ""

          for char in encoded_message:
               if char != " ":
                    temp += char
               else:
                    if temp == "/":
                         decoded_message = decoded_message + " "
                         temp = ""
                    else:
                         decoded_message = decoded_message + MORSE_CODE_TO_ALPHABET[temp]
                         temp = ""


     #DECODING CEASER CIPHER +3
     if identifier == "CAESAR CIPHER(+3)":
          encoded_message_pos = 0
          decoded_message = ""
          alphabet = "xyzabcdefghijklmnopqrstuvwxyz"

          while(encoded_message_pos < len(encoded_message)):
               encoded_message_char = encoded_message[encoded_message_pos]
               if encoded_message_char == " ":
                    decoded_message += " "
                    encoded_message_pos += 1
                    continue

               elif encoded_message_char in NUMBERS:
                    decoded_message += encoded_message_char
                    encoded_message_pos += 1
                    continue
                    
               alphabet_pos = 3
               while encoded_message_char != alphabet[alphabet_pos]:
                    alphabet_pos += 1

               alphabet_pos = alphabet_pos - 3
               decoded_message += alphabet[alphabet_pos]
               encoded_message_pos += 1

     with open(full_path_output, "w") as wf:    
          wf.write(decoded_message)
