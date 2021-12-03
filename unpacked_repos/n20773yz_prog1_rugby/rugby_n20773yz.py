import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("input", help="input folder path")
parser.add_argument("output", help="output folder path")
args = parser.parse_args()

inputPath = args.input
outputPath = args.output

inputFiles = sorted(os.listdir(inputPath))
outputFiles = sorted(os.listdir(outputPath))

file_num = 0
for x in inputFiles:
    file_num += 1
    input_file = inputPath + '/' + x
    with open(input_file) as inputFile:
        content = inputFile.read()
    inputFile.close()

    index = 0
    T1 = 0
    T2 = 0
    for i in content:
        if i == '1':
            if content[index + 1] == 't':
                T1 += 5
            elif content[index + 1] == 'c':
                T1 += 2
            elif content[index + 1] == 'p':
                T1 += 3
            elif content[index + 1] == 'd':
                T1 += 3
        elif i == '2':
            if content[index + 1] == 't':
                T2 += 5
            elif content[index + 1] == 'c':
                T2 += 2
            elif content[index + 1] == 'p':
                T2 += 3
            elif content[index + 1] == 'd':
                T2 += 3
        index += 1
    score = str(T1) + ':' + str(T2)

    if file_num > len(outputFiles):
        output_file = outputPath + '/' + x.replace('.txt', '_n20773yz.txt')
    else:
        output_file = outputPath + '/' + outputFiles[file_num - 1]
    outputFile = open(output_file, "w")
    outputFile.write(score)
    outputFile.close()
    os.rename(output_file, outputPath + '/' + x.replace('.txt', '_n20773yz.txt'))