import argparse, os

def dir_path(string):
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)

parser = argparse.ArgumentParser()
parser.add_argument('input_folder', type=dir_path)
parser.add_argument('output_folder', type=dir_path)
folders = parser.parse_args()

for file in os.listdir(folders.input_folder):
    filepath = folders.input_folder + '/' + file
    input_file = open(filepath, 'r')
    input_file_contents = input_file.read()
    input_file.close()
    algorithm, ciphertext = input_file_contents.split(':')

    if algorithm == 'Hex':
        plaintext = bytearray.fromhex(ciphertext).decode().lower()

    elif algorithm == 'Caesar Cipher(+3)':
        plaintext = ''
        for char in ciphertext:
            if char.isalpha():
                char_ascii = ord(char)
                char_ascii = char_ascii - 3
                if char_ascii < 97:
                    char_ascii += 26
                char = chr(char_ascii)
            plaintext += char

    elif algorithm == 'Morse Code':
        plaintext = ''
        morse_dict = {
        '.-':'a', '-...':'b', '-.-.':'c', '-..':'d', '.':'e',
        '..-.':'f', '--.':'g', '....':'h', '..':'i', '.---':'j',
        '-.-':'k', '.-..':'l', '--':'m', '-.':'n', '---':'o',
        '.--.':'p', '--.-':'q', '.-.':'r', '...':'s', '-':'t',
        '..-':'u', '...-':'v', '.--':'w', '-..-':'x', '-.--':'y',
        '--..':'z', '.----':'1', '..---':'2', '...--':'3', '....-':'4',
        '.....':'5', '-....':'6', '--...':'7', '---..':'8', '----.':'9',
        '-----':'0', '--..--':',', '.-.-.-':'.', '..--..':'?', '.-..-.':'"',
        '-....-':'-', '---...':':', '.----.':"'", '-..-.':'/', '-.--.':'(',
        '-.--.-':')'
        }
        morse_list = ciphertext.split('/')
        for morse_word in morse_list:
            morse_word = morse_word.split()
            for morse in morse_word:
                plaintext += morse_dict[morse]
            plaintext += ' '
        plaintext = plaintext[0:len(plaintext) - 1] # There will be an extra space at the end otherwise

    filename = os.fsdecode(file)
    filename = filename.replace('.txt', '')
    filename += '_h37701dk.txt'
    output_filepath = folders.output_folder + '/' + filename
    output_file = open(output_filepath, 'w+')
    output_file.write(plaintext)
    output_file.close()
