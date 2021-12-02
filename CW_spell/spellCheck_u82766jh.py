import os
import argparse

def read_file(file):
    with open(file, 'r') as f1:
        list1 = f1.readlines()
    for i in range(0, len(list1)):
        list1[i] = list1[i].rstrip('\n')
    return list1

def write_file(file, result_string):
    with open(file, 'w') as f1:
        f1.write(result_string)

def list_dir(start_dir):
    file_list = []
    dir_res = os.listdir(start_dir)
    for path in dir_res:
        # temp_path = start_dir + '/' + path
        temp_path = start_dir + path
        if os.path.isfile(temp_path):
            file_list.append(temp_path)
            # print(temp_path)
    return file_list

def write_file2(file, upper, punc, number, all_words, correct, incorrect):
    with open(file, 'a') as f1:
        print('u82766jh', file=f1)
        print('Formatting ###################', file=f1)
        print('Number of upper case words transformed: ', upper, file=f1)
        print('Number of punctuation’s removed: ', punc, file=f1)
        print('Number of numbers removed: ', number, file=f1)
        print('Spellchecking ###################', file=f1)
        print('Number of words in file: ', all_words, file=f1)
        print('Number of correct words in file: ', correct, file=f1)
        print('Number of incorrect words in file: ', incorrect, file=f1)

def checker(test_file, target_file):
    count_punctuation = 0
    count_upper_case = 0
    count_number = 0
    count_all_words = 0
    count_correct_words = 0
    count_incorrect_words = 0
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

    test_list = read_file(test_file)
    index = 0
    for line in test_list:
        line = list(line)

        for c in line:
            if c in punctuation:
                count_punctuation += 1
                line[index] = ''
            elif c.isupper():
                count_upper_case += 1
                line[index] = c.lower()
            elif c.isdigit():
                count_number += 1
                line[index] = ''
            index += 1

        line_string_list = ''.join(line).split(' ')
        line_string_list = [s for s in line_string_list if s != '']
        for word in line_string_list:
            count_all_words += 1
            if word in word_list:
                count_correct_words += 1
            else:
                count_incorrect_words += 1

    write_file2(target_file, count_upper_case, count_punctuation, count_number, count_all_words,
                count_correct_words, count_incorrect_words)


if __name__ == '__main__':
    argv = argparse.ArgumentParser()
    argv.add_argument("word_file")
    argv.add_argument("test_folder")
    argv.add_argument("target_folder")
    argv_list = argv.parse_args()

    word_file = argv_list.word_file
    word_list = read_file(word_file)

    test_file_list = list_dir(argv_list.test_folder)
    # print(test_file_list)

    output_path = argv_list.target_folder
    if os.path.exists(output_path) == False:
        os.mkdir(output_path)

    for test_file in test_file_list:
        # print(test_file)
        target_file = output_path + '/' + test_file.replace(argv_list.test_folder, '')
        # print(target_file)
        checker(test_file, target_file)
