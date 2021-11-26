import sys
import re
import os

input_directory = sys.argv[1]

for input_file in os.listdir(input_directory):
    with open(os.path.join(input_directory, input_file), "r") as file:

        encryption = file.read()

        if len(re.findall("Hex|hex", encryption)) > 0:
            print("Hexadecimal")
            hex_list = re.findall("[0-9]+[a-z]|[0-9]+[0-9]", encryption)
            hex_string = "".join(hex_list)
            a_string = bytes.fromhex(str(hex_string))
            a_string = a_string.decode("utf-8")

            output_directory = sys.argv[2]
            output_file = output_directory + "/" + input_file[0:-4] + "_d03963st.txt"
            with open(output_file, "w+") as f:
                f.write(a_string.lower())

        if len(re.findall("Caesar Cipher|caesar cipher", encryption)) > 0:
            print("Caesar +3")
            num = int((encryption.find(":"))) + 1
            plaintext = encryption[num:]
            cipher_text = ""
            plaintext_position = 0
            while (plaintext_position < len(plaintext)):
                plaintext_char = plaintext[plaintext_position]
                ascii_value = ord(plaintext_char)
                if ascii_value == 32:
                    cipher_text = cipher_text + " "
                else:
                    if ascii_value < 100:
                        ascii_value = ascii_value + 23
                        cipher_text = cipher_text + chr(ascii_value)
                    else:
                        ascii_value = ascii_value - 3
                        cipher_text = cipher_text + chr(ascii_value)
                plaintext_position = plaintext_position + 1

            output_directory = sys.argv[2]
            output_file = output_directory + "/" + input_file[0:-4] + "_d03963st.txt"
            with open(output_file, "w+") as f:
                f.write(cipher_text)

        if len(re.findall("Morse Code|morse code", encryption)) > 0:
            print("Morse Code")
            num = int((encryption.find(":"))) + 1
            morse_str = encryption[num:]
            morse_lst = morse_str.split()

            morse_dict = {".-":"a", "-...":"b",
                    "-.-.":"c", "-..":"d", ".":"e",
                    "..-.":"f", "--.":"g", "....":"h",
                    "..":"i", ".---":"j", "-.-":"k",
                    ".-..":"l", "--":"m", "-.":"n",
                    "---":"o", ".--.":"p", "--.-":"q",
                    ".-.":"r", "...":"s", "-":"t",
                    "..-":"u", "...-":"v", ".--":"w",
                    "-..-":"x", "-.--":"y", "--..":"z",
                    "/":" "}

            decrypted_morse = ""
            for letter in morse_lst:
                decrypted_morse = decrypted_morse + morse_dict.get(letter)

            output_directory = sys.argv[2]
            output_file = output_directory + "/" + input_file[0:-4] + "_d03963st.txt"
            with open(output_file, "w+") as f:
                f.write(decrypted_morse)
