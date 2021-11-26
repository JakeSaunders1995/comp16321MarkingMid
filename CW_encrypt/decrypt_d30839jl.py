import os
import sys
Input = sys.argv[1]
Output = sys.argv[2]
input_file = os.listdir(Input)
for p in input_file:
    file = open(Input + "/" + p,'r')
    text = file.readline()
    text += " "
    text2 = ""
    text3 = ""
    alphabet3 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]
    alphabet2 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    alphabet1 = ["d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c"]
    morse = ['.-','-...','-.-.', '-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..','-----','.----','..---','...--','....-','.....','-....','--...','---..','----.']
            



    if text[0] == "H":
                y = 4
                for x in range(y ,(len(text))):
                    if x % 3 == 1:
                        text2 = text[x] + text[x+1]
                        text3 += (bytes.fromhex(text2).decode('ascii'))
                        
    elif text[0] == "C":
                y = 18
                for x in range(y ,(len(text))):
                    if text[x] == " ":
                        text2 += text[x]
                    else:
                        location1 = (alphabet1.index(text[x]))
                        text2 += alphabet2[location1]
                        text3 = text2
                        
    elif text[0] == "M":
                y = 11
                for x in range(y ,(len(text))):
                    
                    if text[x] == " ":
                        for i in range(0,35):
                            if (text2) == (morse[i]):
                                location1 = (morse.index(morse[i]))
                                location2 = alphabet3[int(location1)]
                                text3 += location2
                                text2 = ""
                    elif text[x] == "/":
                        text3 += " "
                    else: 
                        text2 += text[x]
    print(text3)
    filew = open(Output + "/" + p.replace(".txt" , "") + "d30839jl",'w') 
    filew.write(text3)
               # if text[0] == "H":
                #    print(text2)
                 #   filew.write(text2) 
                #elif text[0]== "C":
                 #   print(text2)
                  #  filew.write(text2) 
                #elif text[0]== "M":
                 #   print(text3)
                  #  filew.write(text3) 

                      


