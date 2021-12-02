import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('input')
parser.add_argument('output')
args = parser.parse_args()
input = args.input
output = args.output

def morse(text):
    res = ''
    m = {
        ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E", "..-.": "F", "--.": "G",
        "....": "H", "..": "I", ".---": "J", "-.-": "K", ".-..": "L", "--": "M", "-.": "N",
        "---": "O", ".--．": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
        "..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y", "--..": "Z",
    }
    ls = text.split(' ')
    for item in ls:
        if item in m:
            res += (m[item].lower())
        else:
            res += ' '
    return res[:-1]

def caesar(text):
    res = ''
    for ch in text:
        if ch == ' ':
            res += ch
        else:
            num = ord(ch)-3
            res += chr(num)
    return res

def hex(text):
    res = ''
    ls = text.split(' ')
    for item in ls:
        res += chr(int(item, 16))
    return res


def decrypt(file):
    with open(file) as f:
        content = f.read().strip()
    ls = content.split(':')
    method, text = ls[0], ls[1]
    if method == 'Hex':
        return hex(text)
    elif method == 'Morse Code':
        return morse(text)
    elif method == 'Caesar Cipher(+3)':
        return caesar(text)
    else:
        print(f'error decrypt method: {method}!')
        exit(1)

def main(input, output):
    res = decrypt(input)
    with open(output, 'w') as f:
        f.write(f'{res}\n')

file_in = os.listdir(input)
if not os.path.exists(output):
    os.mkdir(output)
for item in file_in:
    name=os.path.join(output, item.split('.')[0]+'_f60163yw.txt')
    item = os.path.join(input, item)
    main(item, name)
