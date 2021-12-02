import argparse
import re

parser = argparse.ArgumentParser(description='Midterm Coursework')
parser.add_argument('src',  help='Word File')
parser.add_argument('dst',  help='Source File')
parser.add_argument('lst',  help='Target File')
args = parser.parse_args()

src = args.src
dst = args.dst
lst = args.lst

with open(dst, "r", encoding="utf-8") as f1:
    CL = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    A = 0
    fa = f1.read()
    for C in fa:
        if C in CL:
            A = A + 1


    b1 = fa.count('@')
    b2 = fa.count(',')
    b3 = fa.count('.')
    b4 = fa.count('!')
    b5 = fa.count("'")
    b6 = fa.count('"')
    b7 = fa.count('#')
    b8 = fa.count('?')
    b9 = fa.count('[')
    b0 = fa.count(']')
    ba = fa.count(';')
    bb = fa.count(':')
    bc = fa.count('{')
    bd = fa.count('}')
    be = fa.count('(')
    bf = fa.count(')')
    bg = fa.count('=')
    bh = fa.count('-')
    bi = fa.count('+')
    bj = fa.count('*')
    bk = fa.count('/')
    bl = fa.count('%')

    B = b1 + b2 + b3 + b4 + b5 + b6 + b7 + b8 + b9 + b0 + ba + bb + bc + bd + be + bf + bg + bh + bi + bj + bk + bl

    S1 = re.sub("\!|\'|\?\@|\#|\[|\]|\,|\.|\;|\:|\{|\}|\(|\)|\=|\-|\+|\*|\/|\%","",fa)
    S = re.sub('\"','',S1)

    numbers = re.sub(r'[^0-9]', '', S)
    C = len(str(numbers))

    N = re.sub(r'[0-9]+', '', S)

    N1 = N.lower()
    W = N1.split()
    D = len(W)
    with open(src, "r", encoding="utf-8") as f:
        fz = f.read().split('\n')
        E = 0
        F = 0
        for I in range(len(W)):
            if W[I] in fz:
                E += 1
            else:
                F += 1

        P1 = 'h18609dp'
        P2 = 'Formatting ###################'
        P3 = 'Number of upper case words changed: %d' %A
        P4 = 'Number of punctuations removed: %d' %B
        P5 = 'Number of numbers removed: %d' %C
        P6 = 'Spellchecking ###################'
        P7 = 'Number of words: %d' %D
        P8 = 'Number of correct words: %d' %E
        P9 = 'Number of incorrect words: %d' %F


        with open(lst, "w", encoding="utf-8") as f2:
            f2.write(P1)
            f2.write('\n')
            f2.write(P2)
            f2.write('\n')
            f2.write(P3)
            f2.write('\n')
            f2.write(P4)
            f2.write('\n')
            f2.write(P5)
            f2.write('\n')
            f2.write(P6)
            f2.write('\n')
            f2.write(P7)
            f2.write('\n')
            f2.write(P8)
            f2.write('\n')
            f2.write(P9)
