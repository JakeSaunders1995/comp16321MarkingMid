import sys,os
files = os.listdir(sys.argv[1])
for j in files:
    path = sys.argv[1]+"/"+j
    file = open(path)
    string = file.read()
    file.close()
    t1Counter = 0
    t2Counter = 0
    def interpreter(character):
        if character == 't':
            return 5
        if character == 'c':
            return 2
        if character == 'p' or character == 'd':
            return 3
    for i in range(2,len(string),3):
        if string[i-1] == '1':
            t1Counter += interpreter(string[i])
        else:
            t2Counter += interpreter(string[i])
    path = sys.argv[2]+"/"+j.split(".")[0]+"_e41206gs."+j.split(".")[1]    
    file = open (path,"w")
    file.write(str(t1Counter)+':'+str(t2Counter))
    file.close()
