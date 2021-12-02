import os
import sys


command_line_arguments = sys.argv
input_directory_name = command_line_arguments[1][2:]
output_directory_name = command_line_arguments[2][2:]

morse_dictionary = {
".-" : "a", "-...": "b", "-.-.": "c",
"-.." : "d", ".": "e", "..-.": "f",
"--." : "g", "....": "h", "..": "i",
".---" : "j", "-.-": "k", ".-..": "l",
"--" : "m", "-.": "n", "---": "o",
".--." : "p", "--.-": "q", ".-.": "r",
"..." : "s", "-": "t", "..-": "u",
"...-" : "v", ".--": "w", "-..-": "x",
"-.--" : "y", "--..": "z", ".----": "1",
"..---" : "2", "...--": "3", "....-": "4",
"....." : "5", "-....": "6", "--...": "7",
"---.." : "8", "----.": "9", "-----": "0"
}


# ---- Main Body of Execution

def execute(inputs, output_path):
  for file in inputs:
    input_data = extract_input_data_from_filename(file).split(':')
    encryption_type = input_data[0]
    data = input_data[1]
    decrypted_text = decrypt(encryption_type, data)
    output_filename = create_empty_file(output_path, file)
    write_data_to_file(decrypted_text, output_filename)
    print("Successfully decoded message from " + str(file) + ".")

def decrypt(encryption, data):
    plaintext = ''

    if(encryption == "Hex"):
        plaintext = decrypt_hex(data)
    elif(encryption == "Morse Code"):
        plaintext = decrypt_morse(data)
    elif(encryption == "Caesar Cipher(+3)"):
        plaintext = decrypt_caesar(data)
    else:
        raise ValueError('Unknown encryption type.')

    return plaintext

# ---- File Operations

def extract_input_data_from_filename(input_filename):
    file = open('./' + input_directory_name + '/' + input_filename, 'r')
    data = file.read()

    if (data[-2:] == '\n'):
        data = data[:-2]

    file.close()
    return data


def create_empty_file(location, input_filename):
    new_filename = input_filename[:-4] + '-prog-2-output.txt'
    open('./' + location + '/' + new_filename, 'x').close()
    return new_filename


def get_filenames_from_input_directory(directory_name):
  directory_contents = os.listdir('./' + directory_name)
  files = []

  for item in directory_contents:
    if(item[-4:] == '.txt'):
        files.append(item)

  return files


def write_data_to_file(data, filename):
    output_file = open('./' + output_directory_name + '/' + filename, 'w')

    output_file.write(data)

    output_file.close()
    return


# ---- Data Processing

def decrypt_hex(data):
    plaintext = ""
    hex_characters = data.split(" ")

    for character in hex_characters:
      plaintext += chr(int(character, 16))

    return plaintext.lower()


def decrypt_morse(data):
    plaintext = ""
    morse_words = data.split(" / ")

    for word in morse_words:
        morse_characters = word.split(" ")
        for character in morse_characters:
            plaintext += morse_dictionary[character]
        plaintext += " "

    return plaintext.lower()


def decrypt_caesar(data):
    plaintext = ""
    caesar_words = data.split(" ")
    wrapping_character_map = {"a": "x", "b": "y", "c": "z"}

    for word in caesar_words:
        for i in word:
            if i not in ["a", "b", "c"]:
                plaintext += chr(ord(i)-3)
            else:
                plaintext += wrapping_character_map[i]
        plaintext += " "

    return plaintext.lower()


# ---- Actual Execution

print(decrypt_hex("74 65 73 74 20 64 61 74 61")) # "test data"
print(decrypt_morse("- . ... - / -.. .- - .-"))  # "test data"
print(decrypt_caesar("whvw gdwd")) # "test data"

execute(get_filenames_from_input_directory(input_directory_name), output_directory_name)
