import os,sys

#function for error message when the arguments are not right
def print_help_and_exit():
    print("Usage: " + sys.argv[0] + " [input folder] [output folder]")
    sys.exit(0)

#code for caesar cipher +3 to text
def caesar_cipher(alpha):
    wording=""
    up=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    lo=['x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w']
    for each in alpha:
        if each==' ':
            wording=wording+each
        else:
            a=up.index(each)
            b=lo[a]
            wording=wording+str(b)
    return wording

#code for hex to text
def hexa(beta):
    beta=beta.replace(" ","")
    l=len(beta)
    ct=0
    wording=""
    while ct<l:
        a=beta[ct]
        b=beta[ct+1]
        c=a+b
        A=int(c,16)
        B=chr(A)
        wording=wording+B
        ct+=2
    return wording

#code for morse code to text
def morse_code(gamma):
    wording=""
    small=gamma.split('/')
    l1=['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.', '-----', '--..--', '.-.-.-', '..--..', '-..-.', '-....-', '-.--.', '-.--.-']
    lett=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0',',','.','?','/','-','(',')']
    for s in small:
        sp=s.split(' ')
        for l in sp:
            if l in l1:
                ind=l1.index(l)
                ch=lett[ind]
                wording=wording+str(ch)
        wording=wording+' '        
    return wording


#encryption program
def encryption(input_folder, output_folder, filename):
    f1=open(input_folder + filename,"r")
    f2=open(output_folder + filename.replace(".txt","_p98424rp.txt") ,"w")
    cont=f1.read()
    para=cont.split(":")
    word=para[1]

    if para[0]=="Morse Code":
        decrypt=morse_code(word)
        f2.write(decrypt)

    elif para[0]=="Caesar Cipher(+3)":
        decrypt=caesar_cipher(word)
        f2.write(decrypt)

    elif para[0]=="Hex":
        decrypt=hexa(word)
        f2.write(decrypt)

    f2.close()
    f1.close()

#checks number of arguments
if(len(sys.argv) != 3):
    print("ERROR: incorrect number of arguments")
    print_help_and_exit()

#get the files
input_folder_string = sys.argv[1]
output_folder_string = sys.argv[2]

#gets the list of files in the given directory
dire=os.listdir(input_folder_string)

#skims through files only if it is a text file and executes the calculation part
for file in dire:
    if ".txt" in file:
        encryption(input_folder_string, output_folder_string, file)

