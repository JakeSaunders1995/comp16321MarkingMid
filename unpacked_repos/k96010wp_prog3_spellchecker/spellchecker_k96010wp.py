#!/usr/bin/env python3
import argparse,os
parser = argparse.ArgumentParser()
parser.add_argument('spell')
parser.add_argument('inf')
parser.add_argument('outf')
args=parser.parse_args()

path, dirs, files = next(os.walk(args.inf))

fileCount = files
print(path)
for i in files:
    ifile = path+"/" +i
    ofile = args.outf+ "/"+ i[0:-4] + "_k96010wp.txt"
    inp = open(ifile).read()+" "
    cWord= ""
    output=""
    wordlist = open(parser.spell).read().split("\n")
    #this is all written under the assumption i cant use regex qwq
    nums=0
    punc=0
    ucount=0
    words=0
    cwords=0
    iwords=0
    isUpper=False
    for char in inp:
        code = ord(char)
        if (code>=65 and code <(65+26)):
            code+=32
            isUpper=True

        if (code >= 96 and code < (96+26)):
            cWord+=chr(code)
        elif code == 32 or code == 10:
            # process word
            if len(cWord)==0:
                continue
            words+=1
            if(isUpper):
                ucount+=1
            if cWord in wordlist:
                cwords+=1
            else:
                iwords+=1
                print(cWord)
            output+=cWord+char
            cWord=""
            isUpper=False
        elif (code >=48 and code<58):
            nums+=1
        else:
            punc+=1

    outfile = open(ofile,"w")
    outfile.write("""[k96010wp]
Formatting ###################
Number of upper case words changed: {}
Number of punctuations removed: {}
Number of numbers removed: {}
Spellchecking ###################
Number of words: {}
Number of correct words: {}
Number of incorrect words: {}""".format(ucount,punc,nums,words,cwords,iwords))

    outfile.close()
