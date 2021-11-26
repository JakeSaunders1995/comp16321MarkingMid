import argparse,os,re
parser = argparse.ArgumentParser()
parser.add_argument('english')
parser.add_argument('file')
parser.add_argument('print')
args = parser.parse_args()

startfile=os.listdir(args.file)
printfile=os.listdir(args.print)
t=0
while t<len(startfile):
    word=open(args.english,"r")
    openfile= args.file+"/"+startfile[t]
    text=open(openfile,"r")
    enlist=[]
    while True :
        x=word.readline()
        if not x :
            break
        enlist.append(x)
    string=""
    while True :
        x=text.read(1)
        if not x :
            break
        string+=x
    #text.close()
    m=len(string)
    new=""
    up=0
    pu=0
    nu=0
    for x in string :
        stringchar=x
        ASCIIValue=ord(stringchar)
        if ((ASCIIValue >= 97 and ASCIIValue <= 122) or ASCIIValue == 32) :
            new+=chr(ASCIIValue)
        elif (ASCIIValue >= 65 and ASCIIValue <= 90) :
            up+=1
            new+=chr(ASCIIValue+32)
        elif ASCIIValue <= 47 or (ASCIIValue >= 58 and ASCIIValue <= 64) or (ASCIIValue >= 91 and ASCIIValue <= 96):
            pu+=1
        else:
            nu+=1
    list=new.split(" ")
    w=0
    ww=0
    for n in list:
        w+=1
    cw=0
    inw=0
    f=0
    ew=0
    nlist=[]
    for n in enlist:
        nlist.append(n.strip())
        ew+=1
    k=0
    for x in list:
        if x in nlist:
            cw+=1
    inw=w-cw
    renamefile=startfile[t]
    renamed=renamefile[0:len(renamefile)-4]+"_m92824cm.txt"
    outputfile=open(renamed,"w")
    outputfile.write("m92824cm")
    outputfile.write("\nFormatting ###################")
    outputfile.write("\nNumber of upper case words transformed:")
    outputfile.write(str(up))
    outputfile.write("\nNumber of punctuation’s removed:")
    outputfile.write(str(pu))
    outputfile.write("\nNumber of numbers removed:")
    outputfile.write(str(nu))
    outputfile.write("\nSpellchecking ###################")
    outputfile.write("\nNumber of words in file:")
    outputfile.write(str(w))
    outputfile.write("\nNumber of correct words in file:")
    outputfile.write(str(cw))
    outputfile.write("\nNumber of incorrect words in file:")
    outputfile.write(str(inw))
    outputfile.close()
    t+=1
    word.close()
