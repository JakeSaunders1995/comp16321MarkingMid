import sys
import os
path=sys.argv[1]
outputpath=sys.argv[2]
path_list = os.listdir(path)
path_list.sort()
num = 0
for filename in path_list:
    num = num + 1
    f = open(os.path.join(path,filename))
    day=f.read()
    t = 5
    c = 2
    p = 3
    d = 3
    i = 1
    T1 = 0
    T2 = 0
    while i < len(day):
        if int(day[i]) == 1:
            i += 1
            if (day[i]) == "t":
                answer1 = t
            elif (day[i]) == "p":
                answer1 = p
            elif (day[i]) == "d":
                answer1 = d
            else:
                answer1 = c
            T1 += answer1
        else:
            i += 1
            if (day[i]) == "t":
                answer2 = t
            elif (day[i]) == "p":
                answer2 = p
            elif (day[i]) == "d":
                answer2 = d
            else:
                answer2 = c
            T2 += answer2
        i += 2
    output_filename = 'test_file_j29403qy' + str(num) + '.txt'
    f1=open(os.path.join(outputpath,output_filename),'w')
    f1.write(str(T1)+":"+str(T2))
    f1.close()


