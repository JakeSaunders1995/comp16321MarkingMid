import os, re, string, sys

running_dir = __file__

main_dir, py_file =   os.path.split(running_dir)

start = sys.argv[1]
end = sys.argv[2]

input_dir = os.path.join( main_dir,start)
output_dir = os.path.join( main_dir,end)

list_file = os.listdir(input_dir)

for s in list_file:
    single_file = open(os.path.join( main_dir,start,s), "r", encoding='windows-1252')
    get_data = single_file.read()
    single_file.close()

    #identifying_algorithm
    algorithm = 0
    splitting= get_data.split(":")

    if splitting[0]== "Hex":
        algorithm = "hexadecimal"

    if splitting[0]== "Caesar Cipher(+3)":
        algorithm = "caesar"

    if splitting[0]== "Morse Code":
        algorithm = "morse"

    #Decoding depending on algorithm
    import codecs
    if algorithm == "hexadecimal":
       splitting[1]= splitting[1].replace(" ", "")
       decoding= codecs.decode(str(splitting[1]), "hex").decode('utf-8')
       plaintext=decoding.lower()
       
    
    if algorithm == "caesar":
       alphabet = "xyzabcdefghijklmnopqrstuvw"
       plaintext=""
       digits="0981234567"
       for word in splitting[1].split():
         for i in word:
            if i in "0123456789":
                cipherTextposition= digits.index(i)
                plaintext= plaintext+digits[cipherTextposition-3]
            else:
                cipherTextposition= alphabet.index(i)
                plaintext=plaintext+alphabet[cipherTextposition-3]
         plaintext= plaintext+" "
   
    if algorithm == "morse":
        morse_dict= { 'A':'.-', 'B':'-...', 
                     'C':'-.-.', 'D':'-..', 'E':'.', 
                     'F':'..-.', 'G':'--.', 'H':'....', 
                     'I':'..', 'J':'.---', 'K':'-.-', 
                     'L':'.-..', 'M':'--', 'N':'-.', 
                     'O':'---', 'P':'.--.', 'Q':'--.-', 
                     'R':'.-.', 'S':'...', 'T':'-', 
                     'U':'..-', 'V':'...-', 'W':'.--', 
                     'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                     '1':'.----', '2':'..---', '3':'...--', 
                     '4':'....-', '5':'.....', '6':'-....', 
                     '7':'--...', '8':'---..', '9':'----.', 
                     '0':'-----'} 

        to_be_decoded=splitting[1]
        to_be_decoded= to_be_decoded.replace("/","")
        to_be_decoded= to_be_decoded+" "
        plaintext= ""
        ci=""

        for i in to_be_decoded:
            if (i !=" "):
              x=0
              ci= ci+i
            else:
              x=x+1
              if x==2:
                plaintext= plaintext+" "
              else:
                plaintext += list(morse_dict.keys())[list(morse_dict.values()).index(ci)] 
                ci = ""
                plaintext= plaintext.lower()
      

    new_s = s.replace('.txt', '_t02231ss.txt')
    
    target_output = open(os.path.join(output_dir, new_s),"wt")

    target_output.write(plaintext)
    target_output.close()
