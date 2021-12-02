import os
import sys

def hex(string):
    msg = ''

    for i in range(len(string)):
        if(i%2 == 0):
            n = int(string[i] + string[i+1], 16)
            msg += chr(n)

    return msg.lower()

def caesar(string):
    msg = ''

    for i in range(len(string)):
        x = ord(string[i])
        
        if((x >= 97 and x <= 122)
           or (x >= 65 and x <= 90)):
            msg += chr((x - 74)%26 + 97)
        else:
            msg += string[i]
    
    return msg.lower()

def morse(string):
    msg = ''
    temp = ''
    morse_dict = { '.-':'a', '-...':'b', '-.-.':'c', '-..':'d', '.':'e',
             '..-.':'f', '--.':'g', '....':'h', '..':'i', '.---':'j',
             '-.-':'k', '.-..':'l', '--':'m', '-.':'n', '---':'o',
             '.--.':'p', '--.-':'q', '.-.':'r', '...':'s', '-':'t',
             '..-':'u', '...-':'v', '.--':'w', '-..-':'x', '-.--':'y',
             '--..':'z', '.----':'1', '..---':'2', '...--':'3', '....-':'4',
             '.....':'5', '-....':'6', '--...':'7', '---..':'8', '----.':'9',
             '-----':'0', '.-.-.-':'.', '..--..':'?', '-.-.--':'!', '--..--':',',
             '---...':':', '-.-.-.':';', '-....-':'-', '..--.-':'_', '-.--.':'(',
             '-.--.-':')', '.----.':"'", '.-..-.':'"', '':'', '/':' ', ' ':''
          }

    for i in range(len(string)):
        if(string[i] == ' '):
            msg += morse_dict[temp]
            temp = ''
            continue
        else:
            temp += string[i]
            
    msg += morse_dict[temp]       
    return msg

def encryption(string):
    if(string[:3].lower() == 'hex'):
        return 0
    elif(string[:6].lower() == 'caesar'):
        return 1
    else:
        return 2

def ciphertext(string):
    for i in range(len(string)):
        if(string[i] == ':'):
            return string[i + 1:len(string) + 1]

def args():
    files = os.listdir(sys.argv[1])
    for i in files:
        comp = ''

        for k in range(len(i)):
            if(i[k] == '.' or k == len(i) - 1):
                comp = sys.argv[2] + '/' + i[:k] + '_w92704dw.txt'
                break

        i = sys.argv[1] + '/' + i
        with open(i, 'r') as input:
            text = (input.read()).replace('\n', '')
        
        cipher = ciphertext(text)
        algorithm = encryption(text)

        with open(comp, 'w') as output:
            if(algorithm == 0):
                output.write(hex(cipher.replace(' ','')))
            elif(algorithm == 1):
                output.write(caesar(cipher))
            else:
                output.write(morse(cipher))

args()
