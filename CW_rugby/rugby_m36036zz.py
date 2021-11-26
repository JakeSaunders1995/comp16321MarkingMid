import argparse
import os
from pathlib import Path

parser = argparse.ArgumentParser(description='')
parser = argparse.ArgumentParser(description='')
parser.add_argument('path', metavar='p', type=str, nargs='+')
parser.add_argument('path2', metavar='p', type=str, nargs='+')

#read
args = parser.parse_args()
path = Path(args.path[0])
l = []

for p in path.glob('*'):
    l.append(str(p))

for q in l:
    print(q)
    l1 = []
    l2 = []
    with open(q,'r') as f:
        content=(''.join(f.read())).strip('\n')

    #分割+储存列表
    t1 = content.split('T')

    for i in t1:
        find = i.find('1')
        if find == 0:
            l1.append(''.join(i.split('1')))
        else:
            l2.append(''.join(i.split('2')))

    #分别计算
    l3 = ['t','c','p','d']
    point = [5,2,3,3]
    total1 = 0
    total2 = 0

    for i in l1:
        for z in l3:
            if str(i)==str(z):
                total1 += point[l3.index(z)]

    for k in l2:
        for w in l3:
            if str(k)==str(w):
                total2 += point[l3.index(w)]

    #对比
    if total1 > total2:
        print('winner is team1')
    elif total1 < total2:
        print('winner is team2')
    elif total1 == total2:
        print('draw')

    #write
    a=str(total1)
    b=str(total2)

    for ii in range(len(l)):
            path2 = parser.parse_args().path2[0]
            p = Path(path2)
            nn=str((os.path.basename(q))[:-4])+'_m36036zz.txt'
            file2 = p / nn
            with file2.open('w') as ff:
                ff.write(a+':'+b)
 
        
       
 


