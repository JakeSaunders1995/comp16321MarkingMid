import os, argparse, re

parser = argparse.ArgumentParser(description = 'get i/o files')
parser.add_argument("input_path")
parser.add_argument("output_path")
args = parser.parse_args()

full_input_path = os.path.join(os.getcwd(), args.input_path)
input_files = os.listdir(full_input_path)

full_output_path = os.path.join(os.getcwd(), args.output_path)

encrypted_inputs = [] # change per task
filenames_split = []
for input_filename in input_files:
    input_path = full_input_path + "/" + input_filename
    input_file = open(input_path, "r")
    encrypted_inputs.append(input_file.read()) # change per task
    input_file.close

    temp_file_split = re.split(".txt", input_filename)
    filenames_split.append(temp_file_split[0])

# find :
# slice either side
# if into encryption type
# decrypt

dict_morse = { '.-':'a', '-...':'b', '-.-.':'c', '-..':'d', 
                '.':'e', '..-.':'f', '--.':'g', '....':'h',
                '..':'i', '.---':'j', '-.-':'k', '.-..':'l', 
                '--':'m', '-.':'n', '---':'o', '.--.':'p', 
                '--.-':'q', '.-.':'r', '...':'s', '-':'t',
                '..-':'u', '...-':'v', '.--':'w', '-..-':'x', 
                '-.--':'y', '--..':'z', '/':' '}

file_num = 1
for encrypted_text in encrypted_inputs:
    split_text = re.split(":",encrypted_text)
    split_chars = str(split_text[1])

    encrypted_chars = re.split("\s", split_chars)

    pos_text = 0
    decrypted_text = ""
    if split_text[0] == "Hex":
        for en_char in encrypted_chars:
            de_char = bytes.fromhex(en_char)
            de_char = de_char.decode("ASCII")
            decrypted_text = decrypted_text + de_char
    elif split_text[0] == "Caesar Cipher(+3)":
        for en_word in encrypted_chars:
            for en_char in en_word:
                de_char = ord(en_char) - 3
                de_char = chr(de_char)
                decrypted_text = decrypted_text + de_char
            decrypted_text = decrypted_text + " "
    elif split_text[0] == "Morse Code":
        for en_char in encrypted_chars:
            de_char = dict_morse[en_char]
            decrypted_text = decrypted_text + de_char


    output_path = full_output_path + "/" + filenames_split[file_num - 1] + "_n72421tn.txt"
    decrypt_output = open(output_path, "w") 
    decrypt_output.write(decrypted_text) # change per task
    decrypt_output.close

    file_num = file_num + 1