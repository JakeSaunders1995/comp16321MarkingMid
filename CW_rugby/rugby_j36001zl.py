import argparse
import re
import os

parser = argparse.ArgumentParser(description="I/O file path")
parser.add_argument("input_folder_path")
parser.add_argument("output_folder_path")
args = parser.parse_args()


def ChangePoint(point):
    if point == "t":
        return 5
    elif point == "c":
        return 2
    elif point == "p":
        return 3
    elif point == "d":
        return 3
    else:
        return 0


def ReadData(filepath):
    global T1
    global T2
    file = open(filepath, 'r')
    filedata = re.findall(r'.{3}', file.read())  # Split every 3 characters
    for i in filedata:
        if i[:2] == "T1":
            T1 += ChangePoint(i[2:])
        elif i[:2] == "T2":
            T2 += ChangePoint(i[2:])
    file.close()


def WriteResult(folder, outputfilename):
    global T1
    global T2
    file = open(f"{folder}/{outputfilename[:-4]}_j36001zl.txt", 'w')
    file.write(f"{T1}:{T2}")
    file.close()


for filename in os.listdir(args.input_folder_path):
    T1 = 0
    T2 = 0
    ReadData(f"{args.input_folder_path}/{filename}")
    WriteResult(args.output_folder_path, filename)
