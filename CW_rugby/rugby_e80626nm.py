import os, argparse

parse = argparse.ArgumentParser()
parse.add_argument('directory', nargs='+')
args = parse.parse_args()
files = os.listdir(args.directory[0])

results = []
lines = []

if not os.path.exists(args.directory[1]):
    os.mkdir(args.directory[1])


for theFile in files:
    with open(args.directory[0]+'/'+ theFile, 'r') as line:
        line = line.read()
        for i in range(len(theFile)):
            if theFile[i:i+4] == '.txt':
                fileName = theFile[:i]
            T1 = 0
            T2 = 0
            for i in range(len(line)):

                if line[i] == 'T':
                    continue

                elif line[i] == '1':
                    i += 1
                    if line[i] == 't':
                        T1 += 5
                    elif line[i] == 'p' or line[i] == 'd':
                        T1 += 3
                    elif line[i] == 'c':
                        T1 += 2

                elif line[i] == '2':
                    i += 1
                    if line[i] == 't':
                        T2 += 5
                    elif line[i] == 'p' or line[i] == 'd':
                        T2 += 3
                    elif line[i] == 'c':
                        T2 += 2

            result = f'{T1}:{T2}'
            with open(f'{args.directory[1]}/{theFile}_e80626nm.txt', 'w') as file:
                file.write(result)

