import argparse
import os
import re

parser = argparse.ArgumentParser()
# Create arguments
parser.add_argument("input_dir", help="A dirpath for the input cipher-text files")
parser.add_argument("output_dir", help="A dirpath for the output decrypted text files")

args = parser.parse_args()

input_dir = args.input_dir
output_dir = args.output_dir

# Make output directory if required
if not os.path.isdir(output_dir):
    os.makedirs(output_dir)

input_files = []
output_files = []
# Walk through input directory recursively to get files
for root, dirs, files in os.walk(input_dir):
    for name in files:
        # root will be relative or absolute depending on what was given as an arg
        input_files.append(os.path.join(root, name))
        # The slice assumes that the input filename ends in .txt
        output_files.append(os.path.join(output_dir, name[:-4] + "_p17498jw.txt"))

# Decryption mappings
morse_code = {'.-':'a', '-...':'b', '-.-.':'c', '-..':'d', '.':'e', '..-.':'f',
              '--.':'g', '....':'h', '..':'i', '.---':'j', '-.-':'k', '.-..':'l',
              '--':'m', '-.':'n', '---':'o', '.--.':'p', '--.-':'q', '.-.':'r',
              '...':'s', '-':'t', '..-':'u', '...-':'v', '.--':'w', '-..-':'x',
              '-.--':'y', '--..':'z', '-----':'0', '.----':'1', '..---':'2',
              '...--':'3', '....-':'4', '.....':'5', '-....':'6', '--...':'7',
              '---..':'8', '----.':'9'}
caesar_3 = "xyzabcdefghijklmnopqrstuvwxyz"


for i in range(0, len(input_files)):
    in_file = input_files[i]
    out_file = output_files[i]
    # Read cipher text from file - assume on first and only first line
    in_fh = open(in_file, "r")
    cipher_line = in_fh.readline()
    in_fh.close()

    # Split line into algorithm and ciphertext
    match = re.match(r"([a-zA-Z3()+ ]+):(.+)", cipher_line)
    algo = match.group(1)
    cipher_text = match.group(2)

    decrypted_line = ""
    # Decrypt cipher text according to algorithm
    if algo == "Morse Code":
        for char in cipher_text.split():
            if char == "/":
                decrypted_line += " "
            else:
                decrypted_line += morse_code[char]
    elif algo == "Hex":
        for char in cipher_text.split():
            # Convert from hex to ascii
            decrypted_line += bytearray.fromhex(char).decode().lower()
    elif algo == "Caesar Cipher(+3)":
        for char in cipher_text.lower():
            if char not in caesar_3:
                decrypted_line += char
            else:
                # Search caesar_3[3:] for char index, then substract 3
                decrypted_line += caesar_3[caesar_3.index(char, 3)-3]

    # Store decrypted text in output file
    out_fh = open(out_file, "w+")
    out_fh.write(decrypted_line)
    out_fh.close()
