import sys
import os



inputfolder = sys.argv[1]
outputfolder = sys.argv[2]


startdirectory = os.getcwd() + inputfolder.replace('.', '')
os.chdir(startdirectory)

for inputfile in os.listdir():
   file = open(inputfile, 'r')
   line = file.read().rstrip()
   algorithm,ciphertext = line.split(':', 1)

   if "+3" in algorithm:

      ciphertext = ciphertext.lower()  

      plaintext = ""
      ciphertextposition = 0
      alphabet = "xyzabcdefghijklmnopqrstuvwxyz"

      while (ciphertextposition < len(ciphertext)):

        ciphertextChar = ciphertext[ciphertextposition]
        alphabetposition = 3
        if ciphertextChar == " ":
            plaintext += " "
            ciphertextposition += 1
        else:

         while (ciphertextChar != alphabet[alphabetposition]):

           alphabetposition += 1

         alphabetposition = alphabetposition - 3
         plaintext += alphabet[alphabetposition]
         ciphertextposition += 1


      os.chdir('..')
      if not os.path.exists(os.getcwd()  + outputfolder.replace('.', '')):
         os.makedirs(os.getcwd()  + outputfolder.replace('.', ''))
         os.chdir(os.getcwd()  + outputfolder.replace('.', ''))

         f = open(inputfile + "_p80249ra.txt", 'w+')
         f.write(plaintext)
         f.close()
         os.chdir('..')
         os.chdir(startdirectory)
         print("DECRYPTED! outputted to the output folder")
         file.close()
      else:
        os.chdir(os.getcwd()  + outputfolder.replace('.', ''))

        f = open(inputfile + "_p80249ra.txt", 'w+')
        f.write(plaintext)
        f.close()
        os.chdir('..')
        os.chdir(startdirectory)
        print("DECRYPTED! outputted to the output folder")
        file.close()

   if "Morse" in algorithm: 
       morsetext = ciphertext

       morse_diction = {
       '.-' : 'a', '-...' : 'b', '-.-.' : 'c', '-..' : 'd', '.' : 'e', '..-.' : 'f', '--.' : 'g', '....' : 'h',  '..' : 'i', 
       '.---' : 'j', '-.-' : 'k', '.-..' : 'l', '--' : 'm', '-.' : 'n', '---' : 'o', '.--.' : 'p', '--.-' : 'q',
       '.-.' : 'r', '...' : 's', '-' : 't', '..-' : 'u', '...-' : 'v', '.--' : 'w', '-..-' : 'x', '-.--' : 'y', '--..' : 'z',  ' ' : '/'
       }

       morsetextlist = []
       result = []
       finalstring = ""
       morsetextlist = morsetext.split(" ")
       for m in morsetextlist:
          decryptedletter = morse_diction.get(m)
          result.append(decryptedletter)


       for i in result:      
           if i is None:
               i = " "
               finalstring = finalstring + str(i)
           else:
               finalstring = finalstring + str(i)


       os.chdir('..')
       if not os.path.exists(os.getcwd()  + outputfolder.replace('.', '')):
           os.makedirs(os.getcwd()  + outputfolder.replace('.', ''))
           os.chdir(os.getcwd()  + outputfolder.replace('.', ''))

           f = open(inputfile + "_p80249ra.txt", 'w+')
           f.write(finalstring)
           f.close()
           os.chdir('..')
           os.chdir(startdirectory)
           print("DECRYPTED! outputted to the output folder")
           file.close()
       else:
           os.chdir(os.getcwd()  + outputfolder.replace('.', ''))

           f = open(inputfile + "_p80249ra.txt", 'w+')
           f.write(finalstring)
           f.close()
           os.chdir('..')
           os.chdir(startdirectory)
           print("DECRYPTED! outputted to the output folder")
           file.close()

         






   if "Hex" in algorithm:
    
    hexcode = ciphertext
    hexcode = hexcode.replace(" ", "")
    decodedhex = bytearray.fromhex(hexcode).decode()

    os.chdir('..')
    os.chdir(os.getcwd()  + outputfolder.replace('.', ''))

    os.chdir('..')
    if not os.path.exists(os.getcwd()  + outputfolder.replace('.', '')):
           os.makedirs(os.getcwd()  + outputfolder.replace('.', ''))
           os.chdir(os.getcwd()  + outputfolder.replace('.', ''))

           f = open(inputfile + "_p80249ra.txt", 'w+')
           f.write(decodedhex)
           f.close()
           os.chdir('..')
           os.chdir(startdirectory)
           print("DECRYPTED! outputted to the output folder")
           file.close()
    else:
           os.chdir(os.getcwd()  + outputfolder.replace('.', ''))

           f = open(inputfile + "_p80249ra.txt", 'w+')
           f.write(decodedhex)
           f.close()
           os.chdir('..')
           os.chdir(startdirectory)
           print("DECRYPTED! outputted to the output folder")
           file.close()

   
   else:
     print("completed.")
     file.close()




   file.close()