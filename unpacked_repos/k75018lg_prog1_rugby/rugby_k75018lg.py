import argparse
import os
parser = argparse.ArgumentParser(description='input and output')
parser.add_argument('input', type=str, help='Input')
parser.add_argument('output', type=str, help='Output')
args = parser.parse_args()
path1 = args.input
path2 = args.output
fl =[i for i in os.listdir(path1)]
filelist1 = [path1 + i for i in os.listdir(path1)]
for files in filelist1:
    index = filelist1.index(files)
    file = open(files)
    record = file.read()
    file.close()
    record = record.strip()
    t1_score = 0
    t2_score = 0
    index1 = 1
    index2 = 2
    while True:
        if record[index2] == "t":
            if record[index1] == "1":
                t1_score += 5
            else:
                t2_score += 5
        elif record[index2] == "c":
            if record[index1] == "1":
                t1_score += 2
            else:
                t2_score += 2
        elif record[index2] == "p":
            if record[index1] == "1":
                t1_score += 3
            else:
                t2_score += 3
        elif record[index2] == "d":
            if record[index1] == "1":
                t1_score += 3
            else:
                t2_score += 3
        index1 += 3
        index2 += 3
        if index1 > len(record):
            break


    filename = fl[index]
    filename = filename[:-4]+"_k75018lg.txt"
    create = open(path2+filename,"w")
    create.write("%d:%d" %(t1_score, t2_score))
    create.close()
