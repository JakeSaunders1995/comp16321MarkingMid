import sys
import os
import string

def listdir_nohidden(path): 
    for f in os.listdir(path): 
        if not f.startswith('.'): 
            yield f 

def hex2dec(string_num):
    return str(int(string_num.upper(), 16))

Values = 'abcdefghijklmnopqrstuvwxyz0123456789'
Keys= ['.-','-...','-.-.','-..','.','..-.','--.','....',
		  '..','.---','-.-','.-..','--','-.','---','.--.',
          '--.-','.-.','...','-', '..-','...-','.--','-..-',
          '-.--','--..','-----','.----','..---','...--',
          '....-','.....','-....','--...','---..','----.']

def main():
    inputPath=sys.argv[1]
    outputPath=sys.argv[2]
    filesPath=listdir_nohidden(inputPath)
    for i in filesPath:
        file_object = open(inputPath+'/'+i)
        line = file_object.readlines()
        tempStrings=line[0].split(':')
        x=i[:-4]
        if tempStrings[0]=='Hex':
            lastString=tempStrings[1].split(' ')
            testString=''
            for j in lastString:
                testString=testString+(chr(int(hex2dec(j))))
            output_object=open(outputPath+'/'+x+'_g58440zy.txt','w+')
            output_object.write(testString.lower())
        elif  tempStrings[0]=='Morse Code':
            lastString=tempStrings[1].split(' ')
            testString=''
            for j in lastString:
                if j=='/':
                    testString=testString+' '
                for k in range(len(Keys)):
                    if j==Keys[k]:
                        testString=testString+Values[k]
            output_object=open(outputPath+'/'+x+'_g58440zy.txt','w+')
            output_object.write(testString.lower())
        elif  tempStrings[0]=='Caesar Cipher(+3)':
            lastString=tempStrings[1]
            testString=''
            for j in lastString:
                if j in ['a', 'b', 'c']:
                    testString=testString+chr(ord(j)+23)
                elif j in string.ascii_letters:
                    testString=testString+chr(ord(j)-3)
                else :
                    testString=testString+j
            output_object=open(outputPath+'/'+x+'_g58440zy.txt','w+')
            output_object.write(testString)
        else:
            pass
            
if __name__ == '__main__':
    main()



