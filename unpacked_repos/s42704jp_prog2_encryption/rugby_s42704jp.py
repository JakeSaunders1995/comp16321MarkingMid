
import sys

input_filepath = sys.argv[1]
output_filepath = sys.argv[2]

f = open(input_filepath,'r',encoding='utf-8')
f2 = open(output_filepath,'w',encoding='utf-8')
score = []
score = list(f.read())

one = 0  
two = 0  
i = 0
for i in range(len(score)):
    if score[i] == '1' or score[i] == '2':
        if score[i] == '1':
            i += 1
            if score[i] == 't':
                one += 5
                i += 2
            elif score[i] == 'c':
                one += 2
                i += 2
            elif score[i] == 'p':
                one += 3
                i += 2
            elif score[i] == 'd':
                one += 3
                i += 2
        elif score[i] == '2':
            i = i + 1
            if score[i] == 't':
                two += 5
                i += 2
            elif score[i] == 'c':
                two += 2
                i += 2
            elif score[i] == 'p':
                two += 3
                i += 2
            elif score[i] == 'd':
                two += 3
                i += 2

f2.write("{}:{}".format(one, two))
