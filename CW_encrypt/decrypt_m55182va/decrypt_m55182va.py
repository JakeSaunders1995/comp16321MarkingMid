import os
import argparse
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("in_file", help="enter input file")
    parser.add_argument("out_file", help="enter output file")
args = parser.parse_args()
input_file = args.in_file
for k in os.listdir(input_file):
    txt_position = k.find('.txt')
    input_file_name = k[0:txt_position]
    file = open(f'{args.in_file}/{k}','r')  
    theScore = []
    for line in file:
        line = line.rstrip()
        theScore.append(line)
    cipher = theScore[0]
    cipher_type = None
    semicolon_position = cipher.find(':')
    Hex_count_no_01 = '23456789abcdef'
    alphabets = 'abcdefghijklomnopqrstuvwxyz'
    hex_alphanumeric = 'abcdef'
    decipher = ''
    
    #determining cipher type
    if '0' in cipher[semicolon_position:] and '1' in cipher[semicolon_position:]:
        for x in Hex_count_no_01:
            if x in cipher[semicolon_position:]:
                cipher_type = 'Hexadecimal'
                break
            else:
                cipher_type = 'Binary'
    elif '.' and '-' in cipher[semicolon_position:]:
        cipher_type = 'Morse Code'
    else:
        cipher_type = 'Caesar Cipher(+3)'
    
    
    #deciphering if hex
    
    main_cipher = cipher[semicolon_position+1:]
    if cipher_type == 'Hexadecimal':
        for x in range(0, len(main_cipher), 3):
            q = main_cipher[x]
            if q in hex_alphanumeric:
                if q == 'a':
                    q = 10
                elif q == 'b':
                    q = 11
                elif q == 'c':
                    q = 12
                elif q == 'd':
                    q = 13
                elif q == 'e':
                    q = 14
                elif q == 'f':
                    q = 15
            y = x+1
            w = main_cipher[y]
            if w in hex_alphanumeric:
                if w == 'a':
                    w = 10
                elif w == 'b':
                    w = 11
                elif w == 'c':
                    w = 12
                elif w == 'd':
                    w = 13
                elif w == 'e':
                    w = 14
                elif w == 'f':
                    w = 15
            decimal = 16*int(q) + int(w)
            decipher = decipher + str(chr(decimal)).lower()
    
    #decipher if morse code
    elif cipher_type == 'Morse Code':
        word_in_morse_code = []
        slash_list = []
        morse_code_list = main_cipher.split(' ')
        for r in morse_code_list:
            if r == '.-':
                r = 'a'
            if r == '-...':
                r = 'b'
            if r == '-.-.':
                r = 'c'
            if r == '-..':
                r = 'd'
            if r == '.':
                r = 'e'
            if r == '..-.':
                r = 'f'
            if r == '--.':
                r = 'g'
            if r == '....':
                r = 'h'
            if r == '..':
                r = 'i'
            if r == '.---':
                r = 'j'
            if r == '-.-':
                r = 'k'
            if r == '.-..':
                r = 'l'
            if r == '--':
                r = 'm'
            if r == '-.':
                r = 'n'
            if r == '---':
                r = 'o'
            if r == '.--.':
                r = 'p'
            if r == '--.-':
                r = 'q'
            if r == '.-.':
                r = 'r'
            if r == '...':
                r = 's'
            if r == '-':
                r = 't'
            if r == '..-':
                r = 'u'
            if r == '...-':
                r = 'v'
            if r == '.--':
                r = 'w'
            if r == '-..-':
                r = 'x'
            if r == '-.--':
                r = 'y'
            if r == '--..':
                r = 'z'
            if r == '/':
                r = ' '
            if r == '.-.-.-':
                r = '.'
            if r == '--..--':
                r = ','
            if r == '..--..':
                r = '?'
            if r == '.----.':
                r = "'"
            if r == '-..-.':
                r = '/'
            if r == '---...':
                r = ':'
            if r == '-.-.-.':
                r = ';'
            if r == '-....-':
                r = '-'
            if r == '-.--.':
                r = '('
            if r == '-.--.-':
                r = ')'
            if r == '.-..-.':
                r = '"'
            if r == '-.-.--':
                r = '!'
            decipher = decipher + r
    #decipher if code is Ceaser (+3)
    elif cipher_type == 'Caesar Cipher(+3)':
        ct = main_cipher.lower()
        pt = ""
        alphabets = 'xyzabcdefghijklmnopqrstuvwxyz'
        ctp = 0
        while ctp<len(ct):
            ctc = ct[ctp]
            ap = 3
            if ctc == ' ':
                pt = pt + ' '
                ctp += 1            
            else:
                while ctc != alphabets[ap]:
                    ap = ap+1
                ap = ap - 3
                pt = pt + alphabets[ap]
                ctp += 1
            
        decipher = pt
    print(decipher)
    line = [f'{decipher}']
    with open(os.path.join(args.out_file, f'{input_file_name}_m55182va.txt'), 'w') as f:
        f.writelines(line)
