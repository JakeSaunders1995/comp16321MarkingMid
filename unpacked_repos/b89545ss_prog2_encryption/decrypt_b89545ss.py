import sys
import os
import glob

encryptfile = []
for name in sys.argv[1:]:
    for file in glob.glob(os.path.join(name, "*.txt")):
        with open(file, "r") as f:
            encryptfile.append(f.read())

encryptfilePosition = 0
while (encryptfilePosition < len(encryptfile)):
    encrypt = encryptfile[encryptfilePosition]


for x in file:
    if x == 0:
        print(convertHex_to_Dec())
    elif x == 0:
        print(cipher_to_word())
    else:
        print(morse_to_message())


def convertHex_to_Dec(hexSubString):
    return chr(int(hexSubString, 16))

hexaString = "536f6c76696e67206865782069732076657279206561737920696e20707974686f6e"
decString = ""

   for i in range(0, len(hexaString), 2):
        subStr = hexaString[i] + hexaString[i + 1]
        decString += convertHex_to_Dec(subStr)

    print(decString)



morsecode_dictionary = { ' ':'/', 'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.', 'f':'..-.', 'g':'--.', 'h':'....',
                    'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..', 'm':'--', 'n':'-.','o':'---', 'p':'.--.', 'q':'--.-',
                    'r':'.-.', 's':'...', 't':'-','u':'..-', 'v':'...-', 'w':'.--','x':'-..-', 'y':'-.--', 'z':'--..',
                    }



def morse_to_message():
    message = input('Enter your morse code: ')
    code = [k for i in message.split() for k,v in morsecode_dictionary.items() if i==v]
    newmessage = ''.join(code)
    print(newmessage)

print(morse_to_message())

def cipher_to_word():
    message = "exw fdhvdu lv d olwwoh pruh gliilfxow"
    decrypt = ""
    for letter in message:
        if letter == " ":   #forspace
            decrypt += " "
    else:
        decrypt += chr(ord(letter) - 3) #convert_the_letters_using_ascii_first_using_ord_than_minus_it_by_3_because_cipher_is+3
                                        #then_use_chr_to_convert_the_ascii_letters_to_normal
    print(decrypt)
