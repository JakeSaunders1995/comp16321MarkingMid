import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("input_folder", type=str)
parser.add_argument("output_folder", type=str)
args = parser.parse_args()


Morse_decode_map = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G',
                    '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N',
                    '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U',
                    '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '.----': '1',
                    '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7',
                    '---..': '8  ', '----.': '9', '-----': '0', '--..--': ',', '.-.-.-': '.', '..--..': '?',
                    '-..-.': '/', '-....-': '-', '-.--.': '(', '-.--.-': ')', '/': ' '}
Caesar_Cipher_decode_map = {'a': 'x', 'b': 'y', 'c': 'z', 'd': 'a', 'e': 'b', 'f': 'c', 'g': 'd', 'h': 'e',
                            'i': 'f', 'j': 'g', 'k': 'h',
                            'l': 'i', 'm': 'j', 'n': 'k', 'o': 'l', 'p': 'm', 'q': 'n', 'r': 'o', 's': 'p',
                            't': 'q', 'u': 'r', 'v': 's',
                            'w': 't', 'x': 'u', 'y': 'v', 'z': 'w'}
Hex_decode_map = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "a": 10, "b": 11,
                  "c": 12, "d": 13, "e": 14, "f": 15}


def Decode_Str(input_data: list, decode_map: dict, decode_type):
    decode_str = ""
    input_data_valid = input_data[1].split(" ")
    for index, element in enumerate(input_data_valid):
        if decode_type == 1:
            decode_str += chr(decode_map[element[0]] * 16 + decode_map[element[1]])
        elif decode_type == 2:
            end_str = "" if index == len(input_data_valid) - 1 else " "
            decode_str += "".join([decode_map[ele] for ele in element]) + end_str
        elif decode_type == 3:
            decode_str += decode_map[element]
    return decode_str.lower()


def main():
    all_txt_files = os.listdir(args.input_folder)
    for txt_file in all_txt_files:
        path = os.path.join(args.input_folder, txt_file)
        with open(path, 'r') as f:
            file_text = f.read()
        file_text = file_text.strip().split(':')
        decode_map = {}
        decode_type = 0
        if file_text[0] == "Hex":
            decode_map = Hex_decode_map
            decode_type = 1
        elif file_text[0] == "Caesar Cipher(+3)":
            decode_map = Caesar_Cipher_decode_map
            decode_type = 2
        elif file_text[0] == "Morse Code":
            decode_map = Morse_decode_map
            decode_type = 3
        decode_str = Decode_Str(file_text, decode_map, decode_type)
        out_path = os.path.join(args.output_folder, txt_file[:-4] + "_[s86124sy].txt")
        with open(out_path, 'w') as f:
            f.write(decode_str)

if __name__ == '__main__':
    main()
# python decrypt[s86124sy].py ./midterm_files/Example_inputs/Example_inputs_program2 ./midterm_files/Example_outputs/Example_outputs_program2

