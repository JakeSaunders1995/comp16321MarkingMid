import sys
import os
f=open(sys.argv[1])
word=f.read()
Englishwordlist=word.splitlines()
path=sys.argv[2]
outputpath=sys.argv[3]
path_list = os.listdir(path)
path_list.sort()
num = 0
for filename in path_list:
    num = num + 1
    f = open(os.path.join(path,filename))
    w=f.read()
    correct = 0
    incorrect = 0
    new = list(w)
    Q = ""
    i = 0
    punctuations = 0
    upper = 0
    number = 0
    word1 = 0
    while i < len(w):
        asciicode = ord(w[i])
        if 32 < asciicode < 48 or 57 < asciicode < 65 or 90 < asciicode < 97 or 122 < asciicode < 127:
            punctuations += 1
            new[i] = ""
            Q = ''.join(new)
            if ord(w[i - 1]) == 32:
                new[i - 1] = ''
                Q =''.join(new)
        if 64 < asciicode < 90:
            upper += 1
            newstr1 = asciicode + 32
            new[i] = chr(newstr1)
            Q =''.join(new)
        if 47 < asciicode < 57:
            number += 1
            new[i] = ""
            Q =''.join(new)
            if ord(w[i - 1]) == 32:
                new[i - 1] = ""
                Q = ''.join(new)
        i += 1
    if i == len(w):
        H = Q.split(" ")
        for K in range(len(H)):
            word1 = K
        for M in H:
            if M in Englishwordlist:
                correct += 1
            else:
                incorrect += 1      
    output_filename = 'test_file_j29403qy' + str(num) + '.txt'
    f1=open(os.path.join(outputpath,output_filename),'w')
    f1.write("j29403qy"+"\nFormatting ###################"+"\nNumber of upper case words changed:"+str(upper)+"\nNumber of Punctuations removed:"+str(punctuations)+"\nNumber of numbers removed:"+str(number)+"\nSpellchecking ###################"+"\nNumber of words:"+str(word1 + 1)+"\nNumber of correct words:"+str(correct)+"\nNumber of incorrect words:"+ str(incorrect))
    f1.close()

