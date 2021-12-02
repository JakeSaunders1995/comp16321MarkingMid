import argparse,os,re
parser = argparse.ArgumentParser(description='Decrypt file.')
parser.add_argument("dir", nargs='+',help='directory containing files')
args = parser.parse_args()
storedfile = os.listdir(args.dir[0])
encryptedalphabet = "defghijklmnopqrstuvwxyzabc"
alphabet = "abcdefghijklmnopqrstuvwxyz"
morsecode = {'..-.': 'f', '-..-': 'x',
                 '.--.': 'p', '-': 't', '..---': '2',
                 '....-': '4', '-----': '0', '--...': '7',
                 '...-': 'v', '-.-.': 'c', '.': 'e', '.---': 'j',
                 '---': 'o', '-.-': 'k', '----.': '9', '..': 'i',
                 '.-..': 'l', '.....': '5', '...--': '3', '-.--': 'y',
                 '-....': '6', '.--': 'w', '....': 'h', '-.': 'n', '.-.': 'r',
                 '-...': 'b', '---..': '8', '--..': 'z', '-..': 'd', '--.-': 'q',
                 '--.': 'g', '--': 'm', '..-': 'u', '.-': 'a', '...': 's', '.----': '1', '/': " ",
                 '._._._': '.', '__..__': ',', '..__..': "?", '_._._.': ";", '___...': ":", '_...._': "-", '_.._.': "/",
                 '.____.': "'", '._.._.': '"', '_.__._': ")", '_.__.': "(", '-.-.--': "!"}
for i in range (0,len(storedfile)):
    prefix = storedfile[i].replace(".txt", "")
    filename = args.dir[0] + "/" + storedfile[i]
    encryptfile = open(filename,"r")
    ciphertext = encryptfile.read()
    plaintext = ""
    algorithm = ""
    Hexvalue = ""
    morsevalue = ""
    cipherstartpos = 0
    for x in range(0,len(ciphertext)):
        if ciphertext[x] == ":":
            algorithm = ciphertext[0:x]
            cipherstartpos = x
            break
    if algorithm == "Hex":
        for y in range (cipherstartpos+1,len(ciphertext)):
            if ciphertext[y] != " ":
                Hexvalue = Hexvalue + ciphertext[y]
        decodevalue = bytearray.fromhex(Hexvalue)
        plaintext = decodevalue.decode()
    elif algorithm == "Morse Code":
        ciphertext = ciphertext.replace("\n","") + " "
        for w in range (cipherstartpos+1,len(ciphertext)):
            if ciphertext[w] != " ":
                morsevalue = morsevalue + ciphertext[w]
            else:
                plaintext = plaintext + morsecode[morsevalue]
                morsevalue = ""
    elif algorithm == "Caesar Cipher(+3)":
        for z in range(cipherstartpos + 1, len(ciphertext)):
            if ciphertext[z] in alphabet:
                for a in range(0,len(encryptedalphabet)):
                    if ciphertext[z] == encryptedalphabet[a]:
                        plaintext = plaintext + alphabet[a]
            else:
                plaintext = plaintext + ciphertext[z]

    writefilepos = str(args.dir[1]) + "/" + prefix + "_g92198jz.txt"
    writefile = open(writefilepos, "w")
    writefile.write(plaintext)

