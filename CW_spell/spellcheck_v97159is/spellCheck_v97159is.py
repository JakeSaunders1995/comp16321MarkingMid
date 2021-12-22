import argparse 
import string

my_parser = argparse.ArgumentParser()

my_parser.add_argument('English_words', type =argparse.FileType('r'))
my_parser.add_argument('input_file', type = argparse.FileType('r'))
my_parser.add_argument('output_file', type= argparse.FileType('w', encoding ='UTF-8'))
args = vars(my_parser.parse_args())
#if args['input_file']:
data = args['input_file'].read()

upper_case_words = 0
punctuation = 0
numbers = 0
correct_words = 0
incorrect_words = 0
formatted_text = ''

punctuations = '''!()-[]{};:'"\,<>.?/@#£$%^&*_+=~|'''

output = 'v97159is \n'
output += "Formatting ###################### \n"

for char in data:
	if char in punctuations:
		punctuation+=1
	elif char.isdigit():
		numbers +=1
	elif char.isupper():
		upper_case_words+=1
		formatted_text += char.lower()
	else:
		formatted_text += char

output+="Number of upper case words transformed: " + str(upper_case_words) + "\n"
output+= "Number of punctuation's removed: " + str(punctuation) + "\n"
output+="Number of number's removed: " + str(numbers) +"\n"


output+="Spellchecking #####################\n"

print(formatted_text)
array =[]
english_words = args['English_words'].read()
for line in english_words.split():
	array.append(line)

for word in formatted_text.split():
	if word in array:
		correct_words +=1
	else:
		incorrect_words +=1

output+="Number of words in file: " + str(correct_words + incorrect_words) + "\n"
output+="Number of correct words in file: " + str(correct_words) + "\n"
output+="Number of incorrect words in file: " + str(incorrect_words) + "\n"

print(output)

args['output_file'].write(output)