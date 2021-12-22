import sys

input_filepath = sys.argv[1]
output_filepath = sys.argv[2]

f = open(input_filepath,'r',encoding='utf-8')
f2 = open(output_filepath,'w',encoding='utf-8')
score = []
score = list(f.read())

a = 0  # T1 Score
b = 0  # T2 Score
i = 0
n = 0
for i in range(len(score)):
    if score[i] == '1' or score[i] == '2':
        if score[i] == '1':
            i = i + 1
            if score[i] == 't':
                a += 5
                i += 2
            elif score[i] == 'c':
                a += 2
                i += 2
            elif score[i] == 'p':
                a += 3
                i += 2
            elif score[i] == 'd':
                a += 3
                i += 2
        elif score[i] == '2':
            i = i + 1
            if score[i] == 't':
                b += 5
                i += 2
            elif score[i] == 'c':
                b += 2
                i += 2
            elif score[i] == 'p':
                b += 3
                i += 2
            elif score[i] == 'd':
                b += 3
                i += 2

f2.write("{}:{}".format(a, b))
