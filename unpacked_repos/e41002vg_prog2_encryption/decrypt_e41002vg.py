#Program 2: encryption program
import os
import sys

andar = sys.argv[1]
bahar = sys.argv[2]
file = os.listdir(andar)

for each in range (len(file)):
      to_open = andar +"\\" + file[each]
      filename, file_extension = os.path.splitext(to_open)
      
      if file_extension == ".txt":

            f = open(to_open, "r")
            data = f.read()
            sp = data.split(":")
            
            def hexa():
                  sp = data.split(":")
                  deci_list = []
                  alpha_list = []
           
                  hexa_list = sp[1].split(' ')
                  for element in hexa_list:
                        deci = int(element, 16)
                        deci_list.append(deci)
                  for letter in deci_list:
                        alpha = chr(letter)
                        alpha_list.append(alpha)
                  result = ''.join(alpha_list)
                  return result.lower()
                 
                        
            def ceaser ():
                  
                  main = sp[1]
                  decrypted = ""
                  for letter in main:
                      if letter.isalpha(): 
                          letter = letter.lower()
                          cur_pos = ord(letter) - ord('a')
                          og_pos = (cur_pos - 3) % 26 + ord('a')
                          actual_letter = chr(og_pos)
                          decrypted += actual_letter
                      else:
                          decrypted += letter
                  return decrypted
            def morse():
                  morse_code = ""
                  morse_dict = { 'A':'.-', 'B':'-...',
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
                                '(':'-.--.', ')':'-.--.-', ' ': '/',
                                '!':'-.-.--', ';': '-.-.-.', ':' : '---...',
                                "'": '.---.', '"' : '.-..-.'}
                  
                  thingy = sp[1].split(" ")
                  for i in thingy:
                        for key in morse_dict:
                              if i == morse_dict[key]:
                                    morse_code += key
                              else:
                                    continue
                  return morse_code.lower()
                  
            if sp[0][0].upper() == "H":
                  result = hexa()
            elif sp[0][0].upper() == "C" :
                  result = ceaser()
            elif sp[0][0].upper() == "M":
                  result = morse()
            else:
                  print("cannot identify cipher, try another file")
            out_file = bahar + "\\" + file[each].replace(".txt", "_") + "e41002vg" + ".txt"
            f_output = open(out_file, "w")
            try:
                  f_output.write(result)
                  f_output.close()
                  f.close()
            except NameError: 
                  print("Error : please enter correct filepath")