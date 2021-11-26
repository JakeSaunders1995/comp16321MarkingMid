from argparse import ArgumentParser
import os

def give_score(s):
    if s == 't':
        return 5
    elif s == 'c':
        return 2
    elif s == 'p':
        return 3
    elif s == 'd':
        return 3

parser = ArgumentParser()
parser.add_argument('input_folder')
parser.add_argument('output_folder')
args = parser.parse_args()

dirname_i = args.input_folder
dirname_o = args.output_folder
for filename in os.listdir(args.input_folder):
   with open(os.path.join(dirname_i, filename)) as f:
       score = f.read()
       length = int(len(score) / 3)

       T1_score = 0
       T2_score = 0
       winner = ""

       for i in range(length):
           if score[:2] == "T1":
               T1_score += give_score(score[2])
               score = score[3:]

           elif score[:2] == "T2":
               T2_score += give_score(score[2])
               score = score[3:]

       if T1_score > T2_score:
           winner = "T1"

       elif T1_score < T2_score:
           winner = "T2"

       elif T1_score == T2_score:
           winner = "draw"

       filename_o = filename.split(".")[0] + "_y44694jk.txt"
       with open(os.path.join(dirname_o, filename_o), 'w') as f_o:
           f_o.write(str(T1_score) + ":" + str(T2_score))
