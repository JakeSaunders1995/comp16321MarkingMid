import argparse

parser = argparse.ArgumentParser(description='example of file copy')
parser.add_argument('src',  help='Source File')
parser.add_argument('dst',  help='Target File')
args = parser.parse_args()

src = args.src
dst = args.dst

with open(src, "r", encoding="utf-8") as f:
    b = f.read().split(':')
    c = b[1]
    L = c.split(' ')

    mos_code = {
        '.-': 'a',
        '-...': 'b',
        '-.-.': 'c',
        '-..': 'd',
        '.': 'e',
        '..-.': 'f',
        '--.': 'g',
        '....': 'h',
        '..': 'i',
        '.---': 'j',
        '-.-': 'k',
        '.-..': 'l',
        '--': 'm',
        '-.': 'n',
        '---': 'o',
        '.--.': 'p',
        '--.-': 'q',
        '.-.': 'r',
        '...': 's',
        '-': 't',
        '..-': 'u',
        '...-': 'v',
        '.--': 'w',
        '-..-': 'x',
        '-.--': 'y',
        '--..': 'z',
        '.-.-.-': '.',
        '--..--': ',',
        '..--..': '?',
        '-.-.--': '!',
        '-.-.-.': ';',
        '---...': ':',
        '-....-': '-',
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
        '.----.': "'",
        '-..-.': '/',
        '-.--.': '(',
        '-.--.-': ')',
        '.-...': '&',
        '-...-': '=',
        '.-.-.': '+',
        '..--.-': '_',
        '.-..-.': '"',
        '.--.-.': '@'
    }

    if 'Morse' in b[0]:
        Q = ''
        for i in L:
            try:
                Q += mos_code[i]
            except:
                Q += " "

    if 'Cipher' in b[0]:
        def decrypt_cis(msg,key):
            Q = ''
            dic = 'abcdefghijklmnopqrstuvwxyz'

            for m in msg:
                index = dic.find(m)
                if(index ==  -1):
                    Q = Q + m
                else:
                    index = index - key
                    index = index % len(dic)
                    Q = Q + dic[index]

            return Q

        def main():
            msg = b[1]
            key = 3

            Q = decrypt_cis(msg, key)
        main()
        msg = b[1]
        key = 3
        Q = decrypt_cis(msg, key)

    if 'Hex' in b[0]:
        Q1 = bytearray.fromhex(c)
        Q1.decode()
        Q2 = str(Q1, 'utf-8')
        Q = Q2.lower()

    with open(dst, "w", encoding="utf-8") as f2:
        f2.write(Q)
