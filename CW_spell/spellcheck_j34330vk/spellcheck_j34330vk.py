import sys
import os


n = len(sys.argv) #total arguments
print("Total arguments passed:", n)

print("\nName of Python script:", sys.argv[0]) #printing the python script

input_directory = sys.argv[2]
output_directory = sys.argv[3]

for filename in os.listdir(input_directory):
    if filename.endswith(".txt"):
        input_file = open(os.path.join(input_directory,filename) ,"r") #Opening The required file for input

        test_str = input_file.readline() #Reading the file as a string

        input_file.close()

        punc = '''! ( ) - [ ] { } ; : ' " \ , < > . / ? * _""''' #Making a variable for all punctuations

        punc = punc.split(' ')
        punc.append('...') 
        count_punc=0 # Counter for punctuation marks
        for ele in test_str: 
            if ele in punc: 
                test_str = test_str.replace(ele, "") # Removing punctuations from string
                count_punc+=1 #Updating the counter for punctuations

        nos = "1234567890"
        count_nos=0
        for num1 in test_str: 
            if num1 in nos: 
                test_str = test_str.replace(num1, "") # Removing numbers from string
                count_nos+=1 #Updating the counter for numbers

        count_upper=0 # Counter for UpperCase letters
        for i in test_str:
            if i.isupper() == True:
                test_str=test_str.replace(i,i.lower()) # Replacing uppercase with lowercase
                count_upper+=1 #Updating the counter for UpperCase letters
            else:
                continue

        words1 = test_str.split() #Creating a list from the string to compare words of the given input file to EnglishWords.txt
        english_words_file = open(sys.argv[1],"r") #Opening The EnglishWords.txt

        test_2 = english_words_file.read() #Reading the file as a string

        english_words_file.close()

        correct_word_count=0 #Making a variable for all correct words
        incorrect_word_count=0 #Making a variable for all incorrect words
        words2=test_2.split()
        for l in words1:
            if l in words2: #Comparing the words from input file to EnglishWords.txt
                correct_word_count+=1 #Updating counter for every correct word

            else:
                incorrect_word_count+=1 #Updating counter for every incorrect word

        x=filename      
        x = x.replace(".txt", "_j34330vk.txt")

        output_file = open(os.path.join(output_directory, x),'w') #Opening an output file for giving the output
        
        write_str='j34330vk\n'
        output_file.write(write_str) #Writing the lines to output files
        output_file.write('Formatting ###################\n')                            #Writing the lines to output files

        output_file.write('Number of upper case words changed: '+str(count_upper)+'\n')  #Writing the lines to output files
        output_file.write('Number of punctuations removed: '+str(count_punc)+'\n')       #Writing the lines to output files
        output_file.write('Number of numbers removed: '+str(count_nos)+'\n')             #Writing the lines to output files

        output_file.write('Spellchecking ###################\n')                         #Writing the lines to output files
        output_file.write('Number of words in file: '+str(len(words1))+'\n')
        output_file.write('Number of correct words in file: '+str(correct_word_count)+'\n')      #Writing the lines to output files
        output_file.write('Number of incorrect words in file: '+str(incorrect_word_count)+'\n')  #Writing the lines to output files
        print

        output_file.close()
