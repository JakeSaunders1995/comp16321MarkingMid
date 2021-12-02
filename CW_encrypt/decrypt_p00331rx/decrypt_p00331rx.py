import argparse
import os

p00331rx = "p00331rx"
parser = argparse.ArgumentParser()
parser.add_argument("input_path",
                    default="./midterm_files/Example_inputs/Example_inputs_program1", type=str)
parser.add_argument("output_path",
                    default="./midterm_files/Example_outputs/Example_inputs_program1",
                    type=str)
args = parser.parse_args()

morse_covert_map = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G',
                    '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N',
                    '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U',
                    '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '.----': '1',
                    '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7',
                    '---..': '8  ', '----.': '9', '-----': '0', '--..--': ',', '.-.-.-': '.', '..--..': '?',
                    '-..-.': '/', '-....-': '-', '-.--.': '(', '-.--.-': ')', '/': ' '}

hex_map = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "A": 10, "B": 11,
           "C": 12, "D": 13, "E": 14, "F": 15}


def encrypt_the_string(data_text):
    line_message = data_text.split(":")
    message_type = line_message[0]
    message_data = line_message[1].split(" ")
    if message_type == "Hex":
        return encrypt_Hex(message_data)
    elif message_type == "Caesar Cipher(+3)":
        return encrypt_Caesar_Cipher(message_data)
    elif message_type == "Morse Code":
        return encrypt_Morse_Code(message_data)


def encrypt_Morse_Code(message_data):
    out_data = []
    for data in message_data:
        out_data.append(morse_covert_map[data])
    return "".join(out_data).lower()


def encrypt_Caesar_Cipher(message_data):
    out_data = []
    for data in message_data:
        word_list = []
        for char in data:
            ord_char = ord(char.lower()) - 3
            if ord_char == 96:
                ord_char = 122
            elif ord_char == 95:
                ord_char = 121
            elif ord_char == 94:
                ord_char = 120
            word_list.append(chr(ord_char))
        out_data.append("".join(word_list))
    return " ".join(out_data)


def encrypt_Hex(message_data):
    word_list = []
    for data in message_data:
        ord_num = hex_map[data[0].upper()] * 16 + hex_map[data[1].upper()]
        char = chr(ord_num)
        word_list.append(char)
    return "".join(word_list).lower()


def read_txt(file_path):
    # read data

    with open(file_path, "r") as f:
        data_line = f.read().strip()
    return data_line


def write_txt(file_path, encrypt_str):
    with open(file_path, "w") as f:
        f.write(encrypt_str)


def main():
    input_files = os.listdir(args.input_path)
    for file in input_files:
        file_path = os.path.join(args.input_path, file)
        file_datta = read_txt(file_path)
        out_str = encrypt_the_string(file_datta)
        out_file_path = os.path.join(args.output_path, file[:-4] + f"_{p00331rx}.txt")
        write_txt(out_file_path, out_str)


if __name__ == '__main__':
    main()
# python3 decrypt_p00331rx.py ./midterm_files/Example_inputs/Example_inputs_program2 ./midterm_files/Example_outputs/Example_outputs_program2

