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
    y=[]
    z=[]
    for i in range (len(x)):
        if x[i]==':':
            y.append(x[0:i])
            z=x[i+1:]

    if y[0]=='Morse Code':
        mc=['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..','--..--','.-.-.-','..--..','-.-.--','-..-.','-....-','-.--.','-.--.-','---...']
        cl=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',',','.','?','!','/','-','(',')',':']

        l1=[]
        ans=[]
        sp=0
        for i in range (len(z)):
            if z[i]==' ':
                l1.append(z[sp:i])
                sp=i+1
        l1.append(z[sp:i])


        for i in range (len(l1)):
            for j in range (len(mc)):
                if l1[i]==mc[j]:
                    ans.append(cl[j])
            if l1[i]=='/':
                ans.append(' ')

        fn=fn[:-4]
        ofn=fn+'_n91131bw.txt'
        os.chdir(path2)
        zz=open(ofn, 'w')
        zz.write('')
        zz.close
        zz=open(ofn, 'a')

        for i in range (len(ans)):
            
            zz.write(ans[i])
        zz.close()

    elif y[0]=='Hex':

        ans=[]
        l1=[]
        sp=0
        for i in range (len(z)):
            if z[i]==' ':
                l1.append(z[sp:i])
                sp=i+1
        l1.append(z[sp:i])

        for i in range (len(l1)):
            ans.append(chr(int(l1[i],16)))
        fn=fn[:-4]
        ofn=fn+'_n91131bw.txt'
        os.chdir(path2)
        zz=open(ofn, 'w')
        zz.write('')
        zz.close
        zz=open(ofn, 'a')
        for i in range (len(ans)):
            zz.write(ans[i].lower())
        zz.close()
    elif y[0]=='Caesar Cipher(+3)':
        word=[]
        ans=[]
        l1=[]
        sp=0
        a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        for i in range (len(z)):
            if z[i]==' ':
                l1.append(z[sp:i])
                sp=i+1
        l1.append(z[sp:i])
        for i in range (len(l1)):
            for j in range(len(l1[i])):
                for k in range(len(a)):
                    if l1[i][j]==a[k]:
                        ans.append(a[k-3])
            ans.append(' ')

        fn=fn[:-4]
        ofn=fn+'_n91131bw.txt'
        os.chdir(path2)
        zz=open(ofn, 'w')
        zz.write('')
        zz.close
        zz=open(ofn, 'a')
        for i in range (len(ans)):
            
            zz.write(ans[i])
        zz.close()
       


        
        

