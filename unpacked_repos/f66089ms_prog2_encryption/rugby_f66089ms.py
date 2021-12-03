import argparse
import os
import re

##Determine the score of each team based on the scoring types and quantity:
##• t = 5 points (Try)
##• c = 2 points (Goal kick)
##• p = 3 points (Penalty)
##• d = 3 points (Drop goal)


parser = argparse.ArgumentParser()
parser.add_argument('input_file', type=str, help = 'Enter input file path')
parser.add_argument('output_file', type=str, help = 'Enter input file path')
args = parser.parse_args()

input_file=args.input_file
output_file=args.output_file

files = os.listdir(input_file)

for z in files:
    in_put=open(os.path.join(input_file,z)).read()
    t1_point = 0
    t2_point = 0

    count = 0
    while count < len(in_put):
        if in_put[count] == '1':
            if in_put[count+1] == 't':
                t1_point += 5
            elif in_put[count+1] == 'c':
                t1_point += 2
            elif in_put[count+1] == 'p':
                t1_point += 3
            elif in_put[count+1] == 'd':
                t1_point +=3
            
        elif in_put[count] == '2':
            if in_put[count+1] == 't':
                t2_point += 5
            elif in_put[count+1] == 'c':
                t2_point += 2
            elif in_put[count+1] == 'p':
                t2_point += 3
            elif in_put[count+1] == 'd':
                t2_point +=3
        
        count+=1

    out = str(t1_point)+' : '+str(t2_point)


    n_file=re.split("[.]",z)[0] + "_f66089ms.txt"
    result=open(os.path.join(output_file,n_file),"w")
    result.write(out)

    result.close()






