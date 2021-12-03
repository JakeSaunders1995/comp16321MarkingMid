#open and read a txtfile
import sys
import re
import os
import argparse

parser = argparse.ArgumentParser(description='Add the file path')
parser.add_argument('input', type=str, help="file path")
parser.add_argument('output', type=str, help='filepath')



args = parser.parse_args()


def rugby(textdata):
    #set two variables one for T1 and T2
    T1 = 0
    T2 = 0
    #set variables for all the ways of scoring.
    t=5
    c=2
    p=3
    d=3
    # if t


    #split the text into groups of three, first two symbols refer


    #textdata[i:i+n] for i in range (0, len(textdata), n):
    #    print(textdata[i])


    split_string = re.findall('...', textdata)

    for x in split_string:
        if x[1] == str(1):
            if x[2] == "t":
                T1 += t
            if x[2] == "c":
                T1 += c
            if x[2] == "p":
                T1 += p
            if x[2] == "d":
                T1 += d

        if x[1] == str(2):
            if x[2] == "t":
                T2 += t
            if x[2] == "c":
                T2 += c
            if x[2] == "p":
                T2 += p
            if x[2] == "d":
                T2 += d


    scores = (str(T1)+":"+str(T2))
    print(scores)
    f = open(args.output+filename, "a")
    f.write(scores)
    f.close()
    file_change = (os.path.splitext(args.output+filename)[0])
    # print(file_change)
    # os.rename(file_change, file_change + '_w64810ak.txt')
    old_file = os.path.join(args.output, filename)
    new_file = os.path.join(args.output, file_change+'_w64810ak.txt')
    os.rename(old_file, new_file)
for filename in os.listdir(args.input):
    if filename.endswith(".txt"):
        f = open(args.input+ '/'+filename)
        rugby(f.readline())









#to the team
#last symbol is the type of scoring

#run through the whole text file using a for loop

#he first two symbols are T1, add to the T1 variable, the points
# from the third symbol

#compare T1 and T2 once the loop is finished.
#output the score into a text file.
