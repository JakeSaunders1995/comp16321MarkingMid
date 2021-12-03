import argparse,os

parser = argparse.ArgumentParser()
parser.add_argument('englishwords', type=argparse.FileType('r'))
parser.add_argument('input_path', metavar='path')
parser.add_argument('output_path',metavar='path')
args = parser.parse_args()

en = args.englishwords.read()
enlist = en.split('\n')
args.englishwords.close()

dirs = os.listdir(args.input_path)
os.mkdir(args.output_path)
for file in dirs:
    a = os.getcwd()
    name = file[:-4]
    f10 = open(str(args.input_path)+'/'+str(file),'r')
    f = f10.read()
    f10.close()
    upper = 0
    punc = 0
    num = 0
    words = 0
    correct = 0
    incorrect = 0
    result = ''
    i = 0
    while i<len(f):
        if ord(f[i])== 33 or ord(f[i])== 34 or ord(f[i])== 58 or ord(f[i])== 59 or ord(f[i])== 63 or ord(f[i])== 123 or ord(f[i])== 125 or ord(f[i])== 91 or ord(f[i])== 93 or ord(f[i])== 96 or(ord(f[i])>38 and ord(f[i])<42)or(ord(f[i])>43 and ord(f[i])<47):
                punc += 1
                if i<len(f)-1 and ord(f[i])==46 and ord(f[i+1])== 46:
                    punc -= 2
        if ord(f[i])>47 and ord(f[i])<58:
            num += 1
        if ord(f[i])>64 and ord(f[i])<91:
            upper += 1
            result += chr(ord(f[i])+32)
        if ord(f[i])==32:
            result += ' '
        if i<len(f)-1 and ord(f[i])==32 and ord(f[i+1])==32:
            result -= ' '
        if ord(f[i])>96 and ord(f[i])<123:
            result += f[i]
        i += 1
    f1 = result.split(' ')
    for each in f1:
        if each != '':
            words += 1
            if each in enlist:
                correct += 1
            else:
                incorrect += 1
    os.chdir(args.output_path)
    f2 = open(str(name)+'_e86238yj','w')
    f2.write('e86238yj \nFormatting ################### \nNumber of upper case words changed: '+str(upper)+'\nNumber of punctuations removed: '+str(punc)+'\nNumber of numbers removed: '+str(num)+'\nSpellchecking ################### \nNumber of words: '+str(words)+'\nNumber of correct words: '+str(correct)+'\nNumber of incorrect words: '+str(incorrect))
    f2.close()
    os.chdir(a)
