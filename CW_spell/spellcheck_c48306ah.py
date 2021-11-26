import os
import re
import argparse


parser = argparse.ArgumentParser()

parser.add_argument("words")
parser.add_argument("input")
parser.add_argument("output")

args = parser.parse_args()

file = open(os.path.join(args.words))
words = file.read().lower().split("\n")
file.close()

punctuation = ["...", ".", ",", "?", "!", '"', "'", ":", ";", "-", "(", ")", "{", "}", "[", "]"]

def format_text(text):
	text = text.split(" ")
	numbers = 0
	punctuated = 0
	upper_case_changes = 0
	correct_words = 0

	for word in text:
		for character in word:
			if ord(character) >= 65 and ord(character) <= 90:
				upper_case_changes += 1
				break
		
	text = " ".join(text)

	for character in text:
		if character in "0123456789":
			numbers += 1

	for number in range(9):
		text = text.replace(str(number), "")

	for punctuation_mark in punctuation:
		punctuated += text.count(punctuation_mark)
		text = text.replace(punctuation_mark, "")

	text = re.sub(' +', ' ', text).lower()

	for word in text.replace("\n", "").strip().split(" "):
		test_word = re.sub("[!.?,'#@]", "", word)
		test_word = re.sub('"', "", test_word)

		if test_word in words:
			correct_words += 1

	return {
		"text": text,
		"num_words": len(text.replace("\n", "").strip().split(" ")),
		"punctuated": punctuated,
		"upper_case_changes": upper_case_changes,
		"numbers": numbers,
		"correct_words": correct_words
	}
		

for filename in sorted(os.listdir(args.input)):
	file = open(os.path.join(args.input, filename))
	text = file.read()
	file.close()

	formatted_text = format_text(text)

	file = open(os.path.join(args.output, f"{os.path.splitext(filename)[0]}_c48306ah.txt"), "w")
	file.write("c48306ah\n")
	# file.write("[user_name]\n")
	file.write(f"Formatting ###################\n")
	file.write(f"Number of upper case letters changed: {formatted_text['upper_case_changes']}\n")
	file.write(f"Number of punctuations removed: {formatted_text['punctuated']}\n")
	file.write(f"Number of numbers removed: {formatted_text['numbers']}\n")
	file.write(f"Spellchecking ###################\n")
	file.write(f"Number of words: {formatted_text['num_words']}\n")
	file.write(f"Number of correct words: {formatted_text['correct_words']}\n")
	file.write(f"Number of incorrect words: {formatted_text['num_words'] - formatted_text['correct_words']}\n")
	file.close()

# for filename in sorted(os.listdir("./midterm_files/Example_outputs/Example_outputs_program3")):
# 	file = open(os.path.join("./midterm_files/Example_outputs/Example_outputs_program3", filename))
# 	correct = file.read()
# 	file.close()

# 	file = open(os.path.join("outputs", f"{os.path.splitext(filename)[0].replace('_[user_name]', '')}_c48306ah.txt"))
# 	attempt = file.read()
# 	file.close()

# 	if attempt == correct:
# 		print(f"Test {os.path.splitext(filename)[0].replace('_[user_name]', '')} PASSED")
# 	else:
# 		print(f"Test {os.path.splitext(filename)[0].replace('_[user_name]', '')} FAILED")