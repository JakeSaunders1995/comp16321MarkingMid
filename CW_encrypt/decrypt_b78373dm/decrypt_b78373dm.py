import sys
import os

#decryption algorithms

def morse(string):
    string+=" "
    index=11
    result=""
    #detecting words
    while index<len(string)-1:
        letter=""
        if string[index]=="/":
            result+=" "
            
        else:
            #detecting letter
            while string[index]!=" ":
                letter+=string[index]
                index+=1
            #decode letter
            result+=convert[letter]
        index+=1
            
       
    return result
                
            

def caesar(string):
    result=""
    for char in string[18:]:
        if char==" ":
            result+=" "
        else:
            current=ord(char)
            current-=3
            if current>122:
                current-=26
            if current<97:
                current+=26
            if current>96 and current<123:
                result+=chr(current)
    return result

def hexadecimal(string):
    result=""
    index=4
    while index<len(string):
        current=string[index]+string[index+1]
        current=int(current,16)
        if current>64 and current<91:
            current+=32
        result+=chr(current)
        index+=3
    return result

#----------------------------------------------------------

        
convert= {"":"",".-":"a","-...":"b","-.-.":"c","-..":"d",".":"e","..-.":"f","--.":"g",
          "....":"h","..":"i",".---":"j","-.-":"k",".-..":"l","--":"m","-.":"n","---":"o",
          ".--.":"p","--.-":"q",".-.":"r","...":"s","-":"t","..-":"u","...-":"v",".--":"w",
          "-..-":"x","-.--":"y","--..":"z",".---":"1","..---":"2","...--":"3","....-":"4",
          ".....":"5","-....":"6","--...":"7","---..":"8","----.":"9","-----":"0","..--..":"?",
          "-.-.--":"!",".-.-.-":".","--..--":",","-.-.-.":";","---...":":",".-.-.":"+",
          "-....-":"-","-..-.":"/","-...-":"=","-.--.":"(","-.--.-":")",".----.":"'",".-..-.":'"'}        
    

folder_to_read = sys.argv[1]
folder_to_write = sys.argv[2]

try:
    os.mkdir(folder_to_write)
except OSError:
    print("")


for filename in os.listdir(folder_to_read):
    if filename.endswith(".txt"):


        code=open(folder_to_read+"/"+filename).read()

        #determining the decryption
        if code[0]=="m" or code[0]=="M":
            output=(morse(code))
        elif code[0]=="c" or code[0]=="C":
            output=(caesar(code))
        elif code[0]=="h" or code[0]=="H":
            output=(hexadecimal(code))

        result=open(folder_to_write+"/"+filename[0:-4]+"_b78373dm.txt","w")

        result.write(output)




    


