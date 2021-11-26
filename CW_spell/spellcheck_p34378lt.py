import sys
import os

englishwords_file = sys.argv[1]
inFolder = sys.argv[2]
outFolder = sys.argv[3]

punctuation_list = ['.', '?', '!', ',', ':', ';', '-', '(', ')', '{', '}', '[', ']', "'", '"']

for file in os.listdir(inFolder):
    if file.endswith('.txt'):
        upper_case_words = 0
        punctuation = 0
        numbers = 0
        words_in_file = 0
        correct_words = 0
        incorrect_words = 0

        textFile = open(inFolder + '/' + file, 'rt')
        String_in_file = textFile.read()
        String_in_file.strip()
        current_word = ''
        index = -1
        is_ellipsis = False
        for char in String_in_file:
            index += 1
            if char == '.' and is_ellipsis:
                continue
            elif char != '.' and is_ellipsis:
                is_ellipsis = False
            if char.isupper():
                upper_case_words += 1
            if not char.isalpha():
                if char.isnumeric():
                    numbers += 1
                elif char != ' ':
                    if char == '.':
                        if index + 3 <= len(String_in_file) and (String_in_file[index+1] and String_in_file[index+2]) == '.':
                            punctuation += 1
                            is_ellipsis = True
                        else:
                            punctuation += 1
                    elif char in punctuation_list:
                        punctuation += 1

            if char.isalpha() or char == "'" or char == '-':
                current_word += char
            elif current_word != '':
                if not current_word.isnumeric():
                    words_in_file += 1
                    correct = False
                    englishWords = open(englishwords_file)
                    for line in englishWords:
                        if current_word.lower() == line.strip():
                            correct = True
                            correct_words += 1
                            break
                    if not correct:
                        incorrect_words += 1
                    englishWords.close()
                current_word = ''

        if current_word != '':
            if not current_word.isnumeric():
                words_in_file += 1
                correct = False
                englishWords = open("EnglishWords.txt")
                for line in englishWords:
                    if current_word.lower() == line.strip():
                        correct = True
                        correct_words += 1
                        break
                if not correct:
                    incorrect_words += 1
                englishWords.close()
            current_word = ''

        outputName = file[:-4] + "_p34378lt"
        try:
            new_file = open(outFolder + '/' + (outputName + '.txt'), 'x')
        except:
            new_file = open(outFolder + '/' + (outputName + '.txt'), 'w')

        new_file.write('p34378lt\n' )
        new_file.write('Formatting ###################\n')
        new_file.write('Number of upper case words changed: ' + str(upper_case_words) + '\n')
        new_file.write('Number of punctuations removed: ' + str(punctuation) + '\n')
        new_file.write('Number of numbers removed: ' + str(numbers) + '\n')
        new_file.write('Spellchecking ###################\n')
        new_file.write('Number of words: ' + str(words_in_file) + '\n')
        new_file.write('Number of correct words: ' + str(correct_words) + '\n')
        new_file.write('Number of incorrect words: ' + str(incorrect_words) + '\n')


        textFile.close()
        new_file.close()

