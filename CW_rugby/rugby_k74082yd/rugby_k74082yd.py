import argparse

import os


parser = argparse.ArgumentParser()

parser.add_argument('input_file_path')

parser.add_argument('output_file_path')



config = parser.parse_args()


def deal(input_file, output_file):

    score_table = {'t': 5, 'c': 2, 'p': 3, 'd': 3}



    score_1 = 0

    score_2 = 0

    with open(input_file) as f:

        s = f.read().strip().split('T')

        for data in s:

            if len(data) != 2:

                continue

            else:

                if data[0] == '1':

                    score_1 += score_table[data[1]]

                else:

                    score_2 += score_table[data[1]]



    with open(output_file, 'w+') as f:

        f.write(str(score_1) + ':' + str(score_2))









files_name = os.listdir(config.input_file_path)

out_name = [f.split('.')[0]+'_k74082yd'+'.txt' for f in files_name]

for i,f in enumerate(files_name):

    deal(config.input_file_path + '/' + f, config.output_file_path + '/' + out_name[i])