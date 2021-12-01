import argparse
import os

def scoring(x):
    if score[x] == "t":
        return 5
    elif score[x] == "c":
        return 2
    elif score[x] in "pd":
        return 3
    else:
        return

parser = argparse.ArgumentParser()
parser.add_argument("input", help="Input file path")
parser.add_argument("output", help="Output file path")
args = parser.parse_args()
files = []
for file in os.listdir(args.input):
    if file.endswith(".txt"):
        files.append(file)
for x in files:
    with open(os.path.join(args.input, x)) as file1:
        score = file1.readline()
    t1 = t2 = 0
    for i in range(1, len(score), 3):
        if score[i] == "1":
            t1 += scoring(i + 1)
        else:
            t2 += scoring(i + 1)
    print(f"{t1}:{t2}")
    if t1 > t2:
        print("Team 1 wins!")
    elif t1 < t2:
        print("Team 2 wins!")
    else:
        print("Draw")
    with open(os.path.join(args.output, f"{x[:-4]}_w27888ms.txt"), "w") as file2:
        file2.write(f"{t1}:{t2}")
