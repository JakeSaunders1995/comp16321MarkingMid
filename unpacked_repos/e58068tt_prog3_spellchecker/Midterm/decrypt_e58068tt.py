import sys, os, os.path

source = str(sys.argv[1])
destination = str(sys.argv[2])
sourceFiles = os.listdir(source)

morseDictionary = {
'.-':'a', '-...':'b','-.-.':'c','-..':'d','.':'e',
'..-.':'f','--.':'g','....':'h','..':'i','.---':'j',
'-.-':'k','.-..':'l','--':'m','-.':'n','---':'o',
'.--.':'p','--.-':'q','.-.':'r','...':'s','-':'t',
'..-':'u','...-':'v','.--':'w','-..-':'x','-.--':'y',
'--..':'z','-----':'0','.----':'1','..---':'2','...--':'3',
'....-':'4','.....':'5','-....':'6','--...':'7','---..':'8',
'----.':'9','.-.-.-':'.','-.-.--':'!','..--..':'?',
'--..--':',','---...':':','-.--.-':')','-.--.':'(',
'/':' '
}

hexDictionary = {
'a':'10', 'b':'11','c':'12','d':'13',
'e':'14','f':'15', '0':'0', '1':'1',
'2':'2','3':'3','4':'4','5':'5','6':'6',
'7':'7','8':'8','9':'9'
}

letterList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']



i = 0
while(i < len(sourceFiles)):
    file = open(source + sourceFiles[i])
    content = file.read()
    decryption = ""
    x = 0
    while(True):
        if(content[x] == ":"): #Found where text starts
            x += 1
            break
        x += 1

    if(content[:5].lower() == "morse"): #Morse code
        tempMorse = ""

        while(True):
            try:
                if(content[x] != " "):
                    tempMorse += content[x]
                    x += 1
                else:
                    decryption += morseDictionary[tempMorse]
                    tempMorse = ""
                    x += 1
            except:
                decryption += morseDictionary[tempMorse]
                break



    elif(content[:3].lower() == "hex"): #hex
        tempHex = ""

        while (True):
            try:
                if(content[x] != " "):
                    tempHex += content[x]
                    x += 1
                else:
                    tempHexValue = ((int(hexDictionary[tempHex[0]])) * 16) + int(hexDictionary[tempHex[1]])
                    decryption += chr(tempHexValue)
                    tempHex = ""
                    x += 1
            except:
                tempHexValue = ((int(hexDictionary[tempHex[0]])) * 16) + int(hexDictionary[tempHex[1]])
                decryption += chr(tempHexValue)
                break


    elif(content[:6].lower() == "caesar"):
        tempLetter = ""

        while(True):
            try:
                if(content[x] != " "):
                    letterValue = ord(content[x].lower()) - 97 #Get number in the alphabet
                    if(letterValue < 3):
                        newLetter = letterList[23 + letterValue]
                    else:
                        newLetter = letterList[letterValue - 3]
                    decryption += newLetter
                    x += 1
                else:
                    decryption += " "
                    x += 1

            except:
                break

    output = open(destination + sourceFiles[i][:-4] + "_e58068tt.txt", "x")
    output.write(decryption)

    i += 1
