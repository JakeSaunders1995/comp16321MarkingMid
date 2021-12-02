import sys
import os

path = sys.argv[1]
for file in os.listdir(path):
    file_path = os.path.join(os.getcwd(), path) + "/" + file
    if os.path.isfile(file_path):

        encrypted_file = open(file_path, 'r')
        encrypted_text = (encrypted_file.read())
        encrypted_file.close()

        encrypted_text_array = encrypted_text.split(":")

        if encrypted_text_array[0] == "Hex":

            encrypted_character_array = encrypted_text_array[1].split(" ")
            decrypted_text = ""
            for i in range(len(encrypted_character_array)):
                encrypted_character = encrypted_character_array[i]
                encrypted_character = int(encrypted_character, 16)
                decrypted_character = chr(encrypted_character)
                decrypted_text += decrypted_character
            decrypted_text = decrypted_text.lower()

        elif encrypted_text_array[0] == "Caesar Cipher(+3)":

            encrypted_character_array = []
            for character in encrypted_text_array[1]:
                if character == "\n":
                    pass
                else:
                    encrypted_character_array.append(character)
                print(encrypted_character_array)
            decrypted_text = ""
            encrypted_text_position = 0
            while (encrypted_text_position < len(encrypted_character_array)):
                encrypted_text_char = encrypted_character_array[encrypted_text_position]
                ASCII_Value = ord(encrypted_text_char)
                ASCII_Value -= 3
                if encrypted_text_char == " ":
                    decrypted_text += " "
                elif encrypted_text_char == "a":
                    decrypted_text += "x"
                elif encrypted_text_char == "b":
                    decrypted_text += "y"
                elif encrypted_text_char == "c":
                    decrypted_text += "z"
                else:
                    decrypted_text += chr(ASCII_Value)
                encrypted_text_position += 1

        elif encrypted_text_array[0] == "Morse Code":

            character_list = "abcdefghijklmnopqrstuvwxyz"
            morse_code_list = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..",
            ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-",
            "...-", ".--", "-..-", "-.--", "--.."]
            encrypted_word_array = encrypted_text_array[1].split(" / ")
            encrypted_character_array = []
            for word in encrypted_word_array:
                encrypted_character_array += word.split(" ")
                encrypted_character_array += " "
            encrypted_character_array.pop()

            decrypted_text = ""
            for character in encrypted_character_array:
                if character == " ":
                    decrypted_text += " "
                else:
                    index_encrypted_character = morse_code_list.index(character)
                    decrypted_text += character_list[index_encrypted_character]

        else:
            pass

        output_file_name = os.path.join(os.getcwd(), sys.argv[2]) + "/" + file[:-4] + "_f92301jb.txt"
        output_file = open(output_file_name, "w")
        output_file.write(decrypted_text)
        output_file.close()
