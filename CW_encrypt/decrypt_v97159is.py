import argparse

my_parser = argparse.ArgumentParser()
my_parser.add_argument('binary_file', type = argparse.FileType('r'))
my_parser.add_argument('output_file', type= argparse.FileType('w'))
args = vars(my_parser.parse_args())

if args['binary_file']:
	data = args['binary_file'].read()
part = data.split(':')
algorithm = part[0]
ciphertext = part[1]
plaintext = ""


if algorithm == 'Hex':
	for hex_digit in ciphertext.split():
		integer_value = int(hex_digit,16)
		ascii = chr(integer_value)
		plaintext += ascii

elif algorithm == 'Caesar Cipher(+3)':
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	newCharacter = 0
	for i in ciphertext:
		if i.lower() in alphabet:
			newCharacter = alphabet.index(i) - 3
			plaintext += alphabet[newCharacter %26]
		else: 
			plaintext += i
elif algorithm == 'Morse Code':
	morse_to_eng = {
    	'....' : 'h', '.-' : 'a', '-...' : 'b', '-.-.' : 'c', '-..' : 'd', '.' : 'e', '..-.' : 'f', '--.' : 'g', '..' : 'i', '.---' : 'j', '-.-' : 'k', '.-..' : 'l', '--' : 'm', '-.' : 'n', '---' : 'o', '.--.' : 'p', '--.-' : 'q', '.-.' : 'r', '...' : 's', '-' : 't', '..-' : 'u', '...-' : 'v', '.--' : 'w', '-..-' : 'x', '-.--' : 'y', '--..' : 'z', '.-.-.-' : '.', '..--..' : '?', '--..--' : ',', '/' : ' '
	}
	words = ''
	for i in ciphertext.split():
		if i != '/':
			plaintext += morse_to_eng[i]
		else:
			plaintext += ' '
			

print(plaintext)

args['output_file'].write(plaintext)
