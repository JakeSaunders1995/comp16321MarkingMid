import os
import sys
file1 = sys.argv[2]
file_input = os.path.realpath(file1)
print(file_input)
for data in os.listdir(file_input):
    f = open(file_input + '/' + data, 'r')
    data = f.read()
    t1_score = 0
    t2_score = 0
    i = 1
    file2 = sys.argv[i]
    txt_name = os.path.realpath(data)
    file_output = os.path.realpath(file2)
    changename = txt_name.replace(".txt", "_s86124sy.txt")
    for i in range(len(data)):
        a = i + 1
        if data[i] =="1":
            i +=3
            if data[a] =="t":
                t1_score += 5
            elif data[a] =="c":
                t1_score += 2
            elif data[a] == "p":
                t1_score += 3
            else:
                t1_score += 3
        elif data[i] == "2":
            if data[a] == "t":
                t2_score += 5
            elif data[a] == "c":
                t2_score += 2
            elif data[a] == "p":
                t2_score += 3
            else:
                t2_score += 3
        i+=2
        final = open(os.path.join(file_output, changename), 'w')
    print(t1_score,":",t2_score,sep="")
