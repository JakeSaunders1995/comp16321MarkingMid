import os,sys

def caeser_decrypt(word_list):
    decrypt_list = []
    for encrypt in word_list:
        plainText = ""
        alphabet = "xyzabcdefghijklmnopqrstuvwxyzabc"
        ciphertextPosition = 0 
        while (ciphertextPosition < len(encrypt)):
            ciphertextChar = encrypt[ciphertextPosition]
            alphabetPosition = 3
            while ciphertextChar != alphabet[alphabetPosition]:
                alphabetPosition = alphabetPosition + 1
            alphabetPosition = alphabetPosition - 3
            plainText = plainText + alphabet[alphabetPosition]
            ciphertextPosition = ciphertextPosition + 1
        decrypt_list.append(plainText)
    decrypt_word = ""
    for word in decrypt_list:
        decrypt_word+=word
        decrypt_word+=" "
        
    return decrypt_word
def hex_decrypt(words):
    hex_words = ""
    for word in words:
        a = chr(int(word,16))
        hex_words+=a
    return hex_words

def morse_decrypt(words):
    global morse_words
    morse_words = ""
    encrypt = {'.-':'a','-...':'b', '-.-.':'c',
               '-..':'d', '.':'e', '..-.':'f',
               '--.':'g', '....':'h', '..':'i',
               '.---':'j','-.-':'k', '.-..':'l',
               '--':'m', '-.':'n', '---':'o',
               '.--.':'p', '--.-':'q', '.-.':'r',
               '...':'s','-':'t','..-':'u',
               '...-':'v', '.--':'w', '-..-':'x',
               '-.--':'y', '--..':'z', '.....':' ',
               '-----':'0','.----':'1','..---':'2',
               '...--':'3','....-':'4','.....':'5',
               '-....':'6','--...':'7','---..':'8',
               '----.':'9'}
    for word in words:
        if word in encrypt:
            morse_words+=encrypt[word]
        elif word =='/':
            morse_words+=" "
    return morse_words
            
inp_file = sys.argv[1]
ba= os.listdir(inp_file)
#os.mkdir(sys.argv[2])       
for k in ba:
    r= inp_file+"/"+k
    with open(r,'r') as file:
        a= file.readline()
        b=a.split(":")
        c=b[1]
        d=b[0]
        words = c.split(" ")
        if d =='Hex':
            word = hex_decrypt(words).lower()
        elif d=='Caesar Cipher(+3)':
            word = caeser_decrypt(words).lower()
        elif d=='Morse Code':
            word = morse_decrypt(words).lower()
    g= k.replace('.txt','')
    w= sys.argv[2]+"/"+g+"_g39786dp"+".txt"
    x = open(w,'w')
    x.write(word)
        
