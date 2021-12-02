import argparse
import os

try:
	parser=argparse.ArgumentParser()
	parser.add_argument("eng_dict", help="English words dictionary file path", type=str)
	parser.add_argument("inputFolder", help="input folder path", type=str)
	parser.add_argument("outputFolder", help="output folder path", type=str)
	files=parser.parse_args()

	fol_in=files.inputFolder
	fol_out=files.outputFolder

	input_files=os.listdir(fol_in)

	for file in input_files:

		English_dict=open(files.eng_dict)
		f_in=open(fol_in + "/" + file)
		output_file = file.rstrip(".txt")+"_m25334kg"+".txt"
		f_out=open(fol_out+"/"+output_file,"w")

		english_words=English_dict.read()
		english_words=english_words.split()
		
		text=f_in.readlines()
		lines=[line.rstrip("\n") for line in text]
		upper=0
		num=0
		punct=0
		symbols=0
		newString=""
		for line in lines:
			i=0
			while i<len(line):
				char=line[i]
				if char==" ":
					newString+=char
				elif char.isalpha():
					if char.isupper():
						newString+=char.lower()
						upper+=1
					else:
						newString+=char
				elif char.isdigit():
					num+=1
				elif char in [".","?","!",",",":",";","-","(",")","[","]","{","}","—","'",'"']:
					punct+=1
					if char==".":
						if len(line)-i>2:
							if line[i+1]=="." and line[i+2]==".":
								#therefore, the symbol scanned is ellipsis(...)
								i+=3
								continue
				else:
					symbols+=1
				i+=1

			words=newString.split()
			correct_words=0
			wrong_words=0
			total_words=0
			for word in words:
				total_words+=1
				if word.lower() in english_words:
					correct_words+=1
				else:
					wrong_words+=1

		f_out.write(os.getlogin()+"\n")
		f_out.write("Formatting ###################"+"\n")
		f_out.write("Number of upper case letters changed: "+str(upper)+"\n")
		f_out.write("Number of punctuations removed: "+str(punct)+"\n")
		f_out.write("Number of numbers removed: "+str(num)+"\n")
		f_out.write("Spellchecking ###################"+"\n")
		f_out.write("Number of words: "+str(total_words)+"\n")
		f_out.write("Number of correct words: "+str(correct_words)+"\n")
		f_out.write("Number of incorrect words: "+str(wrong_words)+"\n")
		print(newString)

		f_in.close()
		f_out.close()

		English_dict.close()


except SyntaxError as err:
	print(err)
except Exception:
	print("Sorry! Something went wrong.")


