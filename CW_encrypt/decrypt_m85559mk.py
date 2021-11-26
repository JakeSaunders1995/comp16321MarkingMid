import argparse
import os

def decrypt_ceaser(string, shift):
    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
    output_string = ""
    for letter in string:
        if letter in lowercase_letters:
            output_string += lowercase_letters[lowercase_letters.index(letter) - shift]
        else:
            output_string += letter
    return output_string

def decrypt_morse(string):
    code_dictionary = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9'}
    output_string = ""
    character_list = string.split()
    for character in character_list:
        if character in code_dictionary.keys():
            output_string += code_dictionary[character]
        elif character == "/":
            output_string += " "

    return output_string

def decrypt_hex(string):
    characters = string.split(" ")
    output_text = ""
    for character in characters:
        output_text += chr(int(character, 16))

    return output_text

#Returns a tuple of the input folder and the output folder
def get_io_folders():
    my_parser = argparse.ArgumentParser()
    my_parser.add_argument("input_folder")
    my_parser.add_argument("output_folder")
    args = my_parser.parse_args()

    return args.input_folder, args.output_folder

def get_output_filename(input_filename, username):
    txt_removed = input_filename.split(".")[0]
    return f'{txt_removed}_{username}.txt'

def get_decryptor_and_decrypt(input_string):
    if input_string[0] == "C":
        return decrypt_ceaser(input_string[18:], 3)
    elif input_string[0] == "H":
        return decrypt_hex(input_string[4:])
    else:
        return decrypt_morse(input_string[11:])


def main():
    input_folder, output_folder = get_io_folders()
    #Creates the output path if it does not already exist
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    for filename in os.scandir(input_folder):
        with open(filename.path, 'r') as f:
            input_string = f.read()
        output_file_path = os.path.join(output_folder, get_output_filename(filename.name, 'm85559mk'))
        with open(output_file_path, "w+") as f:
            f.write(get_decryptor_and_decrypt(input_string))


main()