import sys

method_list = ["hexadecimal","caesar +3","morseCode"]



def determineMethod():
    with open(sys.argv[1], 'r') as file:
        for line in file:
            for word in line.split():
                def checkHex(word):
                    if ((word < '0' or word > '9') and (word < 'a' or word > 'f')):
                        return    
                    hexDec = bytes.fromhex(word).decode('utf-8')
                    with open(sys.argv[2],'w') as output:
                         output.write(hexDec)
                checkHex(word)

               
                def checkCaesar(word):
                    for char in word:
                        if char.isdigit():
                            return False
                    plaintext = ""
                    cipherText = word
                    cipherTextPosition = 0
                    while (cipherTextPosition < len(cipherText)):
                        cipherTextChar = cipherText[cipherTextPosition]
                        ASCIIValue = ord(cipherTextChar)
                        ASCIIValue = ASCIIValue + 3
                        plaintext = plaintext + chr(ASCIIValue)
                        cipherTextPosition = cipherTextPosition + 1
                    print(plaintext)
                checkCaesar(word)
                      



            
                
determineMethod()







# morse code decrypter


#character = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
         #    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
          #   '0','1','2','3','4','5','6','7','8','9']
  #‘0’ represents a dot, and ‘1’ represents a dash.
# code = ['.-','-...','-.-.','-..','.','..-.','--.','....','..',
  #        '.---','-.-','.-..','--','-.','---','.--.','--.-','.-.',
   #       '...','-','..-','...-','.--','-..-','-.--','--..','-----',
    #      '.----','..---','...--','....-','.....','-....','--...',
    #      '---..','----.']