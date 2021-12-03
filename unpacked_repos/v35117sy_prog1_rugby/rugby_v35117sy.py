import argparse
import os

parser = argparse.ArgumentParser(description='input and output')
parser.add_argument('inputpath', type=str, help='input')
parser.add_argument('outputpath', type=str, help='output')
args = parser.parse_args()

inputpath = args.inputpath
outputpath = args.outputpath
dirs = os.listdir(args.inputpath)

for file in dirs:
    f = open(inputpath +'/' + file)
    input = f.readline()
    T1sco = 0
    T2sco = 0
    for i in range(0, len(input), 3):
        if input[i:i+2] == 'T1':
          if input[i+2] == 'c':
            T1sco += 2
          elif input[i+2] == 'p':
              T1sco += 3
          elif input[i+2] == 'd':
              T1sco += 3
          elif input[i+2] == 't':
              T1sco += 5
        elif input[i:i+2] == 'T2':
            if input[i+2] == 'c':
                T2sco += 2
            elif input[i+2] == 'p':
                T2sco += 3
            elif input[i+ 2] == 'd':
                T2sco += 3
            elif input[i + 2] == 't':
                T2sco += 5

    f = open(outputpath +'/'+ file.split('.')[0] + "_v35117sy", "w")
    f.write("%s : %s" % (T1sco, T2sco))
    f.close()