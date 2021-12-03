import sys
import os

def dcrypt(input_file,output_folder,txtfile):
    text_out=""
    f_in=open(input_file,'r')
    for line in f_in:
        y=line.split(':')

    if y[0][0].lower()=='h':
        bytes_obj=bytes.fromhex(y[1])
        text_out=bytes_obj.decode("ASCII").lower()
        if '\n' in y[1]:
            text_out+='\n'

    elif y[0][0].lower()=='c':
        calpha="abcdefghijklmnopqrstuvwxyz"
        text_out=""
        for i in y[1]:
            if i==" ":
                text_out+=i
            elif '\n' in i:
                text_out+='\n'
            else:
                indexval=calpha.find(i.lower())
                indexval-=3
                text_out+=calpha[indexval]

    elif y[0][0].lower()=='m':
        text_out=""
        morsedict={'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0', '--..--': ', ', '.-.-.-': '.', '..--..': '?', '-..-.': '/', '-....-': '-', '-.--.': '(', '-.--.-': ')', '/': ' ','.-...':'&','---...':':','-.-.-.':';','..--.-':'_','-...-':'=','.-.-.':'+','...-..-':'$','.--.-.':'@'}

        for i in y[1].split(sep=' '):
            if i=='':
                continue
            elif '\n' in i:
                text_out+=morsedict[i[:-1]].lower()+"\n"
            else:
                text_out+=morsedict[i].lower()
    else:
        pass
    f_in.close()

    output_file=output_folder+"/"+txtfile[:-4]+"_s63644vb.txt"
    f_out=open(output_file,'w')
    f_out.write(text_out)
    f_out.close()

arg_list=(sys.argv)
parent_path=os.getcwd()
input_folder= arg_list[1]
output_folder= arg_list[2]

os.chdir(input_folder)
for txtfile in os.listdir():
    if txtfile.endswith(".txt"):
        os.chdir(parent_path)
        input_file=f"{input_folder}/{txtfile}"
        dcrypt(input_file,output_folder,txtfile)