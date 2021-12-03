import argparse
import sys
import os

# path = "/home/csimage/Downloads/midterm_files(1)/midterm_files/Example_inputs/Example_inputs_program1"



score_list = []

sorted_path_list = sorted(os.listdir(path))


for filename in sorted_path_list:
   with open(os.path.join(path, filename), 'r') as f:
       text = f.read()
       #print(text)


       score_dic = {"t":5, "c":2, "p":3, "d":3}

       team_score = [0, 0]

       while len(text) != 0:
           team_type = int(text[1])

           if team_type == 1:

               team_score[0] = team_score[0] + score_dic[text[2]]
           else:

               team_score[1] = team_score[1] + score_dic[text[2]]
           if len(text) == 3:
               break
           text = text[3:]




       actual_score = str(team_score[0]) + ":" + str(team_score[1])
       score_list.append(actual_score)

for i,k in enumerate(score_list):


    output = open('/home/csimage/python_midterm/test_file' + str(i+1)+ '_m57983ma', 'w')
    
    output.write(k)
