import argparse
import os
parser = argparse.ArgumentParser()
parser.add_argument('inp', type=str, help="path of input file")
parser.add_argument('outp', type=str, help="path of output file")
args = parser.parse_args()
if os.path.exists(args.inp):
    files_in=os.listdir(args.inp)
for file in files_in:
    input_file = open(args.inp+'/'+file)
    s=input_file.read()
    input_file.close()
    t1score, t2score = 0, 0
    rule = {'t': 5, 'c': 2, 'p': 3, 'd': 3}
    for i in range(0, int(len(s) / 3)):
        i *= 3
        if s[i + 1] == '1':
            t1score += rule[s[i + 2]]
        else:
            t2score += rule[s[i + 2]]
    output_file = open(args.outp+'/'+file[:-4]+"_j23676kd.txt", "w")
    output_file.write(str(t1score) + ':' + str(t2score))
    output_file.close()
