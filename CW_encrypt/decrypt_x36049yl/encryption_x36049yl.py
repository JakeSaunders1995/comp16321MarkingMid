import argparse
import sys
import os

morse = {'.-': 'A',
                      '-...': 'B',
                      '-.-.': 'C',
                      '-..': 'D',
                      '.': 'E',
                      '..-.': 'F',
                      '--.': 'G',
                      '....': 'H',
                      '..': 'I',
                      '.---': 'J',
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
                      '.-.-.-': '.'}

def mainargparse():
    par = argparse.ArgumentParser()
    par.add_argument('inp')
    par.add_argument('out')
    a = par.parse_args()
    return a.inp, a.out


def decrypt(inputpath, outputpath):
    with open(inputpath) as unf:
        l = unf.readline().strip()
        method = l.split(':')[0]
        content = l.split(':')[1]


    if method == 'Hex':
        sent = bytes.fromhex(content.replace(' ', '')).decode()
    elif method == 'Caesar Cipher(+3)':

        content = content.split()
        sent = []

        for word in content:
            cipords = [ord(x) for x in word]
            plainords = [o - 3 for o in cipords]
            plainchars = [chr(i) for i in plainords]
            plaintext = ''.join(plainchars)
            sent.append(plaintext)

        sent = ' '.join(sent)
    else:
        sent = morsecode(content).lower()


    with open(outputpath, 'w') as unf:
        unf.write('{}'.format(sent))





def morsecode(morseCode):
    mess = ''
    results = []
    for it in morseCode.split(' '):
        results.append(morse.get(it))
    for q in results:
        if q:
            mess += q
        else:
            mess += ' '
    return mess


if __name__ == '__main__':

    inp, out = mainargparse()
    list = os.listdir(inp)
    for file in list:
        input = os.path.join(inp, file)
        outpath = os.path.abspath(out)
        if not os.path.exists(outpath):
            os.makedirs(outpath)
        output = os.path.join(outpath,
                                   os.path.splitext(file)[0] + '_x36049yl.txt')
        decrypt(input, output)
