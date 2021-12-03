import argparse
import os

parser = argparse.ArgumentParser(description='Input and Output files')
parser.add_argument('input', type=str, help='Input file')
parser.add_argument('output', type=str, help='Output file')
args = parser.parse_args()


infile = args.input
outfile = args.output

def write_file(dir,file,output):
    if outfile[-1] == "/":
        out_name = outfile + x.split(".txt")[0] + "_g62520js.txt"
        output_file = out_name
        directory = os.path.dirname(outfile)
    else:
        out_name = outfile + "/" + x.split(".txt")[0] + "_g62520js.txt"
        output_file = out_name
        directory = os.path.dirname(output_file)
        #print(directory)


    if not os.path.exists(directory):
        os.makedirs(directory)

    final_dec = open(output_file, "w")
    final_dec.write(output)
    final_dec.close()


for x in os.listdir(infile):

    f = os.path.join(infile, x)
    dir_path = os.path.dirname(f)
    read_scores = open(f, "r")
    enc_file = read_scores.readline()
    file_split = enc_file.split(":")
    enc_type = file_split[0]
    enc_text = file_split[1]

    if enc_type.lower() == "caesar cipher(+3)":
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        enc_text_lower = enc_text.lower()
        final = ""
        key = 3

        for i in enc_text_lower:
            if i in alphabet:
                pos = alphabet.find(i)
                new_pos = (pos - key) % 26
                new_char = alphabet[new_pos]
                final += new_char
            else:
                final += i
        #print(final)
        write_file(outfile,x,final)




    elif enc_type.lower() == "hex":
        hex_dec = bytes.fromhex(enc_text).decode("ascii").lower()
        #print(hex_dec)
        write_file(outfile,x,hex_dec)

    elif enc_type.lower() == "morse code":
        morse_dict = {
    'A':'.-', 'B':'-...',
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
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-', ' ': '/', "@":".--.-."
}

        enc_text = file_split[1]
        split_enc = enc_text.split(" ")
        #print(split_enc)
        final = ""
        for y in split_enc:
            try:
                final += list(morse_dict.keys())[list(morse_dict
                    .values()).index(y)]
            except:
                final += y
        final_lower = final.lower()
        #print(final_lower)
        write_file(outfile,x,final_lower)
