import re
import collections
import argparse
import os
from pathlib import Path

parser = argparse.ArgumentParser(description='')
parser = argparse.ArgumentParser(description='')
parser.add_argument('path3', metavar='p', type=str, nargs='+')
parser.add_argument('path', metavar='p', type=str, nargs='+')
parser.add_argument('path2', metavar='p', type=str, nargs='+')

#read
args = parser.parse_args()
path = Path(args.path[0])
l = []

for p in path.glob('*'):
    l.append(str(p))


for q in l:
    with open(q,'r') as f:
        input=(''.join(f.read())).strip('\n')
    il = input.split()


    #format number
    num = re.sub(r'[0-9]+','',input)
    nl = num.split()


    #format punctuation
    chr = "[-/:;()$&@“.,?!’[\\]{}#%^*+=_\|~<>€£¥•\\''\n]"
    pun = re.sub(chr,'',input)


    #format upper case + count upper changes
    text = ((re.sub(r'[0-9]+','',pun)).lower()).split()
    a=re.sub(r'[0-9]+','',pun).split()
    l = []
    for i in range(len(text)):
        while text[i] != a[i]:
            l.append(text[i])
            i+=1

    #count changes
    alp=0
    num=0
    spa=0
    oth=0
    for oo in range(len(input)):
        if input[oo].isspace():
            spa+=1
        elif input[oo].isdigit():
            num+=1
        elif input[oo].isalpha():
            alp+=1
        else:
            oth+=1
    
    # determine if they are correct
    def tokens(text):
        return re.findall('[a-z]+', text.lower())

    path3 = parser.parse_args().path3[0]
    p3 = Path(path3)
    with open(p3, 'r') as f:
        WORDS = tokens(f.read())
    WORD_COUNTS = collections.Counter(WORDS)


    def known(words):
        return {w for w in words if w in WORD_COUNTS}


    def edits0(word):
        return {word}


    def edits1(word):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'

        def splits(word):
            return [(word[:i], word[i:]) for i in range(len(word) + 1)]

        pairs = splits(word)
        deletes = [a + b[1:] for (a, b) in pairs if b]
        transposes = [a + b[1] + b[0] + b[2:] for (a, b) in pairs if len(b) > 1]
        replaces = [a + c + b[1:] for (a, b) in pairs for c in alphabet if b]
        inserts = [a + c + b for (a, b) in pairs for c in alphabet]
        return set(deletes + transposes + replaces + inserts)


    def edits2(word):
        return {e2 for e1 in edits1(word) for e2 in edits1(e1)}


    def correct(word):
        candidates = (known(edits0(word)) or
                      known(edits1(word)) or
                      known(edits2(word)) or
                      [word])
        return max(candidates, key=WORD_COUNTS.get)


    def correct_match(match):
        word = match.group()

        def case_of(text):
            return (str.upper if text.isupper() else
                    str.lower if text.islower() else
                    str.title if text.istitle() else
                    str)

        return case_of(word)(correct(word.lower()))


    def correct_text_generic(text):
        return re.sub('[a-zA-Z]+', correct_match, text)


    original_word_list = text

    ll = []
    for original_word in original_word_list:
        correct_word = ll.append(correct_text_generic(original_word))
    vv =[]
    for qq in range(len(ll)):
        if ll[qq] != text[qq]:
            vv.append(ll[qq])


    #write
    path2 = parser.parse_args().path2[0]
    p = Path(path2)
    nn=str((os.path.basename(q))[:-4])+'_m36036zz.txt'
    file2 = p / nn
    with file2.open('w') as ff:
        ff.write('Formatting ###################\n')
        ff.write('Number of upper case removed:'+str(len(l)))
        ff.write('\nNumber of punctuation removed:'+str(oth))
        ff.write('\nNumber of numbers removed:'+str(num))
        ff.write('\nSpellchecking ###################')
        ff.write('\nNumber of words:'+str(len(text)))
        ff.write('\nNumber of correct words:'+str(len(text)-len(vv)))
        ff.write('\nNumber of incorrect words:'+str(len(vv)))
