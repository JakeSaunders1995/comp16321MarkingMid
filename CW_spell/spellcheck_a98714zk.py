import sys
import os

directory = str(sys.argv[2])
for filename in os.listdir(directory): # Records all the files/directories in the specified path
    if filename.endswith(".txt"):
        inputTXTfile = os.path.join(directory, filename)
        input_file = open(inputTXTfile,"r")
        input_contents = input_file.read()
        input_file.close()

        english_word_txt = open(sys.argv[1], "r")
        eng_txt_contents = english_word_txt.readlines()
        english_words = []
        for word in eng_txt_contents:
            word = word.strip('\n')
            english_words.append(word)

        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        numbers = "0123456789"

        punctuation_count, number_count, uppercase_count = 0, 0, 0
        stripped_input_contents = ''
        for character in input_contents:
            if (character in punctuations):
                stripped_input_contents += ''
                punctuation_count += 1
            elif (character in numbers):
                stripped_input_contents += ''
                number_count += 1
            elif (character.isupper() == True):
                stripped_input_contents += str(character.lower())
                uppercase_count += 1
            else:
                stripped_input_contents += character

        word_array = stripped_input_contents.split()
        word_count = len(word_array)

        correct_word_count, incorrect_word_count = 0, 0

        for a_word in word_array:
            if (a_word in english_words):
                correct_word_count += 1
            else:
                incorrect_word_count += 1


        output = '''a98714zk
Formatting ###################
Number of upper case letters changed: ''' + str(uppercase_count) + '''
Number of punctuations removed: ''' + str(punctuation_count) + '''
Number of numbers removed: ''' + str(number_count) + '''
Spellchecking ###################
Number of words: ''' + str(word_count) + '''
Number of correct words: ''' + str(correct_word_count) + '''
Number of incorrect words: ''' + str(incorrect_word_count)

        save_path = str(sys.argv[3])
        filename_removeTXT = filename[0:-4]
        output_filename = str(filename_removeTXT+"_a98714zk.txt")

        completeName = os.path.join(save_path, output_filename)

        outputFile = open(completeName, "w+")
        outputFile.write(output)
        outputFile.close
