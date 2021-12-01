import os,sys


#print(score_t2)
#print(score_t1)
def score_count(team):
    score = 0
    for k in team:
        if k=='t':
            score+=5
        elif k=='c':
            score+=2
        elif k=='p':
            score+=3
        elif k=='d':
            score+=3

    return score

inp_file = sys.argv[1]
ba= os.listdir(inp_file)

for k in ba:
    r= inp_file+"/"+k
    with open(r,'r') as file:
        c = file.readlines()
        a = c[0]
        #print(a)
        i=0
        b = len(a)
        #print(b)
        j=0
        score_t1= []
        score_t2 = []
        for i in range(int(b/3)):
            #print(a[j:j+3])
            num = a[j:j+3]
            j+=3
            if num[0:2] == "T1":
                score_t1.append(num[2])
            else:
                score_t2.append(num[2])

        t1_score= str(score_count(score_t1))
        t2_score = str(score_count(score_t2))
        final_score = t1_score+":"+t2_score


    g= k.replace('.txt','')
    w= sys.argv[2]+"/"+g+"_g39786dp"+".txt"
    x = open(w,'w')
    x.write(final_score)
