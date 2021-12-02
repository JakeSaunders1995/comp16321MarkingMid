import sys, os
a = sys.argv[1]
b = os.listdir(a)
for c in b:
    d = a + "/" + c
    with open(d, 'r') as decryptionprogram:
        decryptionprogram = decryptionprogram.read()
        morsedict = {'.-': 'a', '-...': 'b', '-.-.': 'c',
                     '-..': 'd', '.': 'e', '..-.': 'f',
                     '--.': 'g', '....': 'h', '..': 'i',
                     '.---': 'j', '-.-': 'k', '.-..': 'l',
                     '--': 'm', '-.': 'n', '---': 'o',
                     '.--.': 'p', '--.-': 'q', '.-.': 'r',
                     '...': 's', '-': 't', '..-': 'u',
                     '...-': 'v', '.--': 'w', '-..-': 'x',
                     '-.--': 'y', '--..': 'z', '/': " ",
                     '.----': '1', '..---': '2', '...--': '3',
                     '....-': '4', '.....': '5', '-....': '6',
                     '--...': '7', '---..': '8', '----.': '9',
                     '-----': '0', '--..--': ',', '.-.-.-': '.',
                     '..--..': '?', '-..-.':'/', '-....-': '-',
                     '-.--.': '(', '-.--.-': ')', '---...': ':',
                     '-.-.-.': ';', '.----.': '\'', '.-..-.': '"',
                     '-...-': '=', '.-.-.': '+', '.--.-.': '@'
                     }
        output = ""
        if "Morse Code:" in decryptionprogram:
            decryptionprogram = decryptionprogram.replace("Morse Code:", "")
            decryptionprogram = decryptionprogram.split()
            i = 0
            while i<len(decryptionprogram):
                if decryptionprogram[i] in morsedict:
                    output = output + morsedict[decryptionprogram[i]]
                    i += 1
                else:
                    break
        elif "Caesar Cipher(+3):" in decryptionprogram:
            cipherText = ""
            alphabet = "XYZABCDEFGHIJKLMNOPQRSTUVWXYZABC".lower()
            plaintextPosition = 18
            while plaintextPosition < len(decryptionprogram):
                plaintextChar = decryptionprogram[plaintextPosition]
                alphabetposition = 3
                if plaintextChar not in alphabet:
                    cipherText = cipherText + plaintextChar
                else:
                    while plaintextChar != alphabet[alphabetposition]:
                        alphabetposition = alphabetposition + 1
                    alphabetposition = alphabetposition - 3
                    cipherText = cipherText + alphabet[alphabetposition]
                plaintextPosition = plaintextPosition + 1
            output = cipherText
        elif "Hex:" in decryptionprogram:
            decryptionprogram = decryptionprogram.replace("Hex:", "")
            decryptionprogram = decryptionprogram.split()
            i = 0
            while i<len(decryptionprogram):
                num = int(decryptionprogram[i], 16)
                output = output + chr(num)
                output = output.lower()
                i += 1

    e = c.replace('.txt','')
    f = sys.argv[2] + "/" + e + "_j06724tc" + ".txt"
    g = open(f, 'w')
    g.write(output)
