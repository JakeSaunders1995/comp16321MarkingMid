import os, argparse


def getUserInput():
	parser = argparse.ArgumentParser()
	parser.add_argument('english_path', type=str)
	parser.add_argument('input_folder', type=str)
	parser.add_argument('output_folder', type=str)
	args = parser.parse_args()

	with open(args.english_path, "r") as f:
		english_words = f.read().split("\n")
	if not os.path.exists(args.output_folder):
	    os.makedirs(args.output_folder)

	return english_words, args.input_folder, args.output_folder


def formatText(txt):
	formatted = ""
	upp, pun, num = 0, 0, 0
	for c in txt:
		if c == " ":
			formatted += c
		elif c != c.lower():
			formatted += c.lower()
			upp += 1
		elif c.isdigit():
			num += 1
		elif c in punctuation:
			pun += 1
		else:
			formatted += c

	word_li = formatted.split()
	cor, inc = 0, 0
	for word in word_li:
		if word in english_words:
			cor += 1
		else:
			inc += 1

	return upp, pun, num, len(word_li), cor, inc


english_words, input_folder, output_folder = getUserInput()
punctuation = [".", "?", "!", ",", ";", ":", "-", "(", ")", "{", "}", "[", "]", "'", '"', "…"]
filenames = os.listdir(input_folder)
for file in filenames:
	try:
		if not file.endswith(".txt"):
			continue
		with open(input_folder + "/" + file, "r") as f:
			txt = f.read()
		upp, pun, num, wor, cor, inc = formatText(txt)
	except Exception as e:
		upp, pun, num, wor, cor, inc = 0, 0, 0, 0, 0, 0
		print(repr(e))

	output_location = output_folder + "/" + file[:-4] + "_d50341jc.txt"
	with open(output_location, "w") as f:
		f.write("d50341jc\n")
		f.write("Formatting ###################\n")
		f.write("Number of upper case letters changed: " + str(upp) + "\n")
		f.write("Number of punctuations removed: " + str(pun) + "\n")
		f.write("Number of numbers removed: " + str(num) + "\n")
		f.write("Spellchecking ###################\n")
		f.write("Number of words: " + str(wor) + "\n")
		f.write("Number of correct words: " + str(cor) + "\n")
		f.write("Number of incorrect words: " + str(inc) + "\n")
