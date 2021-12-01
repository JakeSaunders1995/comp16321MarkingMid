import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('input_file')
parser.add_argument('output_file')
args = parser.parse_args()
input = args.input_file
output = args.output_file

def comput_score(file):
    m = {'t':5, 'c':2, 'p':3, 'd':3}
    with open(file) as f:
        content = f.read().strip()
    ls = content.split('T')
    scores = {}
    for item in ls:
        if len(item) == 0:
            continue
        num = item[0]
        score = m[item[1]]
        if num in scores:
            scores[num] += score
        else:
            scores[num] = score
    return scores['1'], scores['2']

def main(input, output):
    score1, score2 = comput_score(input)
    with open(output, 'w') as f:
        f.write(f'{score1}:{score2}\n')

files_in = os.listdir(input)
if not os.path.exists(output):
    os.mkdir(output)
for item in files_in:
    name=os.path.join(output, item.split('.')[0]+'_f60163yw.txt')
    item = os.path.join(input, item)
    main(item, name)
