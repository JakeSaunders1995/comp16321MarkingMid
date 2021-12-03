import argparse
import os

if __name__ == "__main__" :
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="Enter input folder: ")
    parser.add_argument("output_file", help="Enter output folder: ")
    args = parser.parse_args()
    folder = str(args.input_file)
    outfolder = str(args.output_file)
    files = os.listdir(folder)

    print(files)

    for file in files:
        my_file = open(folder + "/" + file, "r")

        content = my_file.read()

        print(content)

        st = str(content)

        stp = st.split(':')
        
        print(stp)

        import string  


        
        
        
        temp = file.split(".")
        output_file_name = temp[0] + "_" + "j17768ms" + "." + temp[1]
        outputfile = open(outfolder + "/" + output_file_name, "w+")
        if stp[0] == "Hex":
                d1 = (stp[1])
                b = bytearray.fromhex(d1).decode()
                c = b.lower()
                print(c)
                outputfile.write(c)
        elif stp[0] == "Caesar Cipher(+3)":
                alphabet = string.ascii_lowercase

                encr= (stp[1]).strip()
                key = 3
                        
                g = ""

                for c in encr:

                    if c in alphabet:
                        position = alphabet.find(c)
                        new_position = (position - key) % 26
                        new_character = alphabet[new_position]
                        g += new_character
                    else:
                        g += c
                print(g)
                outputfile.write(g)
        elif stp[0] == "Morse Code":

            morse_to_eng = {
                '.-' : 'a', '-...' : 'b', '-.-.' : 'c', '-..' : 'd', '.' : 'e', '..-.' : 'f', '--.' : 'g', '....' : 'h', '..' : 'i', '.---' : 'j', '-.-' : 'k', '.-..' : 'l', '--' : 'm', '-.' : 'n', '---' : 'o', '.--.' : 'p', '--.-' : 'q', '.-.' : 'r', '...' : 's', '-' : 't', '..-' : 'u', '...-' : 'v', '.--' : 'w', '-..-' : 'x', '-.--' : 'y', '--..' : 'z', '.-.-.-' : '.', '..--..' : '?', '--..--' : ',', '/' : ' ', '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----'
            }
            w1 = (".... --- .-- . ...- . .-. / ... --- .-.. ...- .. -. --. / -- --- .-. ... . / -.-. --- -.. . / -- .- -.-- / -... . / - .... . / -- --- ... - / -.. .. ..-. ..-. .. -.-. ..- .-.. -")
            w2 = (" /")
            word= (w1+w2)
            mwrd = ""
            dwrd = ""
            for wrd in word:
                if (wrd!=' ' and wrd!="/"):
                    mwrd+=wrd
                    continue
                elif (wrd=='/'):
                    dwrd+=" "
                    mwrd=''
                elif (mwrd!=''):
                    dwrd+=morse_to_eng[mwrd]
                    mwrd=''
            ff =str(dwrd)
            outputfile.write(ff)