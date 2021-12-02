import sys
import os

input_folder = sys.argv[1]
output_folder = sys.argv[2]

input_files = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]

morse_code = {
    ".-": "a", "-...": "b", "-.-.": "c", 
    "-..": "d", ".": "e","..-.": "f", 
    "--.": "g", "....": "h","..": "i", 
    ".---": "j", "-.-": "k",".-..": "l", 
    "--": "m", "-.": "n","---": "o", 
    ".--.": "p", "--.-": "q",".-.": "r", 
    "...": "s", "-": "t","..-": "u", 
    "...-": "v", ".--": "w","-..-": "x", 
    "-.--": "y", "--..": "z",".----": "1", 
    "..---": "2", "...--": "3","....-": "4", 
    ".....": "5", "-....": "6","--...": "7", 
    "---..": "8", "----.": "9","-----": "0", 
    "--..--": ",", ".-.-.-": ".","..--..": "?",
    ".-..-.": "\"", "---...": ":", ".----.": "'",
    "-....-": "-", "-.-.--": "!", ".-...": "&",
    "-.-.-.": ";", "-...-": "=", ".-.-.": "+",
    "..--.--": "_", "...-..-": "$", ".--.-.": "@",
    "-..-.": "/", "-....-": "-","-.--.": "(", 
    "-.--.-": ")", "/": " "
}

for input_file in input_files:
    f = open(os.path.join(input_folder, input_file))
    input_file_contents = f.read()
    f.close()

    method = input_file_contents.split(":")[0]
    ciphertext = input_file_contents.split(":")[1].lower()
    plaintext = ""

    if (method == "Hex"):
        for i in ciphertext.split(" "):
            plaintext += chr(int(i, 16))
    elif (method == "Caesar Cipher(+3)"):
        for c in ciphertext:
            a = ord(c)
            if ((a < ord("a")) or (a > ord("z"))):
                plaintext += c
            else:
                a -= 3
                if (a < ord("a")):
                    a += 26
                plaintext += chr(a)
    elif (method == "Morse Code"):
        for i in ciphertext.split(" "):
            plaintext += morse_code[i]

    plaintext = plaintext.lower()

    f = open(os.path.join(output_folder, f"{input_file.split('.txt')[0]}_y35654gw.txt"), "w")
    f.write(plaintext)
    f.close()