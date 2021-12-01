# a program written by Hanmin.L
# calculate the total score with a sum of the string
# input a single series of team scoring
# t = 5; c = 2; p = 3; d = 3;
# output the result into the file .txt

import os
import argparse

# initialize the command line
parser = argparse.ArgumentParser()
parser.add_argument("fin", help="state the input file dir here")
parser.add_argument("fout", help="state the output file dir here")
args = parser.parse_args()

# names in the input dir
input_folder = os.scandir(args.fin)

# find the input test file
for input_name in input_folder:
    #if("r00979hl" not in input_name.name):
    if(True):
        # initialize file input and output
        f = open(input_name)
        output_name = input_name.name.replace(".txt","_r00979hl.txt")
        g = open(str(args.fout)+"/"+output_name, "w")

        # main body begin
        # read the string
        strIn = f.readline()
        # find the 'Tx' score in string
        def Tx_sum(x):
            count = 0
            for i in range(len(strIn)):
                if(strIn[i] == x):
                    if(strIn[i+1] == 't'):
                        count += 5
                    elif(strIn[i+1] == 'c'):
                        count += 2
                    elif(strIn[i+1] == 'p'):
                        count += 3
                    elif(strIn[i+1] == 'd'):
                        count += 3
                    else:
                        continue
            return count
        # main
        g.write(str(Tx_sum('1')) + ":" + str(Tx_sum('2')))
        # main body end

        # file closing
        f.close()
        g.close()
