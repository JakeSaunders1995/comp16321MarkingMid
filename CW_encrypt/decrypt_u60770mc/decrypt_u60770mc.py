import sys

file = open(sys.argv[1],"r")
strText = file.read()           #open the input file and set strText to equal the content of the input
enctype = ""
encText = ""
outText = ""
temp = 0
i = 0
alphabet = "abcdefghijklmnopqrstuvwxyz"     #Variables for the decryption
alphaList = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
morseAlpha = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
tempMorse = ""
Morseword = False
while strText[i] != ":":
    enctype = enctype + strText[i]          #While loop to make enctype = what type of encryption it is
    i += 1

for x in strText[i+1:len(strText):1]:
    i += 1
    encText = encText + strText[i]          #For loop to add all the text after ":" to the encText variable


if enctype == "Hex":                #used if statements to determine what type of encryption it was
    encText = bytes.fromhex(encText)
    outText = encText.decode("ascii")       #If statement to decrypt the hex using a built in class method .fromhex
                                            #and .decode() 
if enctype == "Caesar Cipher(+3)":
    for x in encText:
        if x == " ":
            outText += " "
        else:
            temp = alphabet.index(x) -3     #Caeser shift decryption, found the index value in the string alphabet
            outText = outText + alphabet[temp] #Of where x would be then shifted that value by - 3 to find the index
                                                #Value of where the letter would be in alphabet


if enctype == "Morse Code":
    for x in encText:
        if x == " ":
            Morseword = True
        if x == "/":
            outText += " "  
        elif Morseword == True:             #Iterates through the string until it finds a " ", once this happens
            for y in morseAlpha:            #it sets a variable to equal true as that is when a full word in morse
                if tempMorse == y:          #is created, then it searches through the morse alphabet list to find it
                    temp = morseAlpha.index(y) #and finds its index location
                    outText += alphaList[temp]
                    tempMorse = ""
                    Morseword = False
                else:
                    Morseword = False
        else:
            tempMorse += x
      
   
            
file = open(sys.argv[2],"w")        #Writing the output text to a txt file
file.write("%s" %(outText))
file.close()
