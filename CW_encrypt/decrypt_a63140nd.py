import os
d= os.getcwd()
fname= os.path.join(d, "midterm_files/Example_inputs/Example_inputs_program2/test_file1.txt")
file = open(fname, "r")
split_string= file.read().split(":")

algorithm= split_string[0]
encryptedText= split_string[1]
if algorithm == "Caesar Cipher(+3)":
    words= encryptedText.split()
    count=0
    finalMessage=''
    for i in range (0, len(words)):
        cipherText= list(words[count])
        count= count + 1
        plainText=""
        alphabet="xyzabcdefghijklmnopqrstuvwxyzabc "
        cipherTextPos=0
        while cipherTextPos<len(cipherText):
            cipherTextChar=cipherText[cipherTextPos]
            alphabetPos=3
            while cipherTextChar != alphabet[alphabetPos]:
                alphabetPos=alphabetPos+1
            alphabetPos=alphabetPos-3
            plainText=plainText + alphabet[alphabetPos]
            cipherTextPos=cipherTextPos+1
        finalMessage= finalMessage +" "+ str(plainText)
    
if algorithm == "Hex":
    characters= encryptedText.split()
    count=0
    finalMessage=''
    for i in range(0, len(characters)):
        byte_array = bytearray.fromhex(characters[count])
        num= byte_array.decode()
        count = count + 1
        finalMessage= finalMessage + str(num)
    
if algorithm == "Morse Code":
    citext=encryptedText.split()
    finalMessage=''
    MORSE_CODE_DICT = { 'a':'.-', 'b':'-...',
                    'c':'-.-.', 'd':'-..', 'e':'.',
                    'f':'..-.', 'g':'--.', 'h':'....',
                    'i':'..', 'j':'.---', 'k':'-.-',
                    'l':'.-..', 'm':'--', 'n':'-.',
                    'o':'---', 'p':'.--.', 'q':'--.-',
                    'r':'.-.', 's':'...', 't':'-',
                    'u':'..-', 'v':'...-', 'w':'.--',
                    'x':'-..-', 'y':'-.--', 'z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-',' ':'/'}
    count=0
    for i in range(0, len(citext)):
        decipher = list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext[count])]
        finalMessage= finalMessage + str(decipher)
        count= count + 1
    
outFileName= os.path.join(d, "midterm_files/output_files/output_program2/test_file1_a63140nd.txt")
with open(outFileName, 'w') as f:
    f.write(finalMessage)
