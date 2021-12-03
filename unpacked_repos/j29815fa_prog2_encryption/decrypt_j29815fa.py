import os
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("input")
parser.add_argument("output")

args = parser.parse_args()

morse_codes = [[" ", "/"], ["a",".-"], ["b","-..."], ["c","-.-."], 
                ["d","-.."], [ "e","."], ["f","..-."], 
                ["g","--."], ["h","...."], ["i",".."], 
                ["j",".---"], ["k","-.-"], ["l",".-.."], 
                ["m","--"], ["n","-."], ["o","---"], 
                ["p",".--."], ["q","--.-"], ["r",".-."], 
                ["s","..."], ["t","-"], ["u","..-"], 
                ["v","...-"], ["w",".--"], ["x","-..-"], 
                ["y","-.--"], ["z","--.."], ["1",".----"], 
                ["2","..---"], ["3","...--"], ["4","....-"], 
                ["5","....."], ["6","-...."], ["7","--..."], 
                ["8","---.."], ["9","----."], ["0","-----"]]

for file in sorted(os.listdir(args.input)):
    with open(args.input + "/" + file, "r") as f1:
        encrypted_string = f1.read()
        decrypted_string = ""
        if "Hex" in encrypted_string:
            encrypted_string = encrypted_string.replace("Hex:", "")
            decrypted_string = bytearray.fromhex(encrypted_string).decode().lower()
        elif "Caesar Cipher(+3)" in encrypted_string:
            encrypted_string = encrypted_string.replace("Caesar Cipher(+3):", "")
            for char in encrypted_string:
                if char.isalpha():
                    if ord(char) - 3 < 97:
                        decrypted_string += chr(ord(char) - 3 + 26).lower()
                    else:
                        decrypted_string += chr(ord(char) - 3).lower()
                elif char == " ":
                    decrypted_string += " "
        elif "Morse Code" in encrypted_string:
            encrypted_string = encrypted_string.replace("Morse Code:", "")
            list_of_strings = encrypted_string.split(" ")
            for item in list_of_strings:
                for code in morse_codes:
                    if item.replace("\n", "") == code[1]:
                        decrypted_string += code[0]

        with open(args.output + "/" + file.replace(".txt", "") + "_j29815fa.txt", "w") as f2:
            f2.write(decrypted_string)
