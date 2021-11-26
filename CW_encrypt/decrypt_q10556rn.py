import sys
import os

input_direct = sys.argv[1]
output_direct = sys.argv[2]

morse_to_plain = {".-": "a", "-...": "b", "-.-.": "c", "-..": "d", ".": "e","..-.": "f", "--.": "g", "....": "h", "..": "i", ".---": "j", "-.-": "k", ".-..": "l",
"--": "m", "-.": "n", "---": "o", ".--.": "p", "--.-": "q", ".-.": "r", "...": "s", "-": "t", "..-": "u", "...-": "v", ".--": "w", "-..-": "x", "-.--": "y", "--..": "z",
".----":"1","..---":"2","...--":"3","....-":"4",".....":"5","-....":"6","--...":"7","---..":"8","----.":"9", "-----":"0"}

alphabet = "xyzabcdefghijklmnopqrstuvwxyz"

filenames = os.listdir(input_direct)
for filename in filenames:

  with open(os.path.join(input_direct,filename),'r') as i:
    lines = i.readlines()
  filename =  filename[:-4] + "_q10556rn.txt"
  plaintext = ""

  index = 0
  for line in lines:

    # this if statement performs decryption for morse code if 
    # file starts with a "M"
    if line[0] == "M":
      morsel = ""
      index += 11
      while index < len(line):
        while line[index] != "/":
          if line[index] == " ":
            plaintext += morse_to_plain[morsel]
            index += 1
            morsel = ""
          elif index == (len(line) -1):
            morsel += line[index]
            plaintext += morse_to_plain[morsel]
            break
          else:
            morsel += line[index]
            index += 1
        if line[index] == "/":
          plaintext += " "
        index += 2
    
    # this if statement performs decryption for caesar cipher if
    # file starts with a "C"
    elif line[0] == "C":
      ciphertext = ""
      plaintext = ""
      for i in range (18,len(line)):
        ciphertext += line[i]
      cipherpos = 0
      while(cipherpos < len(ciphertext)):
        if ciphertext[cipherpos] in alphabet:
          alphabetpos = 3
          while(ciphertext[cipherpos] != alphabet[alphabetpos]):
              alphabetpos += 1
          alphabetpos -= 3
          plaintext += alphabet[alphabetpos]
        else:
          plaintext += ciphertext[cipherpos]
        cipherpos+=1
    
    # this if statement performs decryption for hexadecimal if
    # file starts with a "H"

    elif line[0] == "H":
      hexnum = ""
      for i in range(4,len(line)):
        if line[i] == " " or i == (len(line) - 1):
          if i == (len(line)-1):
            hexnum += line[i]
          plaintext += chr(int(hexnum,16))
          hexnum = ""
        hexnum += line[i]

  with open(os.path.join(output_direct,filename),'w') as o:
      o.write(plaintext)

