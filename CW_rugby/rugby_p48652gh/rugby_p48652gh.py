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
            b=0
            c=0
            d=int(len(a)/3)
            for e in range(d):
                i= e*3
                if a[i+1]  =='1':
                    if a[i+2]== 't':
                        b+=5
                    elif  a[i+2]=='c':
                        b+=2
                    elif a[i+2]  == 'p' or 'd':
                        b+= 3
                elif a[i+1] =='2':
                    if a[i+2]== 't':
                        c+=5
                    elif  a[i+2]=='c':
                        c+=2
                    elif a[i+2]  == 'p' or 'd':
                        c+= 3

            os.chdir('../')
            os.chdir(args.output)
            finaloutput= f[0:len(f)-4]+'_p48652gh.txt'



            outfile=open(finaloutput, 'w')


            outfile.write(str(b))
            outfile.write(':')
            outfile.write(str(c))
            os.chdir('../')
            os.chdir(args.file)
