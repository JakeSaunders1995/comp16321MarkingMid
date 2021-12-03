import sys

encrypted = sys.argv[1]
decrypted = sys.argv[2]



decrypted_data = ''


def MorseConvert():

    MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
    with open(encrypted, 'r') as f:
        morseUnedited = f.read()
        morseEncrypted = morseUnedited[11:]
        morseList = morseEncrypted.split(" ")



def CaeserConvert():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    with open(encrypted, 'r') as f:
        caeserUnedited  = f.read()
        caeserUnedited = caeserUnedited[18:]
        caeserWordList = caeserUnedited.split(" ")
        plaintext = ""
    
    for word in caeserWordList:
        for letter in word:
            for alphaPos in range(0,25):
                if letter == alphabet[alphaPos]:
                    plaintext += alphabet[alphaPos - 3]
        plaintext += " "
    
    with open(decrypted, 'w') as f:
        f.write(plaintext)

def HexConvert():
    with open(encrypted, 'r') as f:
        hex_code = f.read()
    hex_code = hex_code[4:]
    hex_list = hex_code.split(" ")
    plaintext = ""
    for hex_letter in hex_list:
        plaintext += bytes.fromhex(hex_letter).decode("ASCII")

    with open(decrypted, 'w') as f :
        f.write(plaintext)
        
        

        

def main():
    with open(encrypted, 'r') as e:
        data = e.read()
            #if not data:
            #    break
        if data.startswith('Hex:'):
           HexConvert()
        elif data.startswith('Caesar Cipher(+3):'):
           CaesesrConvert()
        elif data.startswith('Morse Code:'):
           MorseConvert()

main()

'''

if __name__ == '__main__':
    main()

'''
