import argparse,os
parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("output")
args = parser.parse_args()

path1=args.input
path2=args.output
os.chdir(path1)
for fn in os.listdir(os.getcwd()):
    os.chdir(path1)
    f=open(os.path.join(os.getcwd(),fn), 'r')
    x=f.readline()
    f.close()

    t=5
    c=2
    p=3
    d=3
    T1=0
    T2=0
    list=[]
    y=int(len(x)/3)
    sp=int(0)
    for i in range (y):
        list.append(x[sp:sp+3])
        sp=sp+3
        i+=1
    for i in range (len(list)):

        if list[i][1]==str(1):

            if list[i][2]=='t':
                T1+=t
            if list[i][2]=='c':
                T1+=c
            if list[i][2]=='p':
                T1+=p
            if list[i][2]=='d':
                T1+=d
        else:
    
            if list[i][2]=='t':
                T2+=t
            if list[i][2]=='c':
                T2+=c
            if list[i][2]=='p':
                T2+=p
            if list[i][2]=='d':
                T2+=d
    if T1>T2:
        print('T1 wins')
    elif T2>T1:
        print('T2 wins')
    else:
        print('draw')
    output=str(T1)+':'+str(T2)
    fn=fn[:-4]
    ofn=fn+'_n91131bw.txt'
    os.chdir(path2)
    z=open(ofn, 'w')
    z.write(output)
    z.close()

