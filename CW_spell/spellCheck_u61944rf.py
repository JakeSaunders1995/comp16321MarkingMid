import os
import argparse
import re

INPUT_PATH = "midterm_files/Example_inputs/Example_inputs_program3"
OUTPUT_PATH = "midterm_files/Example_outputs/Example_outputs_program3"
USER_NAME = 'u61944rf'
ENGLISH_DICT_PATH = "midterm_files/EnglishWords.txt"



class SpellCheck():
    def __init__(self, dict_file) -> None:
        with open(dict_file) as f:
            self.eng_dict = f.read().split('\n')
            self.remove_num = '1 2 3 4 5 6 7 8 9 0'.split(' ')
            self.remove_pun = '. ? ! , : ; - _ [ ] { } ( ) \' \" @ #'.split(' ')
        
        
    
    def __call__(self, input_f, output_f): #read str
        #create result list
        with open(input_f) as f:
            all_str = f.read()

        #check upper case, number, pun
        lower_str = all_str.lower()
        num_lower = 0
        num_number = 0
        num_pun = 0
        pure_str_list = []
        for a, b in zip(all_str, lower_str):
            num_lower += (a != b)
            if b in self.remove_num:
                num_number += 1
                continue
            elif b in self.remove_pun:
                num_pun += 1
                continue
            else:
                pure_str_list.append(b)
        pure_str = "".join(pure_str_list)
        result = [USER_NAME]
        result.append('Formatting ###################')
        result.append(f'Number of upper case words changed: {num_lower}')
        result.append(f'Number of punctuations removed: {num_pun}')
        result.append(f'Number of numbers removed: {num_number}')

        #chck spell
        pure_list = pure_str.split(' ')
        all_num = 0
        correct_num = 0
        eng_dict = self.eng_dict
        for word in pure_list:
            if word == '':
                continue
            correct_num += (word in eng_dict)
            all_num += 1
        incorretc_num = all_num - correct_num

        result.append('Spellchecking ###################')
        result.append(f'Number of words: {all_num}')
        result.append(f'Number of correct words: {correct_num}')
        result.append(f'Number of incorretc words: {incorretc_num}')



        with open(output_f, 'w') as f:
            for str in result:
                f.write(str)
                f.write('\n')

                                         
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('englishword', default=ENGLISH_DICT_PATH)
    parser.add_argument('input', default=INPUT_PATH)
    parser.add_argument('output', default=OUTPUT_PATH)

    opt = parser.parse_args()

    #run calculate
    algo = SpellCheck(opt.englishword)
    for file_name in os.listdir(opt.input):
        input_file = opt.input + '/' + file_name
        output_file = opt.output+'/'+file_name[:-4]+'_'+USER_NAME+'.txt'
        algo(input_file, output_file)
    

