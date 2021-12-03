import sys, re, os

map_the_code = { 
	'.-': 'a',
	'-...': 'b',
    '-.-.': 'c',
    '-..': 'd',
    '.': 'e',
    '..-.': 'f',
    '--.': 'g',
    '....': 'h',
    '..': 'i',
    '.---': 'j',
    '-.-': 'k',
    '.-..': 'l',
    '--': 'm',
    '-.': 'n',
    '---': 'o',
    '.--.': 'p',
    '--.-': 'q',
    '.-.': 'r',
    '...': 's',
    '-': 't',
    '..-': 'u',
    '...-': 'v',
    '.--': 'w',
    '-..-': 'x',
    '-.--': 'y',
    '--..': 'z',
    '/': ' ',
    '.----': '1', 
    '..---': '2',
    '...--': '3',
    '....-': '4',
    '.....': '5',
    '-....': '6',
    '--...': '7',
    '---..': '8',
    '----.': '9',
    '-----': '0',
    '.-.-.-':'.',
    '..--..':'?',
    '-.-.--':'!',
    '--..--':',',
    '---...':':',
    '-.-.-.':';',
    '-...-':'-',
    '-.--.':'(',
    '-.--.-':')',
    '.-..-.':'"',
    '.----.':"'",

}

input_folder = sys.argv[1]
output_folder = sys.argv[2]

if input_folder[-1] != "/":
	input_folder += "/"
if output_folder[-1] != "/":
	output_folder += "/"

input_files = os.listdir(input_folder)

for file in range(len(input_files)):
    input_file = open(input_folder + input_files[file], "r")
    # print(input_folder + input_files[file])
    input_file_contents = input_file.read()

    content = re.split(":", input_file_contents)

    enc_method, ciphered_text = content[0], content[1]
    decoded = ""

    if "hex" in enc_method.lower():
        decoded = bytearray.fromhex(ciphered_text).decode().lower()
    elif "caesar" in enc_method.lower():
        for character in ciphered_text:
            ciphered_text = ciphered_text.lower()
            if character == " " or character.isalpha() == False:
                decoded += character
            else:
                if ord(character) - 3 < ord('a'):
                    decoded += chr(ord(character) + 23)
                else:
                    decoded += chr(ord(character) - 3)
        if decoded[-1] == "!":
            decoded = decoded[0:-1]
    elif "morse" in enc_method.lower():
        ciphered_text_arr = ciphered_text.split(' ')
        for code in ciphered_text_arr:
            decoded += map_the_code[code]
    else:
        pass

    file_name = str(input_files[file]).replace('.txt', '')
    output_file_loc = output_folder + file_name + "_m17832wa.txt"
    output_file = open(output_file_loc, "w")
    output_file.write(decoded)

    output_file.close()