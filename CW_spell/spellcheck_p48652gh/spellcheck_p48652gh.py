import argparse
import os
parser=argparse.ArgumentParser()
parser.add_argument('words')
parser.add_argument('file')
parser.add_argument('output')
args=parser.parse_args()

os.chdir(args.file)
for f in os.listdir():
        inputfile=open(f,'r')

        a= inputfile.readline()



        os.chdir('../')

        b=len(a)

        i=0
        alphabet='abcdefghijklmnopqrstuvwxyz'
        capital= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        nums='1234567890'

        correct=0
        incorrect=0
        upper=0
        punc=0
        num=0
        word=0
        new=''


        while i<b:
            new=''
            letter=0
            t=i
            while a[t]!= ' ':
                if t==len(a)-1:
                    t+=1

                    break
                else:
                    t+=1

            v=a[i:t]
            c=0
            while c<=len(v)-1:
                if v[c] in alphabet:
                    letter+=1
                    new+=v[c]

                elif v[c] in capital:
                    upper+=1
                    for g in range(len(capital)):
                        if v[c] == capital[g]:
                            new+=alphabet[g]
                elif v[c] in nums:
                    num+=1
                else:
                    if c+2<=len(v)-1:
                        if v[c+1] == '.' and v[c+2] == '.':
                            c+=2

                    punc+=1
                    
                c+=1

            te=0



            file=open(args.words,'r')

            if letter>0:
                word+=1

                for line in file:
                    line= line.rstrip()

                    if line==new:

                        te+=1
                if te>0:
                    correct+=1


                else:
                    incorrect+=1

            te=0


            i=t+1


        os.chdir(args.output)
        finaloutput= f[0:len(f)-4]+'_p48652gh.txt'



        output_file=open(finaloutput, 'w')



        output_file.write('p48652gh\nFormatting ###################\nNumber of upper case letters changed: ')
        output_file.write(str(upper))
        output_file.write('\nNumber of punctuations removed: ')
        output_file.write(str(punc))
        output_file.write('\nNumber of numbers removed:')
        output_file.write(str(num))
        output_file.write('\nSpellchecking ###################\n')
        output_file.write('Number of words: ')
        output_file.write(str(word))
        output_file.write('\nNumber of correct words: ')
        output_file.write(str(correct))
        output_file.write('\nNumber of incorrect words: ')
        output_file.write(str(incorrect))
        os.chdir('../')
        os.chdir(args.file)
