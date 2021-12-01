#!/usr/bin/env python

import sys
import os

if(len(sys.argv) != 3):
    print('Incorrect number of arguments. Current number of arguments:' + str(len(sys.argv)))
    exit()

# print(sys.argv)

if(os.path.isdir(sys.argv[1])):
    if not os.path.exists(sys.argv[2]):
        os.makedirs(sys.argv[2])
    with os.scandir(sys.argv[1]) as dirs:
        for entry in dirs:
            current_node = sys.argv[1] + '/' + entry.name 
            node_split = os.path.splitext(current_node)
            filename_with_extension = os.path.basename(current_node)
            filename = filename_with_extension.split('.', 1)[0]
            output_path = sys.argv[2] + '/' + filename + '_j73849yh' + node_split[1]
            if(node_split[1].lower() == '.txt'):
                os.system('python3 ' + sys.argv[0] + ' ' + current_node + ' ' + output_path)
    exit()

fin = open(sys.argv[1], 'r')

var_score = [0, 0]

while(fin.read(1) == str('T')):
    # print('Start reading round.')
    tmp_team = int(fin.read(1))
    tmp_type = fin.read(1)
    if(tmp_type == 't'):
        var_score[tmp_team-1] = var_score[tmp_team-1]+5
    elif(tmp_type == 'c'):
        var_score[tmp_team-1] = var_score[tmp_team-1]+2
    elif(tmp_type == 'p'):
        var_score[tmp_team-1] = var_score[tmp_team-1]+3
    elif(tmp_type == 'd'):
        var_score[tmp_team-1] = var_score[tmp_team-1]+3

# print('Processing Complete.')
    
fout = open(sys.argv[2], 'w')
fout.write(str(var_score[0])+':'+str(var_score[1]))

exit