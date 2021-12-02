import os
import re
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("dictionary")
parser.add_argument("input")
parser.add_argument('output')
args = parser.parse_args()
dict_file = args.dictionary
directory = args.input
s = open(dict_file, "r")
eng = s.read()
s.close()
punctuation = ['.','?','!',',',':',';','-','{','}','(',')','"',"'",'–','—','[',']',chr(8212), chr(8211), chr(8230)]
output_folder = args.output
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        f = open(f, "r")
        para = f.read()
        f.close()
        
        upper_case = punc = num = words = correct = incorrect = 0
        eng1 = eng.split()
        
        i = 0
        x = re.findall("[0-9]", para)
        y = re.findall("[A-Z]", para)
        para1 = para.split()
        for i in para1:
            if '...' in i:
                punc +=1
                index = para1.index(i)
                i = i.replace('...','',1)
                para1[index] = i
                para = ' '.join(para1)
         
        for s in para:
            if s in punctuation:
                para = para.replace(s,'',1)
                punc += 1
        for j in x:
            para = para.replace(j, '', 1)
            num += 1
        for q in y:
            para = para.replace(q, q.lower(), 1)
            upper_case += 1
        a = re.findall('[a-z]+', para)
        incorrect = len(a)
        for w in a:
            if w in eng1:
                correct += 1
                incorrect -= 1
        for b in a:
            words += 1
        filename1 = filename[0:(len(filename)-4)]
        output_path = f'{output_folder}/{filename1}_y42270sg.txt'
        ou = open(output_path, 'w')
        ou.write(f'y42270sg\nFormatting ###################\nNumber of upper case letters changed: {upper_case}\nNumber of punctuations removed: {punc}\nNumber of numbers removed: {num}\nSpellchecking ###################\nNumber of words: {words}\nNumber of correct words: {correct}\nNumber of incorrect words: {incorrect}\n')
        ou.close()
