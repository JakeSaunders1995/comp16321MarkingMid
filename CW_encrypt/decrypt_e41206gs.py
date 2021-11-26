import sys,os
files = os.listdir(sys.argv[1])
for j in files:
    path = sys.argv[1]+"/"+j
    file = open(path)
    string = file.read()
    file.close()
    morseD={'.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
            '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
            '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
            '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
            '-.--':'y','--..':'z','-----':'0','.----':'1','..---':'2','...--':'3',
            '....-':'4','.....':'5','-....':'6','--...':'7','---..':'8','----.':'9',
            '.-.-.-':'.','--..--':',','..--..':'?','.----.':'\'','-.-.--':'!','-..-.':'/',
            '-.--.':'(','-.--.-':')','.-...':'&','---...':':','-.-.-.':';','.-..-.':'\"',
            '/':' ', '-....-':'-'
            }
    interpretation = 1
    if('morse' in string.lower()):
        interpretation = 1
    if('hex' in string.lower()):
        interpretation = 2
    if('caesar' in string.lower()):
        interpretation = 3
    string = string.split(":")[1]
    letters=[i for i in string.split()]
    decriptedText=""
    if(interpretation == 1):
        for i in letters:
            decriptedText += morseD.get(i)
    if(interpretation == 2):
        for i in letters:
            decriptedText += chr(int(i,16))
    if(interpretation == 3):
        for i in string:
            if i!=' ':
                decriptedText+=chr(ord(i)-3)
            else:
                decriptedText+=' '
    path = sys.argv[2]+"/"+j.split(".")[0]+"_e41206gs."+j.split(".")[1]    
    file = open (path,"w")
    file.write(decriptedText.lower())
    file.close()
