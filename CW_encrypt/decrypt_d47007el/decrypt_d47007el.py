#Encryption
import argparse
import os

parser=argparse.ArgumentParser(description='Input File and output file')
parser.add_argument("source_file")
parser.add_argument("target_file")
args=parser.parse_args()

cwd=os.getcwd()
print(cwd)

input_file=args.source_file
print(input_file)

output_file=args.target_file
print(output_file)



dirs=os.listdir(input_file)
for file in dirs:

    decoded_message=""

    print(file)
    os.chdir(str(cwd)+"/"+str(input_file))
    encoded_message=open(file,"r")
    encoded_message=encoded_message.read()
    print(encoded_message)
    if encoded_message[0]=="H":
        encoded_message=encoded_message[4:]
        encoded_message=encoded_message.split()
        for i in range(0,len(encoded_message)):
            character=encoded_message[i]
            character=bytes.fromhex(character)
            character=character.decode("ASCII")
            character=character.lower()
            decoded_message=decoded_message+character

    elif encoded_message[0]=="C":
        encoded_message=encoded_message[18:]
        print(encoded_message)
        for i in range(0,len(encoded_message)):
            character=encoded_message[i]
            if character==" ":
                decoded_message=decoded_message+" "
            elif character.isalpha()==True:
                character=character.lower()
                character=ord(character)
                character=int(character)-3
                if character<97:
                    character=character+26
                character=chr(character)
                decoded_message=decoded_message+str(character)
    else:
        morse_code={".-":"a","-...":"b","-.-.":"c","-..":"d",".":"e","..-.":"f","--.":"g","....":"h","..":"i",".---":"j","-.-":"k",".-..":"l","--":"m","-.":"n","---":"o",".--.":"p","--.-":"q",".-.":"r","...":"s","-":"t","..-":"u","...-":"v",".--":"w","-..-":"x","-.--":"y","--..":"z","-----":"0",".----":"1","..---":"2","...--":"3","....-":"4",".....":"5","-....":"6","--...":"7","---..":"8","----.":"9",".-.-.-":".","--..--":",","..--..":"?",".----.":"'","-.-.--":"!","-..-.":"/","-.--.":"(","-.--.-":")",".-...":"&","---...":":","-.-.-.":";","-...-":"=",".-.-.":"+","-....-":"-","..--.-":"_",".-..-.":'"',"...-..-":"$",".--.-.":"@"}
        encoded_message=encoded_message[11:]
        encoded_message=encoded_message.split("/")
        for i in range(0,len(encoded_message)):
            word=encoded_message[i]
            word=word.split()
            for j in range(0,len(word)):
                character=word[int(j)]
                character=morse_code.get(character)
                decoded_message=decoded_message+str(character)
            decoded_message=decoded_message+" "


    os.chdir(str(cwd)+"/"+str(output_file))
    file=file[0:-4]
    print(file)
    file=str(file + "_d47007el.txt")
    file=open(file,"w")
    file.write(decoded_message)
    print(decoded_message)
