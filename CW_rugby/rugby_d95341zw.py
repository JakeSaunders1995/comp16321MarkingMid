import os,argparse,re

parser = argparse.ArgumentParser()
parser.add_argument("dir", nargs='+')
#parser.add_argument("bbb")
args = parser.parse_args()
#args.aaa[0]
#x=args.aaa
#y=args.bbb
# scoring types and quantity:
t = 5
c = 2
p = 3
d = 3
a = os.listdir(args.dir[0])
for i in range(0, len(a)):
    b=args.dir[0]+"/"+a[i]
    c=args.dir[1]+"/"+a[i]
    d=c.replace(".", "_d95341zw.")
    #print(b)
#for i in
    scores1 = open(b, "r")
    scores2 = (scores1.read())
#print(scores2)
    list1=[]
    temp1=int(len(scores2)/3)
    #print(temp1)
    temp2=0
    temp3=3
    for i in range(temp1):
        list1.append(scores2[temp2:temp3])
        temp2 +=3
        temp3 +=3
    #print(list1)



    t1 = 0
    t2 = 0
    i = 0
    #print(len(list1))
    for i in range(len(list1)):
        if list1[i][1] == str(1):
            if list1[i][2] == str("t"):
                t1 = t1 + 5
            elif list1[i][2] == str("c"):
                t1 = t1 + 2

            elif list1[i][2] == str("p"):
                t1 = t1 + 3
            else:
            #list1[i][2] == str(d):
                t1 = t1 + 3

        else:
            if list1[i][2] == str("t"):
                t2 = t2 + 5
                #print(t2)
            elif list1[i][2] == str("c"):
                t2 = t2 + 2

            elif list1[i][2] == str("p"):
                t2 = t2 + 3
            else:
            #list1[i][2] == str(d):
                t2 = t2 + 3
                #print(t2)

    #print(t1, t2)
    result = open(d, "w")
#finalResult=
    s=str(t1) + ":" +str(t2)
    result.write(s)
    #print(c)
    #print(str(t1) + ":"+ str(t2))
    result.close()
    scores1.close()

