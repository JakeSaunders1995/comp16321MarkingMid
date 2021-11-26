import argparse	
import os



parser = argparse.ArgumentParser()
parser.add_argument("first")
parser.add_argument("second")
parser.add_argument("third")
args = parser.parse_args()

with open(args.first, "r") as textfile:
	english_text = textfile.read().splitlines()
	#print(english_text)


files = os.scandir(args.second) 

if not os.path.isdir(args.third):
	os.mkdir(args.third)


for element in files:

	with open(element.path, 'r') as myfile:
	    list1 = myfile.read()
	    
	    
	    upper_case = 0
	    punctuation = 0
	    numbers = 0

	    punctuation_list = [".", "?", "!", ",", ":", ";", "-", "(", ")", "{", "}", "()", "'", "[", "]", '...', '"', "@", "#"]
	    number_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

	    
	    for x in list1:
	    	if x.isupper():	
	    		upper_case += 1
	    		list1 = list1.replace(x,x.lower())
	    	elif x in punctuation_list:
	    		punctuation += 1
	    		list1 = list1.replace(x, "")
	    	elif x in number_list:
	    		numbers += 1
	    		list1 = list1.replace(x, "")
	    
	    
	    list2 = list1.split()
	    
	   
	    words = 0
	    correct_words = 0
	    incorrect_words = 0

	    for y in list2:
	    	words += 1
	    	if y in english_text:
	    		correct_words +=1 
	    	else:
	    		incorrect_words +=1



	output_name = element.name.split(".")[0]
	output_name = output_name + "h18603tp.txt"

	os.path.join(args.third, output_name)
	with open(os.path.join(args.third, output_name), 'w+') as myfile:
		myfile.write("h18603tp")
		myfile.write("\nFormatting ###################")
		myfile.write("\nNumber of upper case letters changed: " + str(upper_case))
		myfile.write("\nNumber of punctuations removed: " + str(punctuation))
		myfile.write("\nNumber of numbers removed: " + str(numbers))
		myfile.write("\nSpellchecking ###################")
		myfile.write("\nNumber of words: " + str(words))
		myfile.write("\nNumber of correct words: " + str(correct_words))
		myfile.write("\nNumber of incorrect words: " + str(incorrect_words))




	   