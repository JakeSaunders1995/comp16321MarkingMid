import re
#import os
import sys

filepath = sys.argv[1]
outputpath = sys.argv[2]

with open(filepath, 'r') as fp:
	text= fp.readline()


scores = re.findall('...', text);

do = scores.count("T1d")
dt = scores.count("T2d")
to = scores.count("T1t")
tt = scores.count("T2t")
po = scores.count("T1p")
pt = scores.count("T2p")
co = scores.count("T1c")
ct = scores.count("T2c")



teamo = (do*3)+(to*5)+(po*3)+(co*2)
teamt = (dt*3)+(tt*5)+(pt*3)+(ct*2)

finalscore = (str(teamo) + ":" + str(teamt))

with open(outputpath, 'w') as fp:
	fp.write(finalscore)


