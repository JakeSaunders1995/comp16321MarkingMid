import os, argparse

parser = argparse.ArgumentParser()
parser.add_argument("input_folder")
parser.add_argument("output_folder")

args = parser.parse_args()
input_folder = os.path.join(os.getcwd(), args.input_folder)
output_folder = os.path.join(os.getcwd(), args.output_folder)

if not os.path.isdir(output_folder):
    os.mkdir(output_folder)

morse = {
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
    "----.": "9",
    "/": " "  # To handle spaces between words
}


def decrypt_hex(ciphertext):
    return bytes.fromhex(ciphertext).decode().lower()


def decrypt_caesar(ciphertext):
    chars = [chr((num - 100) % 26 + 97) if chr(num).isalpha() else chr(num) for num in map(ord, ciphertext.lower())]
    return "".join(chars)


def decrypt_morse(ciphertext):
    return "".join(map(morse.get, ciphertext.split()))


encryption_types = {
    "Hex": decrypt_hex,
    "Caesar Cipher(+3)": decrypt_caesar,
    "Morse Code": decrypt_morse
}

for file in os.listdir(input_folder):
    with open(os.path.join(input_folder, file)) as f:
        text = f.read()

    encryption_type, ciphertext = text.split(":")
    plaintext = encryption_types.get(encryption_type)(ciphertext)

    filename, file_ext = os.path.splitext(file)
    new_file = filename + "_q00848wh" + file_ext
    with open(os.path.join(output_folder, new_file), "w") as f:
        f.write(plaintext)
