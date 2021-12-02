import argparse, os

myparser = argparse.ArgumentParser(description='Rugby score calculator')

myparser.add_argument('input_file_path')
myparser.add_argument('output_file_path')

args = myparser.parse_args()

input_path = args.input_file_path
output_path = args.output_file_path

for file in os.listdir(input_path):
    with open(os.path.join(input_path, file), 'r') as f:
        fileText = f.read()
        filename = os.path.basename(f.name)[:-4]

    morsecode_dict = {'.-' : 'a', '-...' : 'b', '-.-.' : 'c', '-..' : 'd', '.' : 'e', '..-.' : 'f', '--.' : 'g', '....' : 'h', '..' : 'i', '.---' : 'j', '-.-' : 'k', '.-..' : 'l', '--' : 'm', '-.' : 'n', '---' : 'o', '.--.' : 'p', '--.-' : 'q', '.-.' : 'r', '...' : 's', '-' : 't', '..-' : 'u', '...-' : 'v', '.--' : 'w', '-..-' : 'x', '-.--' : 'y', '--..' : 'z', '.-.-.-' : '.', '..--..' : '?', '--..--' : ',', '/' : ' '}

    algorithmType, cipherText = fileText.split(':', 1)[0], fileText.split(':', 1)[1]

    if algorithmType == "Hex":
        plaintext = bytearray.fromhex(cipherText).decode().lower()
    elif algorithmType == "Caesar Cipher(+3)":
        plaintext = ""
        for char in cipherText:
            if ord(char) == 32:
                plaintext += ' '
            elif ord(char) == 10:
                plaintext += '\n'
            else:
                newValue = ord(char) - 3
                if newValue < ord('a'):
                    newValue += 26
                plaintext += chr(newValue)
    elif algorithmType == "Morse Code":
        plaintext = ""
        characters = cipherText.split(' ')
        for char in characters:
            if char != '/':
                plaintext += morsecode_dict[char]
            else:
                plaintext += ' '

    output_filename = filename + "_h06023jc.txt"

    with open(os.path.join(output_path, output_filename),'w',encoding='utf-8') as f:
        f.write(plaintext.lower())