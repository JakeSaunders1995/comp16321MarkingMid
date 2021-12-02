import argparse
import os

def get_output_file_name(filename, username):
	before_txt = filename.split('.')[0]
	return before_txt + '_' + username + '.txt'

if __name__=="__main__":

	parser=argparse.ArgumentParser()
	parser.add_argument('input')
	parser.add_argument('output')
	args=parser.parse_args()
var = str(args.input)
out=str(args.output)
m=os.scandir(var)
for filepath in m:
	f=os.path.join(var,filepath)
	string=open(filepath, 'r') 
	string=string.read()

	morse_reverse={'..-.': 'F', '-..-': 'X',
	                 '.--.': 'P', '-': 'T', '..---': '2',
	                 '....-': '4', '-----': '0', '--...': '7',
	                 '...-': 'V', '-.-.': 'C', '.': 'E', '.---': 'J',
	                 '---': 'O', '-.-': 'K', '----.': '9', '..': 'I',
	                 '.-..': 'L', '.....': '5', '...--': '3', '-.--': 'Y',
	                 '-....': '6', '.--': 'W', '....': 'H', '-.': 'N', '.-.': 'R',
	                 '-...': 'B', '---..': '8', '--..': 'Z', '-..': 'D', '--.-': 'Q',
	                 '--.': 'G', '--': 'M', '..-': 'U', '.-': 'A', '...': 'S', '.----': '1','/':' ','.----' : '1','..---' : '2','...--' : '3','....-' : '4','.....' : '5','-....' : '6','--...' : '7','---..' : '8','----.' : '9','-----' : '0','--..--' : ', ','.-.-.-' : '.','..--..' : '?','-..-.' : '/','-....-' : '-','-.--.' : '(','-.--.-' : ')'}

	
	message=""
	if string.startswith('Hex'):
		sub=string[4:]
		message=bytes.fromhex(sub).decode('utf-8')

	elif string.startswith('Caesar'):
		alphabets="xyzabcdefghijklmnopqrstuvwxyz"
		sub=string[18:]
		length=len(sub)
		i=0
		lenalpha=len(alphabets)
		while i<length :
			character=sub[i]
			if character==' ':
				message=message+" "
			j=4
			while j<lenalpha:
				
				if alphabets[j]==character :
					k=j-3
					cipherchar=alphabets[k]
					message=message+cipherchar
				j=j+1;
			i=i+1

	elif string.startswith('Morse'):
		cutstring=string[11:]
		cutstring=cutstring+" "
		length=len(cutstring)
		i=0
		pos=0
		while i<length:
			
			if cutstring[i]==' ':
				sub=cutstring[pos:i]
				pos=i+1
				for x,y in morse_reverse.items():
					if x==sub :
						message=message+y

			i=i+1
			
		message=message.lower()

	output_file = os.path.join(args.output, get_output_file_name(filepath.name, 'h76117sv'))
	with open(output_file,'w+') as file:
		file.write(message)
