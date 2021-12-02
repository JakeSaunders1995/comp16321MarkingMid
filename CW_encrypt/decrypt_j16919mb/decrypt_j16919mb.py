import sys, os

def writeDataToFile(filename, data):
    for i in range(len(filename)):
        if filename[i] == '.':
            fileExtention = filename[i:]
            filename = filename[:i] ## remove the file extention (most likely .txt)
            break
    else:
        fileExtention = ''

    fileWrite = open((folderWritePath+'/'+filename+'_'+username+fileExtention), "wt")
    ## write statement
    fileWrite.write(data)
    fileWrite.close()

## Pass value and return key
def getKey(value):
    if value == '/':
        return ' ' ## if space return space character
    for key, val, in MorseCodeDict.items():
        if value == val:
            return key
    return "Error, does not exist."

def hexDecode(data):
    for i in range(len(data)):
        if data[i] == ":":
            hexData = data[i + 1:] ## check this
            break
    hexData = hexData.strip(" ")
    cypherString = bytes.fromhex(hexData).decode("utf-8")
    return cypherString.lower()## since utf8 character can also encode ascii this is not a problem

def morseDecode(data):
    for i in range(len(data)):
        if data[i] == ':':
            data = data[i+1:]
            break
    cypherString = "" ## decrypted sting
    character = "" ## morse char
    for i in range(len(data)):
        if data[i] == ' ':
            ## check this
            cypherString += getKey(character) ## append found character to the decyphered string
            
            character = "" ## empty char buffer
        else:
            character += data[i]
    cypherString += getKey(character) ## append last character incase of no space at the end of string
    return cypherString

def ceaserDecode(data):
    shift = ""
    for i in range(len(data)):
        if data[i].lower() == "+": ## maybe do one which caputures a negative too
            while not (data[i+1] == ")"):
                shift += data[i+1]
                i += 1
        if data[i] == ":": ## cut of non cypher data
            data = data[i+1:]
            break
    cypherString = ""

    data.lower()

    for i in range(len(data)):
        if ord(data[i]) > 96 and ord(data[i]) < 123:
            cypherString += chr((((ord(data[i])-97)-int(shift))%26)+97)
        else:
            cypherString += data[i] ## add space or new line 
    return cypherString ## return decoded


## the sheet did not specify the character array
characters = "abcdefghijklmnopqrstuvwxyz01234567989.?!,:;-()[]{}'"
username = "j16919mb"
MorseCodeDict = {'a':'.-','b':'-...','c':'-.-.',
                'd':'-..','e':'.','f':'..-.',
               'g':'--.','h':'....','i':'..',
                'j':'.---','k':'-.-','l':'.-..',
                'm':'--','n':'-.','o':'---',
                'p':'.--.','q':'--.-','r':'.-.',
                's':'...','t':'-','u':'..-',
                'v':'...-','w':'.--','x':'-..-',
                'y':'-.--','z':'--..','1':'.----',
                '2':'..---','3':'...--','4':'....-',
                '5':'.....','6':'-....','7':'--...',
                '8':'---..','9':'----.','0':'-----',
                ',':'--..--','.':'.-.-.-','?':'..--..',
                '/':'-..-.','-':'-....-','(':'-.--.',
                ')':'-.--.-','!':'-.-.--',"'":'.----.'}

folderReadPath = (sys.argv)[1] 
folderWritePath = (sys.argv)[2]

for filename in os.listdir(folderReadPath):
    
    fileR = open(folderReadPath+"/"+filename, "rt")
    while True:
        line = fileR.read()
        if not line:
            break
        
        if line[0].lower() == "h":
            decodedString = hexDecode(line)
        elif line[0].lower() == "m":
            decodedString = morseDecode(line)
        elif line[0].lower() == "c":
            decodedString = ceaserDecode(line)
        else:
            print("Unrecognized encryption.")

    ## write decoded message into file

    fileR.close()
    writeDataToFile(filename, decodedString)