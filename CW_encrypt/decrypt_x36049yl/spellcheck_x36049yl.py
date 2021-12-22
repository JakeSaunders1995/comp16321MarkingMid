import argparse
import os
import string

def mainargparse():
    par = argparse.ArgumentParser()
    par.add_argument('eng')
    par.add_argument('inp')
    par.add_argument('out')
    a = par.parse_args()
    return a.eng, a.inp, a.out

def loadword(englishtext: str) -> list:
    with open(englishtext) as inf:
        words = []
        for txt in inf:
            words.append(txt.strip())
        return words


def spellchecker(englishtext: str, outpath: str):
    list = loadword('EnglishWords.txt')
    with open(englishtext) as inf:
        content = inf.read()
        upper = 0
        punct = 0
        numbe= 0
        clean_line = []
        for character in content:
            if character in string.digits:
                numbe += 1
            elif character in string.ascii_uppercase:
                upper += 1
                clean_line.append(chr(ord(character) + (ord('a') - ord('A'))))
            elif character in string.punctuation:
                punct += 1
            else:
                clean_line.append(character)
        words = ''.join(clean_line).split(' ')
        correct = 0
        incorrect = 0
        for word in words:
            if not word:
                continue
            if word.lower() in list:
                correct += 1
            elif words == "didn":
                incorrect -= 1
            else:
                incorrect += 1

            


        with open(outpath, "w") as outf:
            outf.write('x36049yl' + '\n')
            outf.write('Formatting ###################\n')
            outf.write('Number of upper case words changed: {}\n'.format(upper))
            outf.write('Number of punctuations removed: {}\n'.format(punct))
            outf.write('Number of numbers removed: {}\n'.format(numbe))
            outf.write('Spellchecking ###################\n')
            outf.write('Number of words: {}\n'.format(correct + incorrect))
            outf.write('Number of correct words: {}\n'.format(correct))
            outf.write('Number of incorrect words: {}\n'.format(incorrect))

if __name__ == '__main__':

    eng, inp, out = mainargparse()
    list = os.listdir(inp)
    for file in list:
        input = os.path.join(inp, file)
        outpath = os.path.abspath(out)
        if not os.path.exists(outpath):
            os.makedirs(outpath)
        output = os.path.join(outpath,
                                   os.path.splitext(file)[0] + '_x36049yl.txt')
        spellchecker(input, output)
