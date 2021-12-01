import sys, os
a=sys.argv[1]
b=os.listdir(a)
for c in b:
    d=a+"/"+c
    with open(d, 'r') as results:
        T1=0
        T2=0
        results=results.read()
        x=0
        while x<len(results):
            if results[x]=="T":
                x+=1
                if results[x]=="1":
                    x+=1
                    if results[x]=="t":
                        T1+=5
                        x+=1
                    elif results[x]=="c":
                        T1+=2
                        x+=1
                    elif results[x]=="p":
                        T1+=3
                        x+=1
                    elif results[x]=="d":
                        T1+=3
                        x+=1
                    else:
                        print("unsupported input, check it")
                        break
                elif results[x]=="2":
                    x+=1
                    if results[x]=="t":
                        T2+=5
                        x+=1
                    elif results[x]=="c":
                        T2+=2
                        x+=1
                    elif results[x]=="p":
                        T2+=3
                        x+=1
                    elif results[x]=="d":
                        T2+=3
                        x+=1
                    else:
                        print("unsupported input, check it")
                        break
                else:
                    print("unsupported input, check it")
                    break
            else:
                print("unsupported input, check it")
        if T1>T2:
            print("T1 won")
        elif T2>T1:
            print("T2 won")
        else:
            print("draw")
    e=c.replace('.txt','')
    w=sys.argv[2]+'/'+e+"_n37169dk"+".txt"
    x=open(w,'w')
    x.write(str(T1)+":"+str(T2))
