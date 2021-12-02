import os, argparse, re

args = None
textfile_pattern = None
# gets command line arguments and validates their format
def get_args():
	# take arguments from command line
	global args, textfile_pattern
	parser = argparse.ArgumentParser(description='Decrypts to plaintext given the ciphertext and type of encryption algorithm')
	parser.add_argument('inpath',help='directory containing only .txt files to read input from')
	parser.add_argument('outpath',help='directory to write .txt output files to')
	args = parser.parse_args()
	
	# prints an error and quits if the input folder doesn't exist, creates the output folder if it doesn't exist
	if not os.access(args.inpath,os.F_OK):
		print("Error: Input folder doesn't exist")
		raise SystemExit
	if not os.access(args.outpath,os.F_OK):
		os.mkdir(args.outpath)

	textfile_pattern = re.compile('^[a-zA-Z0-9_/~]+.txt$')

	# starts loop
	loop_files()


# loops through files in the given directory and performs the decryption on each one
def loop_files():
	# loops through files in the provided directory
	for file in os.listdir(args.inpath):
		# skips to the next file if the current file is not .txt
		if not textfile_pattern.search(file):
			continue
		# decrypts the current file and writes to the output file
		plaintext = get_algorithm(file)
		write_output(plaintext,file)


# gets the type of encryption algorithm used from the input file
def get_algorithm(file):
	# splits the input into an array by the colon
	with open(f'{args.inpath}/{file}') as f:
		cipher = f.read().split(':')
	# uses regular expressions to find the type of algorithm from the first part of the ciphertext
	algorithm_pattern = re.compile('caesar|morse|hex',re.I)
	algorithm= algorithm_pattern.search(cipher[0]).group()
	# gets the plaintext from the decryption function(s), makes sure its in lower case and returns
	plaintext = decrypt(algorithm,cipher[1]).lower()
	return plaintext
	

# selects the correct function to decrypt the given algorithm
def decrypt(algorithm, ciphertext):
	# uses eval to run the relevant decrypt algorithm and passes the ciphertext as a paramater
	plaintext = eval(algorithm.lower()+"_decrypt(ciphertext)")
	return plaintext


# decrypts a ciphertext in caesar +3 to plaintext
def caesar_decrypt(ciphertext):
	plaintext = ""
	# loops through all the characters in the ciphertext and replaces them with the character -3 ascii value (except space)
	for character in ciphertext:
		if character != " " and character != '\n':
			# cycles from start to end of the alphabet
			if character in 'abc':
				character = chr(ord(character)+26)
			character = chr(ord(character)-3)
		plaintext += character
	return plaintext


# decrypts a ciphertext in morse to plaintext
def morse_decrypt(ciphertext):
	# dictionary of all morse code definitions (latin letters, numbers and symbols) + '/' as space
	morse_dict = {
		# letters
		'.-':'a', '-...':'b', '-.-.':'c', '-..':'d', '.':'e',
		'..-.':'f' ,'--.':'g', '....':'h', '..':'i',
		'.---':'j', '-.-':'k', '.-..':'l', '--':'m', '-.':'n',
		'---':'o', '.--.':'p', '--.-':'q', '.-.':'r',
		'...':'s', '-':'t', '..-':'u', '...-':'v', '.--':'w',
		'-..-':'x', '-.--':'y', '--..':'z',
		# numbers
		'.----':'1', '..---':'2', '...--':'3', '....-':'4',
		'.....':'5', '-....':'6', '--...':'7', '---..':'8',
		'----.':'9', '-----':'0',
		# punctuation
		'.-.-.-':'.', '--..--':',', '..--..':'?',
		'.----.':"'", '-.-.--':'!', '-..-.':'/', '-.--.':'(',
		'-.--.-':')', '.-...':'&', '---...':':', '-.-.-.':';',
		'-,,,-':'=', '.-.-.':'+', '-....-':'-', '..--.-':'_',
		'.-..-.':'"', '...-..-':'$', '.--.-.':'@',
		# space - not morse, but matches input syntax
		'/':' '}

	cipher_array = ciphertext.split(' ')
	plaintext = ""
	# loops through all the morse codes and adds their translation to the plaintext
	for code in cipher_array:
		plaintext += morse_dict[code]
	return plaintext


# decrypts a ciphertext in hex to plaintext
def hex_decrypt(ciphertext):
	cipher_array = ciphertext.split(' ')
	plaintext = ""
	# loops through all the hex codes (split by space), converts them to ascii characters and adds to plaintext
	for code in cipher_array:
		plaintext += chr(int(code,16))
	return plaintext


# writes the plaintext to the output folder to a file with the same name as the input with username appended
def write_output(plaintext,file):
	with open(f'{args.outpath}/{file[:-4]}_w16910dg.txt','w') as f:
		f.write(plaintext)


# start program
get_args()
