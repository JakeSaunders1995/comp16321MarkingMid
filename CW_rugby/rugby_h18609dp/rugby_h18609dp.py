import argparse

T1 = 0
T2 = 0

parser = argparse.ArgumentParser(description='example of file copy')
parser.add_argument('src',  help='Source File')
parser.add_argument('dst',  help='Target File')
args = parser.parse_args()

src = args.src
dst = args.dst

with open(src, "r", encoding="utf-8") as f:
    L = f.read().split('T')
    if '1t' in L:
        T1 = T1 + (5*L.count('1t'))
    if '1c' in L:
        T1 = T1 + (2*L.count('1c'))
    if '1p' in L:
        T1 = T1 + (3*L.count('1p'))
    if '1d' in L:
        T1 = T1 + (3*L.count('1d'))
    if '2t' in L:
        T2 = T2 + (5*L.count('2t'))
    if '2c' in L:
        T2 = T2 + (2*L.count('2c'))
    if '2p' in L:
        T2 = T2 + (3*L.count('2p'))
    if '2d' in L:
        T2 = T2 + (3*L.count('2d'))

    scr = '%d : %d' %(T1, T2)

    if T1 > T2:
        H = 'T1 Win'
    elif T2 > T1:
        H = 'T2 Win'
    else:
        H = 'Draw'

    with open(dst, "w", encoding="utf-8") as f2:
        f2.write(scr)
        f2.write('\n')
        f2.write(H)
