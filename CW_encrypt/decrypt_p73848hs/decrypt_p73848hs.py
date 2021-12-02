import sys
import os
username = "_p73848hs"


#open files
#saves the content in filecontent
#split up the algortihm and the encrypted text
#create a new list called nospace
#nospace contains encrypted text but split up wherever there is a space
files=os.listdir(sys.argv[1].strip("./"))
for filename in files:
    file = open(sys.argv[1].strip("./")+"/"+filename)
    for line in file:
        filecontent=line
    file.close()
    filecontent=filecontent.split(":")
    algorithm=filecontent[0]
    encrypted=filecontent[1]
    nospace=encrypted.split()


#Output starts as empty
#the mehtod of encryption is determiened
    Output=""
    if algorithm=="Hex":
        #turns hex into binary
        #then truns binary into ascii character
        #concatenate the ascii character into Output
        #repeat for each item in nospace(each hex number)
        for char in range (len(nospace)):
            bytes_object=bytes.fromhex(nospace[char])
            ascii_string=bytes_object.decode("ASCII")
            Output= Output + ascii_string
    
    
    elif algorithm=="Caesar Cipher(+3)":
#if character is " " then dont decrypt
#otherwise turn the character into binary
#takeaway 3 from the binary number
#convert it back to a character
#concatenate the decrypted character to Output
#repeat for each character in encrypted
        for char in range (len(encrypted)):
            if encrypted[char] == " ":
                Output = Output + " "
            else:
                Output=Output+ (chr(ord(encrypted[char])-3))
    
    
    elif algorithm=="Morse Code":
#this is a reference to what each morse code is equal to in the alhphabet
#this is a dictionary
        MorseToChar = {'.-':'A','-...':'B',
                        '-.-.':'C','-..':'D', '.':'E',
                        '..-.':'F', '--.':'G', '....':'H',
                        '..':'I', '.---':'J', '-.-':'K',
                        '.-..':'L', '--':'M', '-.':'N',
                        '---':'O','.--.':'P', '--.-':'Q',
                        '.-.':'R', '...':'S', '-':'T',
                        '..-':'U', '...-':'V', '.--':'W',
                        '-..-':'X', '-.--':'Y', '--..':'Z',
                        '.----':'1','..---':'2', '...--':'3',
                        '....-':'4', '.....':'5', '-....':'6',
                        '--...':'7', '---..':'8', '----.':'9',
                        '-----':'0', '--..--':', ', '.-.-.-':'.',
                        '..--..':'?', '-..-.':'/', '-....-':'-',
                '-.--.':'(', '-.--.-':')'}
#if character is "/" then it means the word ends, so add " "
#otherwise turn the morsecode into string character using the dictionary
#concatenate the decrypted character to Output
#repeat for each element in no space
        for char in range (len(nospace)):
            if nospace[char]=="/":
                Output = Output + " "
            else:
                Output = Output + MorseToChar[nospace[char]]
    
    
#turns Output to all lower case
    Output = Output.lower()
    file = open(sys.argv[2].strip("./")+"/"+filename+username,"w")
    file.write("encryption is fun!")	
