dict = {
    ".-": "a", "-...": "b", "-.-.": "c", "-..": "d", ".": "e", "..-.": "f", "--.": "g",
    "....": "h", "..": "i", ".---": "j", "-.-": "k", ".-..": "l", "--": "m", "-.": "n",
    "---": "o", ".--．": "p", "--.-": "q", ".-.": "r", "...": "s", "-": "t",
    "..-": "u", "...-": "v", ".--": "w", "-..-": "x", "-.--": "y", "--..": "z",

    "-----": "0", ".----": "1", "..---": "2", "...--": "3", "....-": "4",
    ".....": "5", "-....": "6", "--...": "7", "---..": "8", "----.": "9",

    ".-.-.-": ".", "---...": ":", "--..--": ",", "-.-.-.": ";", "..--..": "?",
    "-...-": "=", ".----.": "'", "-..-.": "/", "-.-.--": "!", "-....-": "-",
    "..--.-": "_", ".-..-.": '"', "-.--.": "(", "-.--.-": ")", "...-..-": "$",
    ".-...": "&", ".--.-.": "@", ".-.-.": "+",
}

key = dict.keys()
values = dict.values()

def make_out(name, out):
    path1 = os.path.abspath(output_folder)
    path2 = path1 + '/' + name.replace('.txt','') + '_r86515xl' + '.txt'
    file = open(path2,'w')
    file.write(out)

def hex(file):
    out1 = ''
    for i in file.split(':')[1].split(' '):
        b = chr(int(i,16))
        out1 += b
    return out1.lower()

def Caesar(file):
    list = 'xyzabcdefghijklmnopqrstuvwxyzabc'
    position = 3
    out2 = ''
    for i in file.split(':')[1]:
        if i == ' ':
            out2 += ' '
        elif i not in list:
            continue
        else:
            while i != list[position]:
                position += 1
            else:
                out2 += list[position - 3]
                position = 3
    return out2

def Morse(file):
    out3 = ''
    for i in file.split(':')[1].split(' '):
        if i == '/':
           out3 += ' '
        elif i not in key:
            continue
        else:
            out3 += dict[i]
    return out3


import sys,os,re
script, input_folder, output_folder = sys.argv
dirs = os.listdir(input_folder)
for file_name in dirs:
    path = os.path.abspath(input_folder)
    file = open(path + '/' + file_name,'r')
    file = file.read()
    if re.search('Hex:', file, re.I) != None:
         out1 = hex(file)
         make_out(file_name, out1)
    elif re.search('Caesar', file, re.I) != None:
         out2 = Caesar(file)
         make_out(file_name, out2)
    else:
         out3 = Morse(file)
         make_out(file_name, out3)
