import os
import argparse


cwd = os.getcwd()
print(cwd)

parser = argparse.ArgumentParser(description="spellchecker")
parser.add_argument('inp1')
parser.add_argument('inp2')
parser.add_argument('out')
args = parser.parse_args()



def check(text,wor):
    up = 0
    pun = 0
    num = 0
    punct = '''.?!,;:—-()[]{}...@#!$%^&*_+~—'"'''
    txt = ""
    cor = 0
    inc = 0
    inco = []
    for x in text:
        if x in punct:
            pun += 1
        elif x.isdigit():
            num += 1
        elif x.isupper():
            up += 1
            txt += x.lower()
        else:
            txt += x
    for y in txt.split():
        if y not in wor:
            inc += 1
            inco.append(y)
        else:
            cor += 1
    return up,pun,num,len(txt.split()),cor,inc


dir = args.inp2
spath = args.out
for file in os.listdir(dir):
    if file.endswith(".txt"):                   #iterates through input folder and executes the function on any .txt file
        ope= os.path.join(args.inp2, file)
        f = open(args.inp1,"r")
        wor = f.read().splitlines()
        f.close()
        fle = open(ope,"r")
        text =fle.read()
        fle.close()
        a,b,c,d,e,f = check(text, wor)                                                              #a = up
        fname = file.replace(".txt","")                                                             #b = pun
        fname += "_y10240dt.txt"                                                                    #c = num
        path = os.path.join(spath, fname)                       #write file on a specific path      #d = len(txt.split())
        nf = open(path, "w")                                                                        #e = cor
        nf.write("y10240dt"+ "\n")                                                                  #f = inc
        nf.write("Formatting ###################"+ "\n")
        nf.write("Number of upper case words transformed: "+str(a)+ "\n")
        nf.write("Number of punctuation’s removed: "+str(b)+ "\n")
        nf.write("Number of numbers removed: "+str(c)+ "\n")
        nf.write("Spellchecking ###################"+ "\n")
        nf.write("Number of words in file: "+str(d)+ "\n")
        nf.write("Number of correct words in file: "+str(e)+ "\n")
        nf.write("Number of incorrect words in file: "+str(f)+ "\n")
        nf.close()
