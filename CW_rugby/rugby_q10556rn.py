
import sys
import os

input_direct = sys.argv[1]
output_direct = sys.argv[2]


filenames = os.listdir(input_direct)

for filename in filenames:

  with open(os.path.join(input_direct,filename),'r') as i:
      lines = i.readlines()
  filename =  filename[:-4] + "_q10556rn.txt"

  scores = [0,0]

  for line in lines:
      index = 1
      while index <= len(line):                            
        team = int(line[index]) -1
        scoretype = line[index + 1]
        if scoretype == "t":
          scores[team] += 5
        elif scoretype == "c":
          scores[team] += 2
        elif scoretype == "p":
          scores[team] += 3
        elif scoretype == "d":
          scores[team] += 3
        index +=3

  if scores[0] > scores[1]:
    print("Team 1 is the winner for " + filename[:-13] + "!")
  elif scores[0] < scores[1]:
    print("Team 2 is the winner for " + filename[:-13] + "!")
  else:
    print("It's a draw for " + filename[:-13] + "!")

  with open(os.path.join(output_direct,filename),'w') as o:
      o.write(str(scores[0]) + ":" + str(scores[1])) 



