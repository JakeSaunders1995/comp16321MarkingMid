import argparse
import os
parser = argparse.ArgumentParser()
parser.add_argument('input_file_n05919ah')
parser.add_argument('output_file_n05919ah')
args = parser.parse_args()

input_folder = args.input_file_n05919ah
for file in os.listdir(input_folder):
    filepath = os.path.join(input_folder,file )
    text = open(filepath, 'r')
    scoresheet = text.readline()
    length = len(scoresheet)
    score1 = 0
    score2 = 0
    t = 5
    c = 2
    p = 3
    d = 3
    i = 1
    while length >= i:
            if scoresheet[i] == '1':
                if scoresheet[i+1] == 't':
                    score1 += t
                elif scoresheet[i+1] == 'c':
                    score1 += c
                elif scoresheet[i+1] == 'p':
                    score1 += p
                else:
                    score1 += d
            else:
                if scoresheet[i+1] == 't':
                    score2 += t
                elif scoresheet[i+1] == 'c':
                    score2 += c
                elif scoresheet[i+1] == 'p':
                    score2 += p
                else:
                    score2 += d
            i += 3
    result = str(score1)+':'+str(score2)    
    print(result)
    output_folder = args.output_file_n05919ah
    a = os.path.splitext(file)
    output_file =  a[0] + '_n05919ah'+'.txt'
    print(output_file)
    output_path =  os.path.join(output_folder,output_file )
    f = open(output_path, "w")
    f.write(result)
    f.close()