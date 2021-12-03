import argparse , os

#Decryption Program 

parser = argparse.ArgumentParser(description='Takes messages from decrypted input files and outputs encryptions in new files')
parser.add_argument('inpath', help="Takes input path that contains decrypted files")
parser.add_argument('outpath', help="Saves decrypted messages in new files in the specified path")
args = parser.parse_args()

#Accessing Input Files
cwd = os.getcwd()
os.chdir(args.inpath) 

my_inputs = []
my_Outputs = []
def read_inputs(input_path):
    with open(input_path, 'r') as f:
        return f.read()
  

for file in os.listdir():
    if file.endswith(".txt"):
        input_path = os.path.join(os.getcwd(),file)
        my_Outputs.append(file)
        my_inputs.append(read_inputs(input_path))



#Program
#Morse Code Dictionary
morse = {'.-':'a', '-...':'b', '-.-.':'c', '-..':'d', '.':'e',
'..-.':'f', '--.':'g', '....':'h', '..':'i', '.---':'j', '-.-':'k', '.-..':'l', '--':'m', '-.':'n', '---':'o', '.--.':'p', '--.-':'q', '.-.':'r', '...':'s', '-':'t', '..-':'u', '...-':'v', '.--':'w', '-..-':'x', '-.--':'y', '--..':'z', '/':' ',
'.-.-.-':'.', '--..--':',', '..--..':'?', '-..-.':'/', '.--.-.':'@', '.----':'1', '..---':'2', '...--':'3', '....-':'4', '.....':'5', '-....':'6', '--...':'7', '---..':'8', '----.':'9', '-----':'0', '.---.':"'", '---...':":", '-.-.-.':";", '-....-':'-', '-.-.--':'!', '.-..-.':'"', '-.--.':'(', '-.--.-':')',
'.--...':'[', '-..---':']', '..--.':'{', '--..-':'}'}


#Determining Encryption Methods
enc_methods=[]

for y in range(0,len(my_inputs)):
	encm=""
	for i in range(0,len(my_inputs[y])):
		if(my_inputs[y][i] != ":"):
			encm+=my_inputs[y][i]
		else:
			break
	enc_methods.append(encm)
	#Removing literal method from messages
	my_inputs[y]= my_inputs[y].replace(enc_methods[y]+":","")


#Decryption Process
messages = []

for y in range(0,len(my_inputs)):
	decrypted_text = ""
	if(enc_methods[y] == "Hex" or enc_methods[y] == "hexadecimal"):
		bytes_object = bytes.fromhex(my_inputs[y])
		decrypted_text = bytes_object.decode("ASCII")
		messages.append(decrypted_text.lower())

	elif(enc_methods[y] == "Caesar Cipher(+3)" or enc_methods[y] == "caesar +3"):
		for i in my_inputs[y]:
			if(i != " "):
				i.lower()
				iuni_code = ord(i) - 3
				if(iuni_code < ord("a")):
					iuni_code +=3
					if(iuni_code == ord("a")):
						iuni_code = ord("x")
					elif(iuni_code == ord("b")):
						iuni_code = ord("y")
					elif(iuni_code == ord("c")):
						iuni_code = ord("z")

				decrypted_text += chr(iuni_code)
			else:
				decrypted_text += " "
		messages.append(decrypted_text.lower())

	elif(enc_methods[y] == "Morse Code" or enc_methods[y] == "morseCode"):
		word = ""
		my_inputs[y] += " "
		for i in my_inputs[y]:
			if(i != " "):
				word += i
			else:
				word = word.replace("\n","")
				decrypted_text += morse[word]
				word = ""
		messages.append(decrypted_text.lower())
			















#Creating Output File in the path specified in the 2nd argument
#Overwriting any existing file with same name

os.chdir(cwd)
os.chdir(args.outpath) 

for i in range(0, len(my_Outputs)):
    my_Outputs[i] = my_Outputs[i].replace(".txt","_x74657fa.txt")
    if(os.path.isfile(my_Outputs[i])):
        os.remove(my_Outputs[i])
    o = open(my_Outputs[i], "x")
    o.write(messages[i])

