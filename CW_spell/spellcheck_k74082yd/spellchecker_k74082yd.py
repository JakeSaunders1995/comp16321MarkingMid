import argparse

import os



parser = argparse.ArgumentParser()

parser.add_argument('EnglishWords')

parser.add_argument('input_file_path')

parser.add_argument('output_file_path')



config = parser.parse_args()





def deal(englishWord, input_file, output_file):

    EnglishWords = []

    with open(englishWord) as f:

        data = f.readlines()

        for word in data:

            EnglishWords.append(word.strip())



    with open(input_file) as f:

        data = f.read().strip().split(' ')

        upper_count = 0

        number_count = 0

        punctuation_count = 0

        text = []

        for word in data:

            temp_word= ''

            for letter in word:

                if letter.isdigit():

                    number_count += 1

                    continue

                if letter.isalpha():

                    if letter.isupper():

                        upper_count += 1

                        temp_word += letter.lower()

                        continue

                    else:

                        temp_word += letter.lower()

                else:

                    punctuation_count +=1

                    continue

            if temp_word == '':

                continue

            else:

                text.append(temp_word)



    correct_count = 0

    for w in text:

        if w in EnglishWords:

            correct_count += 1



    with open(output_file, 'w+') as f:

        f.write('[k74082yd]\n')

        f.write('Formatting ###################\n')

        f.write('Number of upper case words changed: {}\n'.format(upper_count))

        f.write('Number of punctuations removed: {}\n'.format(punctuation_count))

        f.write('Number of numbers removed: {}\n'.format(number_count))

        f.write('Spellchecking ###################\n')

        f.write('Number of words: {}\n'.format(len(text)))

        f.write('Number of correct words: {}\n'.format(correct_count))

        f.write('Number of incorrect words: {}'.format(len(text)-correct_count))



files_name = os.listdir(config.input_file_path)

out_name = [f.split('.')[0]+'_k74082yd'+'.txt' for f in files_name]

for i,f in enumerate(files_name):

    deal(config.EnglishWords, config.input_file_path+'/'+f, config.output_file_path+'/'+out_name[i])