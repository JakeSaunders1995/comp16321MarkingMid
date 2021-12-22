  
# str = "T1tT2tT2tT2pT2c"

 

import sys 
import os 

InFold = sys.argv[1] + "/test_file3.txt"
OutFold = sys.argv[2] + "/rugbyscores.txt"



readFile = open(InFold, "r")
inputCode = readFile.read()
   

score = inputCode
# score = "T1cT1pT2tT2tT1t"

score = score.replace("T", " ")


substring = score.count("")
team_1 = 0 
team_2 = 0

# for substring in score:
a = score.count("1t")
team_1 += int(a)*5

b = score.count("1c")
team_1 += int(b)*2

c = score.count("1p")
team_1 += int(c)*3

d = score.count("1d")
team_1 += int(d)*3

e = score.count("2t")
team_2 += int(e)*5

f = score.count("2c")
team_2 += int(f)*2

g = score.count("2p")
team_2 += int(g)*3

h = score.count("2d")
team_2 += int(h)*3



writeFile = open(OutFold, "w")
writeFile.write(str(team_1) + ":" + str(team_2))
writeFile.close









 
    
