import sys
import os

input_path = sys.argv[1]
output_path = sys.argv[2]

input_list = os.listdir(input_path)
input_list.sort()
output_list = os.listdir(output_path)

for file in input_list:
    with open(input_path + file, "r") as fr:
        data = fr.read()
        T = [0, 0]
        i = 0
        while i < len(data):
            team = -1
            st = data[i:i+3]
            team = int(st[1]) - 1
            ch = st[2]
            if ch == 't':
                id = team
                T[id] += 5
            elif ch == 'c':
                id = team
                T[id] += 2
            elif ch == 'p':
                id = team
                T[id] += 3
            elif ch == 'd':
                id = team
                T[id] += 3
            i = i + 3
    output_file = file[0:10] + '_[j29115zl]' + file[10:]
    with open(output_path + output_file, "w+") as fw:
        fw.write(str(T[0]) + ':' + str(T[1]) + "\n")
        
                    
