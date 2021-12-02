import argparse, os
# get folder names
parser = argparse.ArgumentParser()
parser.add_argument('input_folder')
parser.add_argument('output_folder')
args = parser.parse_args()

morse_lut = {
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
    '...-..-': '$',
    '.-...': '&',
    '..--.-': '_',
    '-...-': '=',
    '.-.-.': '+',
    '-..-.': '/',
    '.......': ' '
}

file_list = [i for i in os.listdir(args.input_folder) if os.path.isfile(f'{args.input_folder}/{i}')]

for file_name in file_list:
    # read input file
    f = open(f'{args.input_folder}/{file_name}')
    input_str = f.read()
    f.close()

    # get method and cipher-text
    str_part = input_str.split(':')
    method = str_part[0]
    encrypted_str = ":".join(str_part[1:])
    if method == 'Morse Code':
        output = ''
        words = [i.strip() for i in encrypted_str.split('/')]
        for i in range(len(words)):
            if i != 0:
                output += ' '
            chars = words[i].split(' ')
            for char in chars:
                if char in morse_lut:
                    output += morse_lut[char]
    elif method == 'Caesar Cipher(+3)':
        output = ""
        for char in encrypted_str:
            if ord(char) >= 65 and ord(char) <= 90: # upper case
                output += chr(divmod(ord(char)-65-3+26, 26)[1]+65)
            elif ord(char) >= 97 and ord(char) <= 122: # lower case
                output += chr(divmod(ord(char)-97-3+26, 26)[1]+97)
            else:
                output += char
    elif method == 'Hex':
        char_list = encrypted_str.split(' ')
        output = "".join([chr(int(i, 16)).lower() for i in char_list])

    # write output file
    if '.' in file_name:
        file_name_part = file_name.split('.')
        file_extension = file_name_part.pop(-1)
        new_file_name = f'{".".join(file_name_part)}_q17766yl.{file_extension}'
    else:
        new_file_name = f'{file_name}_q17766yl'
    f = open(f'{args.output_folder}/{new_file_name}', 'w')
    f.write(output)
    f.close()