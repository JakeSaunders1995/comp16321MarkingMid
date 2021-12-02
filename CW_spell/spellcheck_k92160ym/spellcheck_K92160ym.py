import re,argparse,os

parser=argparse.ArgumentParser(description="Check the spelling in a text")
parser.add_argument("dir" , nargs="+")
args=parser.parse_args()
files=os.listdir(args.dir[1])

for i in range (0,len(files)):
	name=files[i].replace(".txt","")
	name_file=args.dir[1]+"/"+files[i]
	result_file=open(name_file,"r")
	text=result_file.read()
	print(args.dir[0])

	pathDict=args.dir[0]+"/EnglishWords.txt"


	with open(pathDict,"r") as f:
		dict=f.read()

		
	num="0123456789"
	punctuations = '''!()-[]{};:'",<>./?@#$%^&*_~'''

	result=[]
	nombre_des_num=0
	remove_numbre=""
	for char in text:
		
		if char not in num:
			remove_numbre=remove_numbre + char
			
		
		else:
			nombre_des_num+=1


	numberOfPunct=0
	remove_punct=""
	for char in remove_numbre:
		if char not in punctuations:
			remove_punct=remove_punct + char
		else:
			numberOfPunct+=1



	nbofUpperChar=0			
	charec=""		
	for char in remove_punct:
		
		if char.isupper():
			char=char.lower() 
			charec=charec + char
			nbofUpperChar+=1
		else:
			charec=charec + char


	correctWords=0
	incorrectWords=0
	words_check=charec.split(" ")



	for word in words_check:
		if word in dict:
			correctWords+=1
		elif word not in dict:
			incorrectWords+=1
			
	totalWords=correctWords+incorrectWords


	Out_put="K92160ym \nFormatting ###################\nNumber of upper case words transformed:"+str(nbofUpperChar) +" \nNumber of punctuation’s removed:"+str(numberOfPunct)+" \nNumber of numbers removed:"+str(nombre_des_num)+" \nSpellchecking ###################\nNumber of words in file:"+str(totalWords) +"\nNumber of correct words in file:"+str(correctWords)+"\nNumber of incorrect words in file:"+str(incorrectWords)+""	


	appearfile=str(args.dir[2])+"/"+ name + "_K92160ym.txt"
	write_f=open(appearfile,"w")
	outcome=Out_put
	write_f.write(outcome) 