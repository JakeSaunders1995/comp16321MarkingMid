import sys
import os 
import os.path

encrypted = sys.argv[1]
decrypted = sys.argv[2]




def caeserDecrypt(caeserdatastrip):
    caeser = ''
    for i in caeserdatastrip:
        if (i == ' '):
            caeser += ' '
        else:
            caeser += (chr(ord(i) - 3))
    return caeser

MORSEtoENG = {
    '....' : 'h', '.-' : 'a', '-...' : 'b',
     '-.-.' : 'c', '-..' : 'd', '.' : 'e',
      '..-.' : 'f', '--.' : 'g', '..' : 'i',
       '.---' : 'j', '-.-' : 'k', '.-..' : 'l',
        '--' : 'm', '-.' : 'n', '---' : 'o', 
        '.--.' : 'p', '--.-' : 'q', '.-.' : 'r',
         '...' : 's', '-' : 't', '..-' : 'u',
          '...-' : 'v', '.--' : 'w', '-..-' : 'x',
           '-.--' : 'y', '--..' : 'z', 
           '.-.-.-' : '.', '..--..' : '?',
            '--..--' : ',', '/' : ' '
}

alphabets = "xyzabcdefghijklmnopqrstuvwxyzabc"

for filename in os.listdir(encrypted):
    input = open(encrypted + "/" + filename,'r') 
    while True:
        data = input.read()
        outfile = filename[:-4]
        path = decrypted
        if not data:
            break
        if data.startswith('Hex'):
            hexdatastrip=data[4:]
            value = bytes.fromhex(hexdatastrip).decode('utf-8')
            outputFile = decrypted + '/' + outfile + '_' + 'p37429am.txt'
            output = open(outputFile, 'w')
            output.write(str(value))
            output.close()

        elif data.startswith('Caesar'):
            caeserdatastrip=data[18:]
            answer = caeserDecrypt(caeserdatastrip)
            outputFile = decrypted + '/' + outfile + '_' + 'p37429am.txt'
            output = open(outputFile, 'w')
            output.write(str(answer))
            output.close()

        elif data.startswith('Morse'):
            morsedatastrip=data[11:]
            morsedatastrip = morsedatastrip.split()
            # morsedatastrip=morsedatastrip+"c"
            # lenword = len(morsedatastrip)
            translation = ''
            for i in morsedatastrip:
                if i != ' ':
                    if i not in MORSEtoENG:
                        break

                    translation = translation + i
                    answer = (MORSEtoENG[translation])

                    outputFile = decrypted + '/' + outfile + '_' + 'p37429am.txt'
                    output = open(outputFile, 'a')
                    output.write(str(answer))
                    output.close()

                    translation = ''
# with open(decrypted, 'w+') as output:
#   output.write(translation)


