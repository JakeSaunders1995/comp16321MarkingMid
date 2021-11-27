import argparse
import os

parse = argparse.ArgumentParser(description='input test file folder path and output file folder path')
parse.add_argument('paths', type=str, nargs='+', help='file folder paths')
args = parse.parse_args()

inputfilelist= []
outputfilelist = []
for outfpath,outdirname,outfilename in os.walk(args.paths[1]):
    continue

for fpath,dirname,fname in os.walk(args.paths[0]):
    for i in fname:
        inputfilelist.append(fpath + '/' + i)
        outputfilelist.append(outfpath + '/' + i[:-4] + '_c74752hz.txt')

for j in range(0,len(inputfilelist)):
    index1 = 1
    index2 = 2
    t = 5
    c = 2
    p = 3
    d = 3
    T1score = 0
    T2score = 0

    with open(inputfilelist[j],mode='r') as f1:
        text = f1.read()
        # print(text)
        while index1 < len(text):
            if text[index1] == '1':
                if text[index2] == 't':
                    T1score += t
                elif text[index2] == 'c':
                    T1score += c
                elif text[index2] == 'p':
                    T1score += p
                elif text[index2] == 'd':
                    T1score += d
                index1 += 3
                index2 += 3
            elif text[index1] == '2':
                if text[index2] == 't':
                    T2score += t
                elif text[index2] == 'c':
                    T2score += c
                elif text[index2] == 'p':
                    T2score += p
                elif text[index2] == 'd':
                    T2score += d
                index1 += 3
                index2 += 3

    print('%s : T1:T2 = %d:%d'%(inputfilelist[j],T1score,T2score))
    with open(outputfilelist[j],mode='w') as f2:
        f2.write(str(T1score) + ':' + str(T2score))