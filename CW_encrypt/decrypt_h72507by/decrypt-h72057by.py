import argparse

# morse_code
ms_dict = {
    '/': ' ',   
    '-': 't',
    '--': 'm',
    '---': 'o',
    '-----': '0',
    '----.': '9',
    '---..': '8',
    '---...': ':',
    '--.': 'g',
    '--.-': 'q',
    '--..': 'z',
    '--..--': ',',
    '--...': '7',
    '-.': 'n',
    '-.-': 'k',
    '-.--': 'y',
    '-.--.': '(',
    '-.--.-': ')',
    '-.-.': 'c',
    '-.-.--': '!',
    '-.-.-.': ';',
    '-..': 'd',
    '-..-': 'x',
    '-..-.': '/',
    '-...': 'b',
    '-....': '6',
    '-....-': '-',
    '.': 'e',
    '.-': 'a',
    '.--': 'w',
    '.---': 'j',
    '.----': '1',
    '.----.': "'",
    '.--．': 'p',
    '.-.': 'r',
    '.-.-.-': '.',
    '.-..': 'l',
    '.-..-.': '"',
    '..': 'i',
    '..-': 'u',
    '..---': '2',
    '..--.-': '_',
    '..--..': '?',
    '..-.': 'f',
    '...': 's',
    '...-': 'v',
    '...--': '3',
    '....': 'h',
    '....-': '4',
    '.....': '5'
}

def de_hex(txt: str):
    res = ''.join(chr(int(i, 16)).lower() for i in txt.split(' '))
    return res

def de_caesar_cipher(txt: str):
    res = ''
    for s in txt:
        if s.islower():
            n = ord(s) - 3
            if n < ord('a'):
                n += 26
            res += chr(n)
        elif s.isupper():
            n = ord(s) - 3
            if n < ord('A'):
                n += 26
            res += chr(n)
        else:
            res += s
    return res

def de_morse_code(txt: str):
    res = ''.join(ms_dict.get(c) for c in txt.split(' '))
    return res

def main(input, output):
    res = ''
    with open(input, 'r') as f:
        txt = f.readline()
        if txt[0] == 'H':
            res = de_hex(txt[4:])
        elif txt[0] == 'C':
            res = de_caesar_cipher(txt[18:])
        elif txt[0] == 'M':
            res = de_morse_code(txt[11:])
    with open(output, 'w') as f:
        f.write(res)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', type=str)
    parser.add_argument('output', type=str)
    args = parser.parse_args()
    main(args.input, args.output)
