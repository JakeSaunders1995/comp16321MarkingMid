import os
import sys
import re
import contextlib

finput = sys.argv[1] #input file from user
foutput = sys.argv[2] #output file from user

                
with open(finput, 'r') as fin:
        content = fin.read()
        morse = {'..-.': 'f', '-..-': 'x',
                 '.--.': 'p', '-': 't', '..---': '2',
                 '....-': '4', '-----': '0', '--...': '7',
                 '...-': 'v', '-.-.': 'c', '.': 'e', '.---': 'j',
                 '---': 'o', '-.-': 'k', '----.': '9', '..': 'i',
                 '.-..': 'l', '.....': '5', '...--': '3', '-.--': 'y',
                 '-....': '6', '.--': 'w', '....': 'h', '-.': 'n', '.-.': 'r',
                 '-...': 'b', '---..': '8', '--..': 'z', '-..': 'd', '--.-': 'q',
                 '--.': 'g', '--': 'm', '..-': 'u', '.-': 'a', '...': 's', '.----': '1'}
        # content = content.replace("Hex","").replace(":","").replace("Caesar Cipher(+3)","").replace("Morse Code","")
        # --------------------------------(for hex)--------------------
        def hextype(content) : 
                content = content.replace("Hex","").replace(":","").replace("Caesar Cipher(+3)","").replace("Morse Code","")             
                a_string = bytes.fromhex(content)
                hexdecode = a_string.decode("ascii")
                return hexdecode
# ---------------------------------------------(for caesar cipher)------
        def decryption(key, content):
                content = content.replace("Hex","").replace(":","").replace("Caesar Cipher(+3)","").replace("Morse Code","")
                decipherText=""
                alphabet="abcdefghijklmnopqrstuvwxyzabc"
                # content=content.replace("Caesar Cipher(+3)","")
                for letter in content:
                        if letter in alphabet:
                                letter_index = (alphabet.find(letter)-key)%len(alphabet)
                                decipherText=decipherText+alphabet[letter_index]
                        else:
                                decipherText = decipherText+letter
                return decipherText
# ----------------------------------------------(for morsecode)------
        def morsecode(content):
                content =content.replace("Hex","").replace(":","").replace("Caesar Cipher(+3)","").replace("Morse Code","")
                content=re.findall(r'\S+', content)
                reOut1=""
                for i in content:
                                if i in morse:
                                        sc = morse[i]
                                        reOut1=reOut1+sc
                                if i not in morse:
                                        reOut1=reOut1+i
                                more=reOut1.replace("/"," ")
                return more
        result =""
        # char=content[0]
        if content.startswith("M") == True:
                function=morsecode(content)
                result=result+function
        elif content.startswith("C") == True:
                function=decryption(3, content)
                result=result+function
        elif content.startswith("H") == True:
                function=hextype(content)
                result=result+function
        
        
with open(foutput, "w") as fout:
        with contextlib.redirect_stdout(fout):

                # decrypted=decryption(3, content)
                print(result)


