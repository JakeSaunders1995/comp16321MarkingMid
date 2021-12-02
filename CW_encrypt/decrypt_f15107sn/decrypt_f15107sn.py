import argparse

def read_file(in_file):
    in_f= open(in_file,'r')
    txt= in_f.readline() # read the first line
    in_f.close()
    return txt

def find_encryption(enc_txt,encryption_list):
    encryption= enc_txt.split(':')[0] #hex
    encryption_txt= enc_txt.split(':')[1] #ency text

    for enc in encryption_list:
        if enc == encryption:
            break
    return enc, encryption_txt

def morse_decryption(message):
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
                    '(':'-.--.', ')':'-.--.-', ' ': '/'}

    message += ' '
    decipher = ''
    citext = ''
    for letter in message:
        # checks for space
        if (letter != ' '):
            # counter to keep track of space
            i = 0
            # storing morse code of a single character
            citext += letter
        # in case of space
        else:
            # if i = 1 that indicates a new character
            i += 1
            # if i = 2 that indicates a new word
            if i == 2 :
                # adding space to separate words
                decipher += ' '
            else:
                # accessing the keys using their values (reverse of encryption)
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
                citext = ''

    return decipher.lower()

def caesar_decryption(decryption_txt):
    decipher= ''
    for letter in decryption_txt:
        if ord(letter)-3 == 29: #space
            decipher+= ' '
        else:
            decipher+= chr(ord(letter)-3)
    return decipher.lower()

def hex_decryption(decryption_txt):
    decipher= ''
    for letter in decryption_txt.split(' '):
        decipher+= chr(int(letter,16)) #learn
    return decipher.lower()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Encryption Decryption')
    parser.add_argument('in_file', type=str, help='Input file')
    parser.add_argument('out_file', type=str, help='Output file')
    args = parser.parse_args()

    # 2. reading the input .txt file
    enc_txt= read_file(args.in_file)
    print('The encrypted text is:> ',enc_txt)

    encryption_list= ['Morse Code','Caesar Cipher(+3)','Hex']

    # 3. finding the encryption used in the text
    enc,enc_txt= find_encryption(enc_txt,encryption_list)
    print('The encryption used in the text is :> ',enc)

    # 4. Decrypting the text
    if enc == 'Morse Code':
        decrypted_text= morse_decryption(enc_txt)
    elif enc == 'Caesar Cipher(+3)':
        decrypted_text= caesar_decryption(enc_txt)
    else:
        decrypted_text= hex_decryption(enc_txt)

    ## Writing the decrypted text to the output file

    out_file= open(args.out_file,'w')
    out_file.write(decrypted_text)
    out_file.close()
