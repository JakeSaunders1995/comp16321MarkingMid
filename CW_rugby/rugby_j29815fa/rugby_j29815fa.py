import os
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('input')
parser.add_argument('output')

args = parser.parse_args()

list_of_scores = [["t", 5], ["c", 2], ["p", 3], ["d", 3]]

for file in sorted(os.listdir(args.input)):
    with open(args.input + "/" + file, "r") as f1:
        string = f1.read()
        T1 = 0
        T2 = 0
        for i in range(0, len(string), 3):
            score = string[i: i + 3]
            if "1" in score:
                for item in list_of_scores:
                    if item[0] in score:
                        T1 += item[1]
            else:
                for item in list_of_scores:
                    if item[0] in score:
                        T2 += item[1]
        with open(args.output + "/" + file.replace(".txt", "") + "_j29815fa.txt", "w") as f2:
            f2.write(str(T1) + ":" + str(T2))
