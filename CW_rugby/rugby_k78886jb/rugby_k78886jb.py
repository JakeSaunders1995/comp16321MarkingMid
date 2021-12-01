import argparse
import os

inputs = argparse.ArgumentParser()
inputs.add_argument('input_path')
inputs.add_argument('output_path')

arguments = inputs.parse_args()

files = []
for file in os.listdir(arguments.input_path):
    files.append(os.path.join(arguments.input_path, file))


t = 5
c = 2
p = 3
d = 3

for input_file in files:

    f = open(input_file, 'r')
    text = f.read()
    f.close()

    i = -1
    while input_file[i] != '/':
        i -= 1

    filename = input_file[i:-4]

    Score_1 = 0
    Score_2 = 0
    i = 0

    while i < len(text):
        if text[i+1] == '1':
            if text[i+2] == 't':
                Score_1 += t
            elif text[i+2] == 'c':
                Score_1 += c
            elif text[i+2] == 'p':
                Score_1 += p
            else:
                Score_1 += d
        else:
            if text[i+2] == 't':
                Score_2 += t
            elif text[i+2] == 'c':
                Score_2 += c
            elif text[i+2] == 'p':
                Score_2 += p
            else:
                Score_2 += d
        i += 3

    output_file = arguments.output_path + '/' + filename + '_k78886jb.txt'

    f = open(output_file, 'w')
    f.write(str(Score_1)+':'+str(Score_2))
    f.close()
