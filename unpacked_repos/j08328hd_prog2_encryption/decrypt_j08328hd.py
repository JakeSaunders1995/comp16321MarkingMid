import sys, os

alph = "abcdefghijklmnopqrstuvwxyz"
morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', 
'.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', 
'-..-', '-.--', '--..']

other = '''0123456789&'@)(:,=-+?/".'''
morseOther=['-----','.----','..---','...--','....-','.....','-....','--...','---..',
'----.','.-...','.----.','.--.-.','-.--.-','-.--.','---...','--..--','-...-','-....-',
'.-.-.','..--..','-..-.','.-..-.','.-.-.-']

print(other)
count = 0

inPath = sys.argv[1]
outPath = sys.argv[2]

inFiles = os.listdir(inPath)
inFiles.sort()

for file in inFiles:
    count += 1
    fIn = open(inPath + "/" + file, "r")
    fOut = open(outPath + "/test_file"+str(count)+"_j08328hd.txt", "w")
    data = fIn.read()
    dataAr = data.split(':')

    decrypted = ''

    if dataAr[0] == 'Hex':
        decrypted = bytearray.fromhex(dataAr[1]).decode()
    elif dataAr[0] == 'Caesar Cipher(+3)':
        for i in dataAr[1]:
            if i in alph:
                pos = alph.index(i)
                if pos < 3:
                    pos = pos + 26
                decrypted = decrypted + alph[pos-3]
                continue
            decrypted = decrypted + i

    elif dataAr[0] == "Morse Code":
        code = dataAr[1].split(" ")
        for i in code:
            if i == '/':
                decrypted = decrypted + " "
                continue
            elif i in morse:
                pos = morse.index(i)
                decrypted = decrypted + alph[pos]
            elif i in morseOther:
                pos = morseOther.index(1)
                decrypted = decrypted + other[pos]
            
    print(decrypted.lower())
    fOut.write(decrypted.lower())
    fOut.close()