import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("input_folder_path")
parser.add_argument("output_folder_path")

def decrypt_hex(encrypted_message):
    message = [chr(int(letter, 16)) for letter in encrypted_message.split(' ')]
    return "".join(message)

def decrypt_morse(encrypted_message):
    morse_table = {
        ".-": "a",
        "-...": "b",
        "-.-.": "c",
        "-..": "d",
        ".": "e",
        "..-.": "f",
        "--.": "g",
        "....": "h",
        "..": "i",
        ".---": "j",
        "-.-": "k",
        ".-..": "l",
        "--": "m",
        "-.": "n",
        "---": "o",
        ".--.": "p",
        "--.-": "q",
        ".-.": "r",
        "...": "s",
        "-": "t",
        "..-": "u",
        "...-": "v",
        ".--": "w",
        "-..-": "x",
        "-.--": "y",
        "--..": "z",
        "-----": "0",
        ".----": "1",
        "..---": "2",
        "...--": "3",
        "....-": "4",
        ".....": "5",
        "-....": "6",
        "--...": "7",
        "---..": "8",
        "----.": "9"
    }
    words = []
    for word in encrypted_message.split('/'):
        letters = [morse_table[letter] for letter in word.split(' ') if len(letter)]
        words.append("".join(letters))

    return " ".join(words)

def decrypt_caesar_plus3(encrypted_message):
    alphabet = 'xyzabcdefghijklmnopqrstuvw'
    words = []
    for word in encrypted_message.split(" "):
        new_word = [alphabet[ord(letter) - ord('a')] for letter in word]
        words.append("".join(new_word))
    
    return " ".join(words)

def decrypt(encrypted_message):
    pos = encrypted_message.find(':')
    modality = encrypted_message[:pos]
    message = encrypted_message[pos + 1:]

    functions = {
        'Hex': decrypt_hex,
        'Caesar Cipher(+3)': decrypt_caesar_plus3,
        'Morse Code': decrypt_morse
    }
    message = functions[modality](message)
    return message

def main():
    args = parser.parse_args()

    for file_name in os.listdir(args.input_folder_path):
        if file_name.endswith('.txt'):
            # read file contents
            input_file_path = os.path.join(args.input_folder_path, file_name)
            with open(input_file_path) as f:
                encrypted_message = f.read().strip('\n')

            # solve problem
            message = decrypt(encrypted_message)

            # write results
            output_file_name = file_name[:-4] + '_m18453ab.txt'
            output_file_path = os.path.join(args.output_folder_path, output_file_name)
            with open(output_file_path, 'w') as f:
                f.write(message)


if __name__ == "__main__":
    main()