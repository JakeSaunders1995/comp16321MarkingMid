import argparse
import os

scoring_type = {
    't': 5,
    'c': 2,
    'p': 3,
    'd': 3
}

username = 'g91274qw'

def parse_args():

    parser = argparse.ArgumentParser()
    parser.add_argument('input_folder')
    parser.add_argument('output_folder')
    args = parser.parse_args()
    return args.input_folder, args.output_folder


def winner(input_file_path, output_file_path):

    with open(input_file_path) as f:
            result = f.readline().strip()

    T1_scoring = 0
    T2_scoring = 0
    m = 0
    Team = result[m + 1]
    letter = result[m + 2]
    if Team == '1':
        T1_scoring += scoring_type[letter]
    else:
        T2_scoring += scoring_type[letter]

    m += 3
    Team = result[m + 1]
    letter = result[m + 2]
    if Team == '1':
        T1_scoring += scoring_type[letter]
    else:
        T2_scoring += scoring_type[letter]

    m += 3
    Team = result[m + 1]
    letter = result[m + 2]
    if Team == '1':
        T1_scoring += scoring_type[letter]
    else:
        T2_scoring += scoring_type[letter]

    m += 3
    Team = result[m + 1]
    letter = result[m + 2]
    if Team == '1':
        T1_scoring += scoring_type[letter]
    else:
        T2_scoring += scoring_type[letter]

    m += 3
    if m < len(result):
        Team = result[m + 1]
        letter = result[m + 2]
        if Team == '1':
            T1_scoring += scoring_type[letter]
        else:
            T2_scoring += scoring_type[letter]



    m += 3
    if m < len(result):
        Team = result[m + 1]
        letter = result[m + 2]
        if Team == '1':
            T1_scoring += scoring_type[letter]
        else:
            T2_scoring += scoring_type[letter]


    m += 3
    if m < len(result):
        Team = result[m + 1]
        letter = result[m + 2]
        if Team == '1':
            T1_scoring += scoring_type[letter]
        else:
            T2_scoring += scoring_type[letter]




    with open(output_file_path, 'w') as f:
            f.write('{}:{}'.format(T1_scoring, T2_scoring))


if __name__ == '__main__':

    input_folder, output_folder = parse_args()
    file_list = os.listdir(input_folder)
    for file in file_list:
        input_file = os.path.join(input_folder, file)
        output_folder_path = os.path.abspath(output_folder)
        if not os.path.exists(output_folder_path):
            os.makedirs(output_folder_path)
        output_file = os.path.join(output_folder_path,
                                   os.path.splitext(file)[0] + '_' + username + '.txt')
        winner(input_file, output_file)
