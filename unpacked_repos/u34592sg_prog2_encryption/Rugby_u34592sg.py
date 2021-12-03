### Rugby Score Keeper ###
import sys
import os
import re
t = 5 
c = 2 
p = 3 
d = 3
info = sys.argv[1]
oufo = sys.argv[2]
list1 = os.listdir(info)
with os.scandir(info) as entries:
  for i in entries:
    T1_score = 0
    T2_score = 0
    file_object = open(i , "r")
    st = os.path.basename(i)[:-4]
    fw = open(oufo + "/" + st + "_u34592sg.txt" , "w")
    file_contents = file_object.read()
    scores = []
    x= re.split(r"[a-z]", file_contents)
    x.remove('')
    for i in file_contents:
      if i.islower() == True:
        scores.append(i)

    for i in range(len(x)):
      if x[i] == "T1" and scores[i] == "t":
        T1_score += 5
      elif x[i] == "T1" and scores[i] == "c":
        T1_score += 2
      elif x[i] == "T1" and scores[i] == "p":
        T1_score += 3
      elif x[i] == "T1" and scores[i] == "d":
        T1_score += 3
      elif x[i] == "T2" and scores[i] == "t":
        T2_score += 5
      elif x[i] == "T2" and scores[i] == "c":
        T2_score += 2
      elif x[i] == "T2" and scores[i] == "p":
        T2_score += 3
      elif x[i] == "T2" and scores[i] == "d":
        T2_score += 3


        
        
    
    fw.write(str(T1_score) + ":" + str(T2_score))
    file_object.close()
    fw.close()

##    ouf.write(str(T1_score) + ":" + str(T2_score))
##    ouf.close()



