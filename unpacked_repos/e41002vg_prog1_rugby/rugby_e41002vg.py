#Program 1 : Rugby score tally
import sys
import os

infi = sys.argv[1]
outfi = sys.argv[2]
infi1 = os.listdir(infi)

for inside in range (len(infi1)):
      in_file = infi +"\\" + infi1[inside]
      filename, file_extension = os.path.splitext(in_file)
      
      if file_extension == ".txt" :
            f = open(in_file, "r")
            data = f.read()
            points = data.split('T')
            
            if "" in points:
                  points.remove("")
            team1 =[]
            team2 = []
            
            for i in points:
                  if i[0] == '1':
                        team1.append(i)      
                  elif i[0]== '2':
                        team2.append(i)
                        
            def calc(L):
                  total = 0
                  for i in L:
                        if i[1]== 't':
                              total = total + 5
                        elif i[1] == 'c':
                              total = total + 2
                        elif i[1] == 'p' or 'd':
                              total = total + 3
                        else:
                              print("invalid input")
                  return total
            
            T1= str(calc(team1))
            T2= str(calc(team2))
            result = T1 +":"+ T2
            
            out_file = outfi + "\\" + infi1[inside].replace(".txt", "_") + "e41002vg" + ".txt"
            f_output = open(out_file, "w")
            f_output.write(result)
            f_output.close()
            f.close()
