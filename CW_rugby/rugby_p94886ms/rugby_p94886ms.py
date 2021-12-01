#Rugby Project

import os



# t = 5 points (Try)
# c = 2 points (Goal kick)
# p = 3 points (Penalty)
# d = 3 points (Drop goal)

t,c,p,d = 5,2,3,3

T1Total, T2Total = 0,0

scores = open("rugby_file.txt", "r")


u = scores.read(3)
v = scores.read(3)
w = scores.read(3)
x = scores.read(3)
y = scores.read(3)
z = scores.read(3)

if "T1t" in u:
	T1Total = T1Total + t

if "T1c" in u:
	T1Total = T1Total + c

if "T1p" in u:
	T1Total = T1Total + p 

if "T1d" in u:
	T1Total = T1Total + d


if "T1t" in v:
	T1Total = T1Total + t

if "T1c" in v:
	T1Total = T1Total + c

if "T1p" in v:
	T1Total = T1Total + p 

if "T1d" in v:
	T1Total = T1Total + d


if "T1t" in w:
	T1Total = T1Total + t

if "T1c" in w:
	T1Total = T1Total + c

if "T1p" in w:
	T1Total = T1Total + p 

if "T1d" in w:
	T1Total = T1Total + d



if "T1t" in x:
	T1Total = T1Total + t

if "T1c" in x:
	T1Total = T1Total + c

if "T1p" in x:
	T1Total = T1Total + p 

if "T1d" in x:
	T1Total = T1Total + d



if "T1t" in y:
	T1Total = T1Total + t

if "T1c" in y:
	T1Total = T1Total + c

if "T1p" in y:
	T1Total = T1Total + p 

if "T1d" in y:
	T1Total = T1Total + d



if "T1t" in z:
	T1Total = T1Total + t

if "T1c" in z:
	T1Total = T1Total + c

if "T1p" in z:
	T1Total = T1Total + p 

if "T1d" in z:
	T1Total = T1Total + d

##########################################

if "T2t" in u:
	T2Total = T2Total + t

if "T2c" in u:
	T2Total = T2Total + c

if "T2p" in u:
	T2Total = T2Total + p 

if "T2d" in u:
	T2Total = T2Total + d


if "T2t" in v:
	T2Total = T2Total + t

if "T2c" in v:
	T2Total = T2Total + c

if "T2p" in v:
	T2Total = T2Total + p 

if "T2d" in v:
	T2Total = T2Total + d


if "T2t" in w:
	T2Total = T2Total + t

if "T2c" in w:
	T2Total = T2Total + c

if "T2p" in w:
	T2Total = T2Total + p 

if "T2d" in w:
	T2Total = T2Total + d



if "T2t" in x:
	T2Total = T2Total + t

if "T2c" in x:
	T2Total = T2Total + c

if "T2p" in x:
	T2Total = T2Total + p 

if "T2d" in x:
	T2Total = T2Total + d



if "T2t" in y:
	T2Total = T2Total + t

if "T2c" in y:
	T2Total = T2Total + c

if "T2p" in y:
	T2Total = T2Total + p 

if "T2d" in y:
	T2Total = T2Total + d



if "T2t" in z:
	T2Total = T2Total + t

if "T2c" in z:
	T2Total = T2Total + c

if "T2p" in z:
	T2Total = T2Total + p 

if "T2d" in z:
	T2Total = T2Total + d


results = open("rugby_file_p94886ms", "w")
results.write (str(T1Total)+":"+str(T2Total))

scores.close
results.close
