import argparse,os

parser = argparse.ArgumentParser()
parser.add_argument('input_path', metavar='path')
parser.add_argument('output_path',metavar='path')
args = parser.parse_args()

dirs = os.listdir(args.input_path)
os.mkdir(args.output_path)
for file in dirs:
    a = os.getcwd()
    name = file[:-4]
    f10 = open(str(args.input_path)+'/'+str(file),'r')
    f = f10.read()
    f10.close()
    if 'Hex' in f:
        f0 = f.replace('Hex:','')
        f1 = f0.split(' ')
        result = ''
        for each in f1:
            if int(str(each),16)>64 and int(str(each),16)<91 :
                result += chr(int(str(each),16)+32)
            else:
                 result += chr(int(str(each),16))   
    elif 'Caesar' in f:
        f0 = f.strip('Caesar Cipher(+3)')
        f1 = f0.strip(':')
        result = ''
        for each in f1:
            if ord(each)>99 and ord(each)<123:
                result += chr(ord(each)-3)
            elif ord(each)>96 and ord(each)<100:
                result += chr(ord(each)+23)
            else:
                result += ' '
    else:
        CODE = {'.-':'a',  '-...':'b',   '-.-.':'c',
            '-..':'d',    '.':'e',      '..-.':'f',
            '--.':'g',    '....':'h',   '..':'i',
            '.---':'j',   '-.-':'k',    '.-..':'l',
            '--':'m',     '-.':'n',     '---':'o',
            '.--.':'p',   '--.-':'q',   '.-.':'r',
            '...':'s',    '-':'t',      '..-':'u',
            '...-':'v',   '.--':'w' ,   '-..-': 'x',
            '-.--':'y',   '--..':'z',

            '-----':'0',  '.----':'1' ,  '..---':'2' ,
            '...--':'3',  '....-':'4' ,  '.....':'5', 
            '-....':'6' , '--...': '7' ,  '---..':'8',
            '----.':'9',
            
            '/':' '
            }
        f1 = f.strip('Morse Code:')
        target = f1.split(' ')
        result = ''
        for i in target:
            if i in CODE.keys():
                result += ''+CODE[i]
            else:
                result += ''
    os.chdir(args.output_path)
    f2 = open(str(name)+'_e86238yj','w')
    f2.write(result)
    f2.close()
    os.chdir(a)
    






