import sys
import os
list_input=sys.argv
input_directory= sys.argv[1]
output_directory= sys.argv[2]
filenames=[]
outputpaths=[]
paths=[]
for entry in os.listdir(input_directory):
    if (entry.endswith(".txt")):
        path1=(os.path.join(input_directory,entry))
        paths.append(path1)
        filename= entry.split(".")[0]
        outputfilename=filename+"_e18770as.txt"
        outputpath=(os.path.join(output_directory,outputfilename))
        outputpaths.append(outputpath)
        filenames.append(filename)

length=len(filenames)

for i in range(length):
    input_file=paths[i]
    output_file=outputpaths[i]
    fin= open(input_file, "r")
    fout=open(output_file,"w")

    contents=fin.read()
    contents=contents.strip()
    list1=contents.split(":")
    char1=list1[0][0].lower()
    
    def morsecode():
        list2=list1[1].split()
        mor = {'.-': 'A',   '-...': 'B',   '-.-.': 'C','-..': 'D','.': 'E','..-.': 'F','--.': 'G',   '....': 'H',  '..': 'I','.---': 'J','-.-': 'K','.-..': 'L','--': 'M','-.': 'N','---':
            'O','.--.': 'P', '--.-': 'Q','.-.': 'R','...': 'S',  '-': 'T',    '..-': 'U', '...-': 'V','.--': 'W',   '-..-': 'X','-.--': 'Y',   '--..': 'Z',  '-----': '0','.----': '1',
            '..---': '2',  '...--': '3','....-': '4',  '.....': '5',  '-....': '6', '--...': '7',
               '---..': '8',  '----.': '9', "/": " ", ".-.-.-":".","--..--":",","..--..":"?",
            "-.-.-.":";" , "---...": ":","-..-.": "/", "-....-" :" -", ".----.":"'", ".-..-.":'"',
              "-.--.":"(", "-.--.-" :")", "-...-": "=", ".-.-.": "+",".--.-.": "@","-.-.--":"!", ".-...":"&",
               "..--.-":"_"}
        string1=""
        for i in list2:
            char=mor[i]
            string1+= char
        final_String=string1.lower()
        return(final_String)
            
    def hexa():
        string=bytes.fromhex(list1[1]).decode('ASCII')
        final_String=string.lower()
        return(final_String)

    def caesar():
        ciphertext=list1[1].lower()
        plainText= ''
        ciphertextPosition=0
        alphabet="xyzabcdefghijklmnopqrstuvwxyzabc"
        while (ciphertextPosition < len(ciphertext)):
            ciphertextChar= ciphertext[ciphertextPosition]
            if ciphertextChar in alphabet:
                alphabetPosition= 3

                while ciphertextChar != alphabet[alphabetPosition]:
                    alphabetPosition+= 1
                alphabetPosition-=3
                plainText= plainText + alphabet[alphabetPosition]

            else:
                plainText= plainText + ciphertextChar
            ciphertextPosition+=1


        return(plainText.lower())


    if char1=="h":
        answer=hexa()
    elif char1=="m":
        answer=morsecode()

    elif char1=="c":
        answer=caesar()

    fout.write(answer)


    fin.close()
    fout.close()
        
