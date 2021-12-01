import os
import argparse
import re

def rugby(input_file, output_file):
    f = open(input_file, 'r')
    content = f.read()
    flag = 0
    score_1 = 0
    score_2 = 0
    t_1 = content.count("T1t")
    c_1 = content.count("T1c")
    p_1 = content.count("T1p")
    d_1 = content.count("T1d")
    t_2 = content.count("T2t")
    c_2 = content.count("T2c")
    p_2 = content.count("T2p")
    d_2 = content.count("T2d")
    score_1 = (t_1 * 5) + (c_1 * 2) + (p_1 * 3) + (d_1 * 3)
    score_2 = (t_2 * 5) + (c_2 * 2) + (p_2 * 3) + (d_2 * 3)
    with open(output_file, "w") as f:
        text = f.write(str(score_1) + ":" + str(score_2))
    f.close()

def list_dir(start_dir):
    file_list = []
    dir_res = os.listdir(start_dir)
    for path in dir_res:
        temp_path = start_dir + path
        if os.path.isfile(temp_path):
            file_list.append(temp_path)
    return file_list


if __name__ == '__main__':
    argv = argparse.ArgumentParser()
    argv.add_argument("test_folder")
    argv.add_argument("target_folder")
    argv_list = argv.parse_args()

    test_file_list = list_dir(argv_list.test_folder)

    output_path = argv_list.target_folder
    if os.path.exists(output_path) == False:
        os.mkdir(output_path)

    for test_file in test_file_list:
        output_file = output_path + '/' + test_file.replace(argv_list.test_folder, '')
        rugby(test_file, output_file)
