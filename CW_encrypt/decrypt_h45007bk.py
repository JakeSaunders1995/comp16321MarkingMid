def main(input_filepath,output_filepath):

    #init dict for morse code lookup
    morse_dict={
        '.-': 'A',
        '-...': 'B',
        '-.-.':'C',
        '-..':'D',
        '.':'E',
        '..-.':'F',
        '--.':'G',
        '....':'H',
        '..':'I',
        '.---':'J',
        '-.-':'K',
        '.-..':'L',
        '--':'M',
        '-.':'N',
        '---':'O',
        '.--.':'P',
        '--.-':'Q',
        '.-.':'R',
        '...':'S',
        '-':'T',
        '..-':'U',
        '...-':'V',
        '.--':'W',
        '-..-':'X',
        '-.--':'Y',
        '--..':'Z',
        '-----':'0',
        '.----':'1',
        '..---':'2',
        '...--':'3',
        '....-':'4',
        '.....':'5',
        '-....':'6',
        '--...':'7',
        '---..':'8',
        '----.':'9',
        '.-...':'&',
        '.----.':'\'',
        '.--.-.':'@',
        '-.--.-':')',
        '-.--.':'(',
        '---...':':',
        '--..--':',',
        '-...-':'=',
        '-.-.--':'!',
        '.-.-.-':'.',
        '-....-':'-',
        #MULTIPLICATION SIGN * NOT INCLUDED BECAUSE SAME AS X
        '------..-.-----':'%',
        '.-.-.':'+',
        '.-..-.':'"',
        '..--..':'?',
        '-..-.':'/'
    }

    file=open(input_filepath)
    ciphertext=file.read().strip()
    plaintext=''

    if ciphertext[0:3]=='Hex':
        ciphertext=ciphertext[4:]+' ' #added space so gets last hex code in the loop as of form 'xx '
        for i in range(0,len(ciphertext),3):
            assert ciphertext[i+2]==' ', 'Ciphertext in wrong format: missing whitespace'
            chr_hex=int(ciphertext[i:i+2],base=16)
            plaintext+=chr(chr_hex)

    elif ciphertext[0:10]=='Morse Code': #note / is used as a space, otherwise - . and space for end of letter
        ciphertext=ciphertext[11:]+' '#add space for morse word to end and lookup
        morse_word=''
        for chr_morse in ciphertext:
            if chr_morse=='-' or chr_morse=='.':
                morse_word+=chr_morse
            elif chr_morse=='/':
                plaintext+=' '
            elif chr_morse==' ':
                if morse_word!='':
                    plaintext+=morse_dict[morse_word]
                    morse_word=''

    elif ciphertext[0:17]=='Caesar Cipher(+3)':
        ciphertext=ciphertext[18:]
        for chr_crypt in ciphertext:
            if 'a'<=chr_crypt<='z' or 'A'<=chr_crypt<='Z':
                chr_crypt=ord(chr_crypt)-3
                if ord('Z')<chr_crypt<ord('a') or chr_crypt<ord('A'):
                    chr_crypt+=26
                chr_crypt=chr(chr_crypt)
            plaintext+=chr_crypt

    plaintext=plaintext.lower()
    file=open(output_filepath,'w')
    file.write(plaintext)
    file.close()

#--------

#to iterate over txt files in a directory, (non recusrively)
#or just files if given paths to files

import argparse, os
parser=argparse.ArgumentParser(description="Script to decrypt files that are encrypted with morse code, caesar +3, or hexadecimal")
parser.add_argument('input_path',type=str,help="Input path to file or folder")
parser.add_argument('output_path',type=str,help="Output path to file or folder")

args=parser.parse_args()

username='_h45007bk'

def dir_txtlist(dirpath):
	f_list=[]
	for f_obj in os.scandir(dirpath):
		if f_obj.is_file(follow_symlinks=True):
			f_list.append(f_obj.path)
	return f_list

if not os.path.exists(args.input_path):
	print("Error: cannot access or find the input path at this time.")
	exit()

if os.path.isdir(args.input_path):
	if not os.path.exists(args.output_path):
		os.makedirs(args.output_path)
	if os.path.isdir(args.output_path):
		fin_lst=dir_txtlist(args.input_path)
		for fileout in fin_lst:
			fout=os.path.join(args.output_path,os.path.basename(fileout))
			ext_i=fout.rfind('.')
			fout=fout[:ext_i]+username+fout[ext_i:]
			fin=os.path.join(args.input_path,os.path.basename(fileout))
			main(fin, fout)
	else:
		print('Error: output path must be to a directory if the input path is also to a directory')
		exit()
elif os.path.isfile(args.input_path):
	if os.path.isdir(args.output_path):
		fout=os.path.join(args.output_path,os.path.basename(args.input_path))
		ext_i=fout.rfind('.')
		fout=fout[:ext_i]+username+fout[ext_i:]
		main(args.input_path, fout)
	elif os.path.isfile(args.output_path) or (not os.path.exists(args.output_path)):
		main(args.input_path, args.output_path)

else:
	print("Error: provided path(s) are not to a file or directory")
	exit()