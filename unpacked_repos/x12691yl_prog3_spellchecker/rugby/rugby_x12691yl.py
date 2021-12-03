import argparse, os

parser = argparse.ArgumentParser()
parser.add_argument('input_folder')
parser.add_argument('output_folder')
args = parser.parse_args()
input_folder, output_folder = args.input_folder, args.output_folder
input_folder = os.getcwd()+input_folder[1:] if input_folder[0] == '.' else input_folder
output_folder = os.getcwd()+output_folder[1:] if output_folder[0] == '.' else output_folder

def rugby(data):
    scoring = {'t': 5, 'c': 2, 'p': 3, 'd': 3}
    ans = [0, 0, 0]
    for i in range(2, len(data)+2, 3):
        ans[int(data[i-1])] += scoring[data[i]]
    return f"{ans[1]}:{ans[2]}"


for file in filter(lambda x: x.endswith(".txt"), os.listdir(args.input_folder)):
    output = rugby(open(f'{args.input_folder}/{file}', "r").read().strip())
    file = file.replace('.txt', '')
    w = open(f'{args.output_folder}/{file}_x12691yl.txt', "w")
    w.write(output)
    w.close()
