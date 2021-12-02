import sys

input_file_path = sys.argv[1]
output_file_path = sys.argv[2]

def decode_hex(s:str) -> str:
    wordlist = s.split(" ")
    res = ""
    for word in wordlist:
        res += chr(int(word, 16))
    return res.lower()

def decode_caesar(s:str) -> str:
    res = ""
    for c in s:
        if c < 'a' or c > 'z':
            res += c
        else:
            if c == 'a':
                res += 'x'
            elif c == 'b':
                res += 'y'
            elif c == 'c':
                res += 'z'
            else:
                res += chr(ord(c) - 3)
    return res

def decode_morse(s:str) -> str:
    res = ""
    slist = s.split(' ')
    dict = {'.-': 'A',
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
            '.-.-.-': '.',
            '/' : ' '
            }
    for val in slist:
        res += dict[val]
    return res.lower()

def helper(type:str, text:str) -> str:
    if type[0] == 'H':
        return decode_hex(text)
    elif type[0] == 'C':
        return decode_caesar(text)
    elif type[0] == 'M':
        return decode_morse(text)

with open(input_file_path, 'r') as f:
    context = f.read()

type = context.split(":")[0]
text = context.split(":")[1]

output = helper(type, text)

with open(output_file_path, 'w') as f:
    f.write(output)