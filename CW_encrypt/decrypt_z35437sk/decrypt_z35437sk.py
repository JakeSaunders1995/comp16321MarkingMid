#Welcome to Sambbhav's agency to decode the secret code
import argparse
import string
import sys
import codecs
import os 
def decoder(code):
    input_text=""
    for ch in code:
    	if(ch==':'):
    		break
    	input_text+=ch.lower()
    # print(input_text)
    index=code.index(":")
    in_code=code[index+1:]
    # print(in_code)
    remove=input_text.replace(" ","")
    # print(remove)
    decode=""
    if (input_text.translate(remove)<="ceasercipher(+3)"):
    	for ch in in_code:
    		if(ch==" "):
    			decode+=" "
    		if(ch=="a" or ch=="b" or ch=="c"):
    		    decode+=chr(ord(ch)-3+26)	
    		else:
    		    decode+=chr(ord(ch)-3)
    	return decode
    elif (input_text.translate(remove)<="hexadecimal"):
    	byte_array=bytearray.fromhex(in_code)
    	return byte_array.decode()
    elif (input_text.translate(remove)<="morsecode"):
    	in_code=in_code+" "
    	morse_letter=""
    	decoded_wrd=""
    	morse_decoder= {'.-':'A', '-...':'B','-.-.':'C', '-..':'D', '.':'E','..-.':'F', '--.':'G','....':'H','..':'I', '.---':'J','-.-':'K','.-..':'L','--':'M', '-.':'N','---':'O', '.--.':'P', '--.-':'Q','.-.':'R', '...':'S', '-':'T','..-':'U', '...-':'V', '.--':'W','-..-':'X', '-.--':'Y', '--..':'Z','.----':'1', '..---':'2', '...--':'3','....-':'4', '.....':'5', '-....':'6','--...':'7', '---..':'8', '----.':'9','-----':'0', '--..--':', ', '.-.-.-':'.','..--..':'?', '-..-.':'/', '-....-':'-','-.--.':'(', '-.--.-':')', '-.-.--':'!','---...':':'}
    	for ch in in_code:
        	if(ch!=' ' and ch!='/'):
        		morse_letter+=ch
        		
        	elif(ch=='/'):
        		decoded_wrd+=' '
        		morse_letter=''
        	elif(morse_letter!=''):
        			decoded_wrd+=morse_decoder[morse_letter].lower()
        			morse_letter=''
        			decode=decoded_wrd
    return decode
if __name__=="__main__":
	parser=argparse.ArgumentParser()
	parser.add_argument('input')
	parser.add_argument('output')
	args = parser.parse_args()
	st=str(args.input)
	st_out=str(args.output)
	l=os.listdir(st)
	l.sort()
	for filepath in l:
		f= os.path.join(st,filepath)
		pos_t=filepath.find(".txt")
		out_fname=filepath[0:pos_t]
		# print(f)
		with codecs.open(f, 'r', encoding='utf-8',errors='ignore') as fdata:
		  string=fdata.read()
		  result=decoder(string)  			
		  
		  with open(os.path.join(st_out,f'{out_fname}_z35437sk.txt'),"w") as file_writer:
		       # print(st_out)
		       file_writer.write(result)
