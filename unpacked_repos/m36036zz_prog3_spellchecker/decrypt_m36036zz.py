import argparse
import os
import binascii
from pathlib import Path

parser = argparse.ArgumentParser(description='')
parser = argparse.ArgumentParser(description='')
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
        content=(''.join(f.read())).strip('\n')
    hl = content.split()

    #caesar
    if hl[0] == 'Caesar':
        hl.pop(0)
        hl[0] = hl[0][11:]
        text = []
        for z in hl:
            for x in z:
                asc = ord(x)-3
                if asc > 96:
                    word = chr(asc)
                    text.append(word)
                elif asc < 97:
                    asc2 = 123-(97-asc)
                    word = chr(asc2)
                    text.append(word)
                else:
                    print('u input out of fucking range')
            text.append(' ')
        path2 = parser.parse_args().path2[0]
        p = Path(path2)
        nn=str((os.path.basename(q))[:-4])+'_m36036zz.txt'
        file2 = p / nn
        with file2.open('w') as ff:
            ff.write(''.join(text))

    #morse
    elif hl[0] == 'Morse':
        dict = {'.-': 'A',
        '-...': 'B',
        '-.-.': 'C',
        '-..':'D',
        '.':'E',
        '..-.':'F',
        '--.': 'G',
        '....': 'H',
        '..': 'I',
        '.---':'J',
        '-.-': 'K',
        '.-..': 'L',
        '--': 'M',
        '-.': 'N',
        '---': 'O',
        '.--.': 'P',
        '--.-': 'Q',
        '.-.': 'R',
        '...': 'S',
        '-': 'T',
        '..-': 'U',
        '...-': 'V',
        '.--': 'W',
        '-..-': 'X',
        '-.--': 'Y',
        '--..': 'Z',
        '.----': '1',
        '..---': '2',
        '...--': '3',
        '....-': '4',
        '.....': '5',
        '-....': '6',
        '--...': '7',
        '---..': '8',
        '----.': '9',
        '-----': '0',
        '..--..': '?',
        '-..-.': '/',
        '-.--.-': '()',
        '-....-': '-',
        '.-.-.-': '.',
        '/':' '
        }
        hl.pop(0)
        hl[0] = hl[0][5:]
        pp = []
        for m in hl:
            pp.append((dict[m]).lower())
        path2 = parser.parse_args().path2[0]
        p = Path(path2)
        nn=str((os.path.basename(q))[:-4])+'_m36036zz.txt'
        file2 = p / nn
        with file2.open('w') as ff:
            ff.write(''.join(pp))
  
    #hex
    elif hl[0][0:4] == 'Hex:':
        hl[0] = hl[0][4:]
        bl = []
        asc3 = []
        for i in hl:
            bl.append((bin(ord(binascii.unhexlify(i)))).strip('\n'))
            a = str(binascii.unhexlify(i)).strip('b')
            b = a.strip("''")
            asc3.append((b).strip('\n'))
        path2 = parser.parse_args().path2[0]
        p = Path(path2)
        nn=str((os.path.basename(q))[:-4])+'_m36036zz.txt'
        file2 = p / nn
        with file2.open('w') as ff:
            ff.write((''.join(asc3)).lower())
        
