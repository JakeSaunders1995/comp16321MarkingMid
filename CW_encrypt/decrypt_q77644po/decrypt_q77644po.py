import sys
inputpath=sys.argv[1]
outputpath=sys.argv[2]



def decrypt(s):
    a=s.split(':')[0][0]
    b=s.split(':')[1]

    #-----------------------------------------------------------------hex---------------------------------------------------------------------
    if a == 'H':
        hexs=b.split(' ')
        output=''
        for i in range(len(hexs)):
            output=output+chr(int(hexs[i],16))
        return output
    

    #----------------------------------------------------------------Caesar--------------------------------------------------------------------
    if a == 'C':
        output=''
        for i in range(len(b)-1):
            if b[i] != ' ':
                if ord(b[i])> 99:
                    output=output+chr(ord(b[i])-3)
                else:
                    output=output+chr(ord(b[i])+23)
            else:
                output=output+' '
        return(output)


    #-----------------------------------------------------------------Morse----------------------------------------------------------------------
    if a == 'M':
        library=    ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '.----', '..---', '...--',
                    '....-', '.....', '-....', '--...', '---..', '----.', '-----', '--..--', '.-.-.-', '..--..', '-..-.', '-....-', '-.--.', '-.--.-']
        words=b.split('/')
        output=''
        for i in range(len(words)):
            letters=words[i].split(' ')
            if letters[-1]=='':
                letters.pop()
            if letters[0]=='':
                letters.pop(0)
            
            word=''
            for j in range(len(letters)):
                word=word+chr(library.index(letters[j])+97)
            output=output+word+' '
        return(output[:-1])
    return('damn')


import os
files=os.listdir(inputpath)
for i in range(len(files)):
    if files[i].endswith(".txt"):
        inputname=inputpath+'/'+files[i]
        inputfile=open(inputname)
        outputname=files[i][:-4]+'_q77644po.txt'
        outputfile=open(outputpath+'/'+outputname,'w')
        outputfile.write(decrypt(inputfile.read()))
        
        


    
