import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('input', type=str)
parser.add_argument('output', type=str)
args = parser.parse_args()

score_type = {'t': 5,
             'c': 2,
             'p': 3,
             'd': 3}
# renames original .txt file to include _q26752aa
def get_name(file_name):
    for i in range(len(file_name)):
        if file_name[i] == '.':
            output_name = file_name[0:i]
            return output_name + '_q26752aa.txt'
#-----------------------------------------------#
os.chdir(args.input)
for file in os.listdir():
    t1_score = 0
    t2_score = 0
    if file.endswith(".txt"):
        filepath = args.input + '/' + file
        f = open(filepath, "r")
        input = f.read().strip()
        f.close()

        for i in range(len(input)):
            char = input[i]
            if char == '1':
                t1_score += score_type.get(input[i + 1])
            if char == '2':
                t2_score += score_type.get(input[i + 1])

        final_score = str(t1_score) + ':' + str(t2_score)
        filepath = args.output + '/' + get_name(file)

        w = open(filepath, "w")
        w.write(final_score)
        w.close()
