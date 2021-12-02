import os
import sys

eng_path = sys.argv[1]
lopala = sys.argv[2]
baita = sys.argv[3]

file = os.listdir(lopala)

for each in range (len(file)):
      to_open = lopala +"\\" + file[each]
      filename, file_extension = os.path.splitext(to_open)
      
      if file_extension == ".txt":
            f = open(to_open, "r")
            data = f.read()

            #Formatting
            
            punctuation = ['.', '?', '!', ',', ';', ':', '-', '_', '(', ')', '{', '}', 
                           '[', ']', "'", '"', '…', '/','`' ]
            sentence = ""
            p_count = 0
            u_count = 0
            d_count = 0 
            for word in data:
                  if word in punctuation:
                        p_count +=1
                  elif word.isupper():
                        u_count +=1
                        sentence += word.lower()
                  elif word.isdigit():
                        d_count +=1
                  else:
                        sentence += word

           
            file2 = open(eng_path, "r")
            english = file2.read().split('\n')
            
            
            #spellcheck
            
            wrong_count = 0
            t_count= 0
            split = sentence.split(" ")

            while '' in split:
                  split.remove('')
                  
            
            for i in split:
                  if i != '\n':
                        t_count+=1
                        if i not in english:
                              wrong_count +=1
            
            
            result1 =[ "e41002vg \n", "Formatting ################### \n","Number of upper case letters changed: ",str(u_count) ,"\n",
            "Number of punctuations removed: ", str(p_count), "\n",
            "Number of numbers removed: ", str(d_count), "\n" ]
            result2 = ["Spellchecking ################### \n","Number of words: ", str(t_count),"\n", 
            "Number of correct words: ", str(t_count-wrong_count), "\n",
            "Number of incorrect words: ", str(wrong_count)]
            
            
            out_file = baita + "\\" + file[each].replace(".txt", "_") + "e41002vg" + ".txt"
            f_output = open(out_file, "w")
            f_output.writelines(result1)
            f_output.writelines(result2)
            file2.close()
            f_output.close()
            f.close()