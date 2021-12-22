import argparse,os,re
parser = argparse.ArgumentParser()
parser.add_argument("Inputfilepath")
parser.add_argument("Outputfilepath")
args = parser.parse_args()

Morsecodedict = {
    '....' : 'h', '.-' : 'a', '-...' : 'b',
     '-.-.' : 'c', '-..' : 'd', '.' : 'e', 
     '..-.' : 'f', '--.' : 'g', '..' : 'i', 
     '.---' : 'j', '-.-' : 'k', '.-..' : 'l', '--' : 'm', '-.' : 'n',
      '---' : 'o', '.--.' : 'p', '--.-' : 'q', '.-.' : 'r', '...' : 's', 
      '-' : 't', '..-' : 'u', '...-' : 'v', '.--' : 'w', '-..-' : 'x', '-.--' : 'y',
       '--..' : 'z', '.-.-.-' : '.', '..--..' : '?', '--..--' : ',', '/' : ' ','--..--':', ',
       '.-.-.-':'.','..--..':'?','-..-.':'/','-....-':'-','-.--.':'(','-.--.-':')', '.----':'1',
        '..---':'2','...--' :'3','....-':'4', '.....':'5','-....':'6','--...':'7',
  '---..':'8', '----.':'9','-----':'0', 
}
#get names of the files
def getnames():
    global filenamelist
    filenamelist = sorted(os.listdir(args.Inputfilepath))
getnames()

def getname():#get the output name list of the files
    global outputlist
    outputlist = sorted(os.listdir(args.Outputfilepath))
getname()


def gettype():
    global filetype,f
    f = open(inputpath,"r")
    filetype = f.read(1)
    f.close

resultnum =0    
for file in filenamelist:
    inputpath = args.Inputfilepath + '/' + file
    gettype()
    #solve ceaser
    if filetype =="C":
        f = open(inputpath)
        content = f.read()
        colon = re.search(':', content).span() 
        plaintext = content[colon[1]:len(content)]
        plaintext = plaintext.rstrip()
        cipherText = ""
        alphabet = "xyzabcdefghijklmnopqrstuvwxyzabc"
        plaintextPosition = 0
        while plaintextPosition < len(plaintext):
            plaintextChar = plaintext[plaintextPosition]
            alphabetPosition = 3
            if plaintextChar == " ":
                cipherText += " "
                plaintextPosition += 1
            else: 
                while plaintextChar != alphabet[alphabetPosition]:
                    alphabetPosition += 1
                alphabetPosition -= 3
                cipherText = cipherText+alphabet[alphabetPosition]
                plaintextPosition += 1
                result = cipherText

    #solve hex
    if filetype =="H":
        f = open(inputpath)
        content = f.read()
        colon = re.search(':', content).span() 
        plaintext = content[colon[1]:len(content)]
        plaintext = plaintext.split(" ")
        ciphertext = []
        num = 0
        while num < len(plaintext):
            word = int(plaintext[num],16)
            ciphertext.append(chr(word))
            num += 1
        num = 0
        ciphertext = "".join(ciphertext)
        result = ciphertext

    #solve morse
    if filetype == "M":
        content = f.read()
        colon = re.search(':', content).span() 
        plaintext = content[colon[1]:len(content)]
        plain = plaintext.split(" ")
        wordlist = []
        for x in plain :
            if x != " ":
                wordlist.append(Morsecodedict[x])
        wordcontent = "".join(wordlist)
        result = wordcontent
    result = result.lower()

#output and rename
    print(result)
    rename = file.split(".")
    path = args.Outputfilepath + '/' + rename[0] + "_" +  "[user_name].txt"
    f = open(path,'w')
    f.write(result)
    os.rename(path,args.Outputfilepath + '/' + rename[0] + '_'+'g60486zz.txt')
