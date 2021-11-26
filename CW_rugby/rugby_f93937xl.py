import argparse
import os


parser = argparse.ArgumentParser(description='rugby')
parser.add_argument('input_path', type=str, help='A required string argument -- input path')
parser.add_argument('output_path', type=str, help='A required string argument -- output path')

args = parser.parse_args()

input_path = args.input_path
output_path = args.output_path
input_files = os.listdir(input_path)
output_files = os.listdir(output_path)


a = 0
while a < len(input_files):
    input_file = input_files[a]
    input_path_1 = input_path + "/" + input_file
    with open(input_path_1, "r") as f:
        lst = f.read()
    score1 = 0
    score2 = 0
    p = 0
    while p < len(lst):
        while lst[p+1] == "1":
            if lst[p+2] == "t":
                score1 += 5
            elif lst[p+2] == "c":
                score1 += 2
            else:
                score1 += 3
            break
        while lst[p+1] == "2":
            if lst[p+2] == "t":
                score2 += 5
            elif lst[p+2] == "c":
                score2 += 2
            else:
                score2 += 3
            break
        p = p + 3
    score = str(score1) + ":" + str(score2)
    output_file = input_file[:-4] + "_f93937xl" + input_file[-4:]
    output_path_1 = output_path + "/" + output_file
    with open(output_path_1, "w+") as f:
         score = f.write(score)
    a = a + 1


f.close()
