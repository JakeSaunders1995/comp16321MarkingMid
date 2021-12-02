import argparse
import os
parser=argparse.ArgumentParser()
parser.add_argument('file')
parser.add_argument('output')
args=parser.parse_args()
os.chdir(args.file)
for f in os.listdir():
        inputfile=open(f,'r')
        for line in inputfile:
            line=line.rstrip()
        a=line
        output_file=args.output
        if a[0] == 'C':
            al  = 'abcdefghijklmnopqrstuvwxyz'
            if a[14]=='-':
                b= int(a[15])  - 2*int(a[15])
            else:
                b= int(a[15])


            d=''
            for i in range(len(a)-18):
                c=0


                if a[i+18]!= ' ':
                    while al[c] != a[i+18]:
                        c+=1


                    d=d+al[c-b]

                else:
                    d=d+' '

            os.chdir('../')
            os.chdir(args.output)
            finaloutput= f[0:len(f)-4]+'_p48652gh.txt'



            outfile=open(finaloutput, 'w')
            outfile.write(d)
            os.chdir('../')
            os.chdir(args.file)

        elif a[0] == 'H':
            i=4
            d=''
            al= 'abcdefghijklmnopqrstuvwxyz'
            ca='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            while i<len(a):
                e=a[i] +a[i+1]
                m= chr(int(e,16))
                if m in ca:
                    for l in range(len(ca)):
                        if m == ca[l]:
                            d=d+al[l]
                else:
                    d=d+ chr(int(e,16))
                i+=3

            os.chdir('../')
            os.chdir(args.output)
            finaloutput= f[0:len(f)-4]+'_p48652gh.txt'



            outfile=open(finaloutput, 'w')
            outfile.write(d)
            os.chdir('../')
            os.chdir(args.file)


        elif a[0]=='M':

            word=''

            z = {'a': '.-', 'b': '-...',
                                   'c': '-.-.', 'd': '-..', 'e': '.',
                                   'f': '..-.', 'g': '--.', 'h': '....',
                                   'i': '..', 'j': '.---', 'k': '-.-',
                                   'l': '.-..', 'm': '--', 'n': '-.',
                                   'o': '---', 'p': '.--.', 'q': '--.-',
                                   'r': '.-.', 's': '...', 't': '-',
                                   'u': '..-', 'v': '...-', 'w': '.--',
                                   'x': '-..-', 'y': '-.--', 'z': '--..',
                                   '1': '.----', '2': '..---', '3': '...--',
                                   '4': '....-', '5': '.....', '6': '-....',
                                   '7': '--...', '8': '---..', '9': '----.',
                                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                                   '?': '..--..', '/': '-..-.', '-': '-....-',
                                   '(': '-.--.', ')': '-.--.-', ' ': '/'}
            i=11
            while i<len(a):

                t=i
                while a[t] != ' ':
                    if t==len(a)-1:
                        t+=1
                        break
                    else:
                        t+=1

                v=a[i:t]

                for key, value in z.items() :
                    if v == value:
                        word=word+key

                i=t+1


            os.chdir('../')
            os.chdir(args.output)
            finaloutput= f[0:len(f)-4]+'_p48652gh.txt'



            outfile=open(finaloutput, 'w')
            outfile.write(word)
            os.chdir('../')
            os.chdir(args.file)
