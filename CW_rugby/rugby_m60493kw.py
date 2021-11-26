import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('input_path')
parser.add_argument('output_path')
args = parser.parse_args()
a = os.listdir(args.input_path)
b = sorted(a)
for i in range(len(os.listdir(args.input_path))):
    
    
    with open(args.input_path + "/" + b[i], "r") as f:
        file = f.read()

    record = file.split("T")[1:]

    score = [0, 0]
    scoreMap = {
        't': 5,
        'c': 2,
        'p': 3,
        'd': 3
    }

    for r in record:
        score[int(r[0]) - 1] += scoreMap[r[1]]

    with open(args.output_path+"/test_file"+str(int(i)+1)+"_m60493kw.txt", "w") as f:
        f.write(f"{score[0]}:{score[1]}")
        
