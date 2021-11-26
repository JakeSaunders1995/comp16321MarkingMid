import argparse
import os

morsedic = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.' 
        }
morsedict = {value:key for key,value in morsedic.items()}

#Hex Code
def hexdecode(value):
    hexv= bytes.fromhex(value).decode('utf-8')
    return hexv
    
    


#Morse Code
def morse_decode(value):
    message = value             
    temp = []
    letter = []
    a = -1
    for i in message.split(' '):
        a += 1
        letter += [i.split('/')]
        for k in range(len(letter[a])):
            temp += morsedict.get(letter[a][k], '')
        temp += ' '
    final_word = ""
    q = ""

    x = ''.join(temp)
    y = x.split("  ")
    for words in y :
        letters = words.split()
        q = ''.join(letters)
        final_word = final_word + q + " "
    return final_word.lower()


#Caeser Code
def caeser_decode(value):
    engval = ""

    for character_ref in value:
        #for upper case alphabets
        if character_ref.isupper(): 

                c_index = ord(character_ref) - ord('A')

                # shift chars
                c_initial_pos = (c_index - 3) % 26 + ord('A')

                c_initial = chr(c_initial_pos)

                engval += c_initial
        #for lower case 
        elif character_ref.islower(): 

                c_index = ord(character_ref) - ord('a') 

                c_initial_pos = (c_index - 3) % 26 + ord('a')

                c_initial = chr(c_initial_pos)

                engval += c_initial
        #for numbers
        elif character_ref.isdigit():
                
                c_initial = (int(character_ref) - 3) % 10

                engval += str(c_initial)

        elif character_ref == " ":

                # for spaces 
                engval += character_ref

    return engval

n = 0

if __name__ == "__main__" :
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="Enter input folder name")
    parser.add_argument("output_file", help="Enter output folder name")
    args = parser.parse_args()
    folder = str(args.input_file)
    outfolder = str(args.output_file)
    files = os.listdir(folder)
    files.sort()
    
    for filename in files:
        file = os.path.join(folder, filename)
        
        openfile = open(file, "r")
        newval = openfile.read()
        value = newval
        #filtering list
        finval = value.split(":")      
        if finval[0] == "Hex":
            del finval[0]
            value = ' '.join(finval)
            outval = hexdecode(value)

        if finval[0] == "Caesar Cipher(+3)":
            del finval[0]
            value = ' '.join(finval)
            outval = caeser_decode(value)
            
        if finval[0] == "Morse Code":
            del finval[0]
            value = ' '.join(finval)
            outval = morse_decode(value)

        out_name = files[n]
        out_name = out_name.replace(".txt", "_f06903rd.txt")
        final_out = os.path.join(outfolder, out_name)
        out_open = open(final_out, "w")
        out_open.write(outval)    
        n += 1