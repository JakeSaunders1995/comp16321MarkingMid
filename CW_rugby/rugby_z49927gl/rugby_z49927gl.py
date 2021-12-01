#fixed
import os
import sys
from pathlib import Path
import ntpath

fin = sys.argv[1]
fout = sys.argv[2]
for fin in os.scandir(fin):
    file = open(fin.path, 'r')
    my_list = file.readline().strip()
    file.close()
    countTeamOne = 0
    countTeamTwo = 0
    i = 0
    l = len(str(my_list))
    while i < l:
        #first team points
        if my_list[i+1] == str(1) and my_list[i+2] == str("t"):
            countTeamOne = countTeamOne + 5
        elif my_list[i+1] == str(1) and my_list[i+2] == str("c"):
            countTeamOne = countTeamOne + 2
        elif my_list[i+1] == str(1) and my_list[i+2] == str("p"):
            countTeamOne = countTeamOne + 3
        elif my_list[i+1] == str(1) and my_list[i+2] == str("d"):
            countTeamOne = countTeamOne + 3
    #second team points
        elif my_list[i+1] == str(2) and my_list[i+2] == str("t"):
            countTeamTwo = countTeamTwo + 5
        elif my_list[i+1] == str(2) and my_list[i+2] == str("c"):
            countTeamTwo = countTeamTwo + 2
        elif my_list[i+1] == str(2) and my_list[i+2] == str("p"):
            countTeamTwo = countTeamTwo + 3
        elif my_list[i+1] == str(2) and my_list[i+2] == str("d"):
            countTeamTwo = countTeamTwo + 3
        i = i + 3
    result = ''
    result = result + str(countTeamOne) + ":" + str(countTeamTwo)
    out_file = Path(fin).stem + "_z49927gl.txt"
    out_file = os.path.join(fout, out_file)
    output = open(out_file, 'w+')
    output.write(str(result))
    output.close()
