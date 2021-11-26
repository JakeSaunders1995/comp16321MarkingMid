import os, sys

for file in os.listdir(sys.argv[1]):  
    os.chdir('..')
    os.chdir(sys.argv[1])
    score = open(file, 'r')
    info = score.read()
    b = info.rstrip()
    time = int(len(b)/3)
    List = list(b)
    j = 0
    t1score = 0
    t2score = 0
    for i in range(0, time):
        a = List[j:j+3]
        temp = 0
        if a[2] == 't':
            temp = 5
        elif a[2] == 'p':
            temp = 3
        elif a[2] == 'c':
            temp = 2
        elif a[2] == 'd':
            temp = 3
        if a[1] == '1':
            t1score = t1score + temp
        elif a[1] == '2':
            t2score = t2score + temp
        j += 3
    final = str(t1score)+":"+str(t2score)
    os.chdir('..')
    os.chdir(sys.argv[2])
    name = os.path.basename(file).split('.')[0]
    output = open(name+"_y55928xn.txt", 'x')
    output.write(final)
    

