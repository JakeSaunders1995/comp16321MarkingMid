import argparse,os,re
parser = argparse.ArgumentParser()
parser.add_argument('file')
parser.add_argument('print')
args = parser.parse_args()
startfile=os.listdir(args.file)
printfile=os.listdir(args.print)
t=0
while t<len(startfile):
    i=0
    t1=0
    t2=0
    openfile= args.file+"/"+startfile[t]
    text=open(openfile,"r")
    word=""
    while True :
        x=text.read(1)
        if not x :
            break
        word+=x
    text.close()

    m=len(word)
    while i < m-1 :
        if word[i]== "1" :
            u=word[i+1]
            if u=="t"  :
                t1=t1+5
            elif u=="c" :
                t1+=2
            elif u=="p" or u=="d":
                t1+=3
            u=0
        elif word[i]== "2" :
            u=word[i+1]
            if u=="t"  :
                t2=t1+5
            elif u=="c" :
                t2+=2
            elif u=="p" or u=="d":
                t2+=3
            u=0
        i+=1
    q=str(t1)+":"+str(t2)
    renamefile=startfile[t]
    renamed=renamefile[0:len(renamefile)-4]+"_m92824cm.txt"
    outputfile=open(renamed,"w")
    outputfile.write(str(q))
    outputfile.close()
    t+=1
