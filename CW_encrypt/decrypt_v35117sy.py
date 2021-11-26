import argparse
import os
parser = argparse.ArgumentParser(description='input and output')
parser.add_argument('input_file_path', help='input')
parser.add_argument('output_file_path', help='output')
args = parser.parse_args()
input_file_path = args.input_file_path
output_file_path = args.output_file_path

def caesar(text):
    res = ''
    for ch in text:
        if ch == ' ':
            res += ch
        else:
            num = ord(ch)-3
            res += chr(num)
    return res

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

def main(input_file, output_file):
    res = decrypt(input_file)
    # print(res)
    with open(output_file, 'w') as f:
        f.write(f'{res}\n')

in_files = os.listdir(input_file_path)
if  not os.path.exists(output_file_path):
    os.mkdir(output_file_path)
for item in in_files:
    out_name = os.path.join(output_file_path,item.split('.')[0]+'_v35117sy.txt')
    item = os.path.join(input_file_path, item)
    main(item, out_name)
