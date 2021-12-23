import re
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("engpath")
parser.add_argument("echo")
parser.add_argument("output")
args = parser.parse_args()
eng_path = args.engpath
directory_in = args.echo
directory_out = args.output



for file in os.listdir(directory_in):
	x = os.path.join(directory_in, file)
	z = open(eng_path)
	f = open(x)
	lines = f.read()
	eng_words = z.read()
	converted_text = ""
	upper_count = 0
	punc_count = 0
	num_count = 0
	num_words = 0
	num_corr_words = 0
	num_incor_words = 0
	punc_list = [".", "?", "!", ",", ":", ";", "-", "--", "(", ")"
	, "{", "}", "[", "]", "'", "❝", "❞", "..."]
	for i in range(len(lines)):
		if lines[i].isupper():
			converted_text += lines[i]
			upper_count += 1

		elif lines[i].isnumeric():
			num_count += 1

		elif lines[i] in punc_list:
			punc_count += 1

		else:
			converted_text += lines[i]

	final_text = converted_text.lower()
	check_text = re.split(' |\n', final_text)
	pass_text = []

	for i in check_text:
		if i != "":
			pass_text.append(i)

	num_words = len(pass_text) 
	for i in range(len(pass_text)):
		if pass_text[i] in eng_words:
			num_corr_words += 1
		elif pass_text[i] not in eng_words:
			num_incor_words += 1
		else: break
		

	file_name = re.split('.txt', file)
	file_out_name = file_name[0]
	file_out_path = directory_out + "/" + file_out_name + "_" + "v14799cc.txt"
	g = open(file_out_path, "a")
	g.write("v14799cc\n")
	g.write("Formatting ##################\n")
	g.write("Number of upper case words changed: " + str(upper_count) + "\n")
	g.write("Number of punctuations removed: " + str(punc_count) + "\n")
	g.write("Number of numbers removed: " + str(num_count) + "\n")
	g.write("Spellchecking ##################\n")
	g.write("Number of words: " + str(num_words) + "\n")
	g.write("Number of correct words: " + str(num_corr_words) + "\n")
	g.write("Number of incorrect words: " + str(num_incor_words) + "\n")

	
f.close()
g.close()
z.close()