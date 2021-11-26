import argparse,os,re
parser = argparse.ArgumentParser()
parser.add_argument("eng")
parser.add_argument("input")
parser.add_argument("output")
args = parser.parse_args()

path1=args.input
path2=args.output
engpath=args.eng

os.chdir(path1)
engfile=open(engpath,'r')
eng=[]
engo=engfile.readline().split()
eng.append('a')
for i in engfile:
    aa=i.strip()
    eng.append(aa)

engfile.close()
let=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
uet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
num=['0','1','2','3','4','5','6','7','8','9']
acc=[]

f=False
for fn in os.listdir(os.getcwd()):
    os.chdir(path1)
    f=open(os.path.join(os.getcwd(),fn), 'r')
    x=f.read()
    nco=0#num counter
    uco=0#upper case counter
    pco=0#punchuation counter
    for i in range (len(x)):
        f=False
        if x[i]==' ':
            #acc.append(' ')
            f=True
        for j in range(len(let)):
            if x[i]==let[j]:
                #acc.append(let[j])
                f=True
            elif x[i]==uet[j]:
                #acc.append(let[j])
                uco+=1
                f=True
        for k in range(len(num)):
            if x[i]==num[k]:
                nco+=1
                f=True
        if f==False:
            if i+2 <= len(x):
                if x[i]=='.' and x[i+1] == '.' and x[i+2]=='.':
                    i+=2
            
            pco+=1
    x=x.lower()
    x=re.sub("\d","",x)
    x=re.sub("[^\w\s]|_","",x)
    x=re.sub(" +"," ",x)
    
    x=x.split(' ')
    cco=0
    
    for i in range(len(x)):
        for j in range (len(eng)):
            if eng[j]==x[i]:
                cco+=1
                

                
        
            
    wco=len(x)
    ico=len(x)-cco
    xx='Number of upper case words changed: '+str(uco)
    yy="Number of punctuations removed: "+str(pco)
    z2="Number of numbers removed: "+str(nco)
    x1='Number of words: '+str(wco)
    y1='Number of correct words: '+str(cco)
    z1='Number of incorrect words: '+str(ico)
    
    fn=fn[:-4]
    ofn=fn+'_n91131bw.txt'
    os.chdir(path2)
    zz=open(ofn, 'w')
    zz.write('')
    zz.close
    zz=open(ofn, 'a')
    zz.write('n91131bw\n')
    zz.write('Formatting ###################\n')
    zz.write(str(xx))
    zz.write('\n')
    zz.write(str(yy))
    zz.write('\n')
    zz.write(str(z2))
    zz.write('\n')
    zz.write('Spellchecking ###################\n')
    zz.write(str(x1))
    zz.write('\n')
    zz.write(str(y1))
    zz.write('\n')
    zz.write(str(z1))
    



    
        
    
        
