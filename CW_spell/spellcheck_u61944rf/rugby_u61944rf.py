import os
import argparse
import re

INPUT_PATH = "midterm_files/Example_inputs/Example_inputs_program1"
OUTPUT_PATH = "midterm_files/Example_outputs/Example_outputs_program1"
USER_NAME = 'u61944rf'


class Rugby():
    def __init__(self) -> None:
        self.scoring_dict = {'t':5, 'c':2, 'p':3, 'd':3}
    

    def __call__(self, inputfile, output_file):
        with open(inputfile) as f:
            str_rcd = f.read()
        src_rcd = str_rcd.split('T')[1:]

        src_list = [0,0]

        for str_item in src_rcd:
            team_num = int(str_item[0]) - 1
            type = str_item[1]
            src = self.scoring_dict[type]
            src_list[team_num] += src

        with open(output_file, 'w') as f:
            f.write(f'{src_list[0]}:{src_list[1]}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input',default=INPUT_PATH)
    parser.add_argument('output', default=OUTPUT_PATH)

    opt = parser.parse_args()

    #run calculate
    algo = Rugby()
    for file_name in os.listdir(opt.input):
        output_file = opt.output + '/' + file_name[:-4]+'_'+USER_NAME+'.txt'
        input_file = opt.input + '/' + file_name
        algo(input_file, output_file)
    

