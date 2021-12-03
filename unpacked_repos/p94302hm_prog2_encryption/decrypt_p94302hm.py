import sys, os

inputfolder = sys.argv[1]
os.chdir(inputfolder)

for file in os.listdir():
    if file.endswith(".txt"):
        filepath = f"{inputfolder}/{file}"
        inputcipher = open(filepath, "r")
        cipher = inputcipher.read()
        inputcipher.close()

    encryptionMethod = cipher.split(":")[0]
    ciphertext = cipher.split(":")[1]

    if (encryptionMethod == "Morse Code"):
        morse = {
            "a":".-", "b":"-...", "c":"-.-.", "d":"-..", "e":".",
            "f":"..-.", "g":"--.", "h":"....", "i":"..", "j":".---",
            "k":"-.-", "l":".-..", "m":"--", "n":"-.", "o":"---",
            "p":".--.", "q":"--.-", "r":".-.", "s":"...", "t":"-",
            "u":"..-", "v":"...-", "w":".--", "x":"-..-", "y":"-.--",
            "z":"--..", " ":"/"
        }
        ciphertextMorse = ciphertext.split()
        for i in range(len(ciphertextMorse)):
            for letter in morse:
                if (ciphertextMorse[i] == morse[letter]):
                    ciphertextMorse[i] = letter
        ciphertext = "".join(ciphertextMorse)

    elif (encryptionMethod == "Caesar Cipher(+3)"):
        result = ""
        for i in range(len(ciphertext)):
            char = ciphertext[i]
            if (char == " "):
                result += " "
            else:
                result += chr((ord(char) - 3 - 97) % 26 + 97)
        ciphertext = result

    elif (encryptionMethod == "Hex"):
        ciphertextHex = ciphertext.split()
        result = ""
        for i in range(len(ciphertextHex)):
            result += bytes.fromhex(ciphertextHex[i]).decode("utf-8")
        ciphertext = result.lower()

    outputfolder = sys.argv[2]
    outputresult = open(outputfolder+file[:-4]+"_p94302hm.txt", "w")
    outputresult.write(ciphertext)
