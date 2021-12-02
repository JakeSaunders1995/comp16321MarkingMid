import argparse
import os


obj = argparse.ArgumentParser()
obj.add_argument("input_folder", type=str, metavar='path')
obj.add_argument("output_folder", type=str, metavar='path')

args = obj.parse_args()


morse_translator = {'.-': 'a',   '-...': 'b',   '-.-.': 'c',
       '-..': 'd',      '.': 'e',   '..-.': 'f',
         '--.': 'g',   '....': 'h',     '..': 'i', 
      '.---': 'j',    '-.-': 'k',   '.-..': 'l',
        '--': 'm',     '-.': 'n',    '---': 'o', 
      '.--.': 'p',   '--.-': 'q',    '.-.': 'r',
       '...': 's',      '-': 't',    '..-': 'u', 
      '...-': 'v',    '.--': 'w',   '-..-': 'x',
      '-.--': 'y',   '--..': 'z',  '-----': '0', 
     '.----': '1',  '..---': '2',  '...--': '3',
     '....-': '4',  '.....': '5',  '-....': '6', 
     '--...': '7',  '---..': '8',  '----.': '9',
     '.-.-.-': '.',  '--..--': ',', '..--..': '?',
     '-.-.-.': ';',  '---...': ':',  '-....-': '-',
     '-..-.': '/',  '.----.': '\'',  '.-..-.': '\"',
     '-.--.': '(',  '-.--.-': ')',  '@': '.--.-.',
     '-.-.--': '!'}

for filename in os.listdir(args.input_folder):


	new_file = args.input_folder + '/' + filename
	file = open(new_file, 'r')

	line = file.read()
	file.close()

	if line[0].lower() == 'm':
		line = line + ' '
		data = line[11:]
		not_translated = []
		translated = []
		result = ''
		for i in range(len(data)):
			if data[i] == ' ': 
				result = ''.join(not_translated)
				translated.append(morse_translator.get(result))
				result = ''
				not_translated = []
			elif data[i] == '/':
				result = ''
				not_translated = []
			else: 
				not_translated.append(data[i])

		for i in range(len(translated)):
			if translated[i] == None:
				translated[i] = ' '

		result = ''.join(translated)
		result = result.lower()


	elif line[0].lower() == 'c':
		data = line[18:]
		shifted_data = []
		for i in range(len(data)):
			shifted_data.append(chr(ord(data[i]) - 3))

		for i in range(len(shifted_data)):
			if shifted_data[i] == '\x1d':
				shifted_data[i] = ' '
		result = ''.join(shifted_data)
		result = result.lower()


	elif line[0].lower() == 'h':
		data = line[4:]
		binary_format = bytes.fromhex(data.lower())
		result = binary_format.decode('ASCII')
		result = result.lower()


	new_output_file = filename.replace('.', '_c01724bh.')
	new_file = args.output_folder + '/' + new_output_file

	file = open(new_file, 'w')
	file.write(result)
	file.close()


