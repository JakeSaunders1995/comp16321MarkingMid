import os
import argparse


def main(scoring):

    leng = len(scoring)
    points1 = 0
    points2 = 0

    points = {
        't': 5,
        'c': 2,
        'p': 3,
        'd': 3
    }

    for i in range(0, leng, 3):
        ordi = scoring[i + 2]
        to_add = points[ordi]
        if scoring[i + 1] == '1':
            points1 = points1 + to_add
        else:
            points2 = points2 + to_add

    return f"{points1}:{points2}"


parser = argparse.ArgumentParser()
parser.add_argument('input_folder')
parser.add_argument('output_folder')
args = parser.parse_args()

input_folder = args.input_folder
output_folder = args.output_folder
input_files = os.listdir(f"./{input_folder}")

for file in input_files:
    f = open(f"{input_folder}/{file}", "r")
    string = f.read().replace("\n", " ")
    string = string.strip()
    ans = main(string)
    k = file.find('.')
    output_file = file[0:k] + "_h63651bn" + file[k:]
    g = open(f"{output_folder}/{output_file}", "w")
    g.write(ans)
    f.close()
    g.close()

