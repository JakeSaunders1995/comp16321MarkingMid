import os
import sys
import re
path = os.getcwd()
try:
	os.chdir(sys.argv[1])
	true_text = sys.argv[1]
	os.chdir(sys.argv[2])
	true_input = sys.argv[2]
	os.chdir(sys.argv[3])
	true_ouput = sys.argv[3]
except:
	arg1 = (sys.argv[1])[2:]
	arg2 = (sys.argv[2])[2:]
	arg3 = (sys.argv[3])[2:]
	true_text = path + "/" + arg1
	true_input = path + "/" + arg2
	true_ouput = path + "/" + arg3
os.chdir(true_input)
				
input_folder = os.listdir(true_input)
file_names = []
for file in input_folder:
	if file.endswith(".txt"):
		uppercase_count = 0
		punctuation_count = 0
		number_count = 0
		file_names.append(file)
		with open(file,"r") as f:
			file_content = (f.read()).strip()
			for x in file_content:
				if x.isupper(): uppercase_count += 1 
			print("uppercase:" + str(uppercase_count))	
			for y in file_content:
				if y.isnumeric(): number_count += 1 
			print("number:" + str(number_count))
			for z in file_content:
				if not z.isalpha() and z != " " and not z.isalnum(): 
					punctuation_count += 1
			print("punctuation" + str(punctuation_count))
			lowercase_file = file_content.lower()
			casefile = lowercase_file.replace(".","")
			casefile = casefile.replace("?","")
			casefile = casefile.replace("!","")
			casefile = casefile.replace(",","")
			casefile = casefile.replace(":","")
			casefile = casefile.replace(";","")
			casefile = casefile.replace("-","")
			casefile = casefile.replace("–","")
			casefile = casefile.replace("(","")
			casefile = casefile.replace(")","")
			casefile = casefile.replace("[","")
			casefile = casefile.replace("]","")
			casefile = casefile.replace("{","")
			casefile = casefile.replace("}","")
			casefile = casefile.replace("'","")
			casefile = casefile.replace("\"","")
			casefile = casefile.replace("…","")
			casefile = casefile.replace("1","")
			casefile = casefile.replace("2","")
			casefile = casefile.replace("3","")
			casefile = casefile.replace("4","")
			casefile = casefile.replace("5","")
			casefile = casefile.replace("6","")
			casefile = casefile.replace("7","")
			casefile = casefile.replace("8","")
			casefile = casefile.replace("9","")
			casefile = casefile.replace("0","")
			casefile = casefile.replace("\n","")
			casefile = casefile.replace("\t","")
			casefile = casefile.strip()
			casefile = casefile.replace("  "," ")
			word_list = casefile.split(" ")
			
			for x in word_list:
				if not x.isalnum(): word_list.remove(x)
				if x == "\n": word_list.remove(x)
	
			print("words:" + str(len(word_list)))

			englishfile = open(true_text)
			spellcheck = []
			count = 0
			incorrectwords = []
			for line in englishfile:
				line = line.strip()
				spellcheck.append(line)
			for x in word_list:
				for y in spellcheck:
					if y == x: 
						count += 1
						break
				if x != y: incorrectwords.append(x)
			print(incorrectwords)
			print("Incorrect words: " + str(len(word_list)-count))
		os.chdir(true_ouput)
		output_file = file[:-4] + "_n80569fh.txt"
		print (output_file)
		with open(output_file,"w") as o:
			o.write("n80569fh \nFormatting ################### \nNumber of upper case letters changed: " + str(uppercase_count) +"\nNumber of punctuations removed: " + str(punctuation_count) + "\nNumber of numbers removed: " + str(number_count) +"\nSpellchecking ################### \nNumber of words: " + str(len(word_list)) +"\nNumber of correct words: " + str(count) +"\nNumber of incorrect words: " + str(len(incorrectwords)))
		os.chdir(true_input)


