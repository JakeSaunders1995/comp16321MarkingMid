import sys
print(sys.argv)
test = open(sys.argv[1] , "r")
oku = test.readline()


if int(oku[1]) == 1 :
	if str(oku[2]) == "t":
		result11 = 5
	if str(oku[2]) == "c":
		result11 = 2
	if str(oku[2]) == "p":
		result11 = 3
	if str(oku[2]) == "d":
		result11 = 3
else :
	result11 = 0


if int(oku[1]) == 2 :
	if str(oku[2]) == "t":
		result21 = 5
	if str(oku[2]) == "c":
		result21 = 2
	if str(oku[2]) == "p":
		result21 = 3
	if str(oku[2]) == "d":
		result21 = 3
else :
	result21 = 0

if int(oku[4]) == 1 :
	if str(oku[5]) == "t":
		result12 = 5
	if str(oku[5]) == "c":
		result12 = 2
	if str(oku[5]) == "p":
		result12 = 3
	if str(oku[5]) == "d":
		result12 = 3
else :
	result12 = 0

if int(oku[4]) == 2 :
	if str(oku[5]) == "t":
		result22 = 5
	if str(oku[5]) == "c":
		result22 = 2
	if str(oku[5]) == "p":
		result22 = 3
	if str(oku[5]) == "d":
		result22 = 3
else :
	result22 = 0

if int(oku[7]) == 1 :
	if str(oku[8]) == "t":
		result13 = 5
	if str(oku[8]) == "c":
		result13 = 2
	if str(oku[8]) == "p":
		result13 = 3
	if str(oku[8]) == "d":
		result13 = 3
else :
	result13 = 0

if int(oku[7]) == 2 :
	if str(oku[8]) == "t":
		result23 = 5
	if str(oku[8]) == "c":
		result23 = 2
	if str(oku[8]) == "p":
		result23 = 3
	if str(oku[8]) == "d":
		result23 = 3
else :
	result23 = 0

if int(oku[10]) == 1 :
	if str(oku[11]) == "t":
		result14 = 5
	if str(oku[11]) == "c":
		result14 = 2
	if str(oku[11]) == "p":
		result14 = 3
	if str(oku[11]) == "d":
		result14 = 3
else :
	result14 = 0

if int(oku[10]) == 2 :
	if str(oku[11]) == "t":
		result24 = 5
	if str(oku[11]) == "c":
		result24 = 2
	if str(oku[11]) == "p":
		result24 = 3
	if str(oku[11]) == "d":
		result24 = 3
else :
	result24 = 0

if int(oku[13]) == 1 :
	if str(oku[14]) == "t":
		result15 = 5
	if str(oku[14]) == "c":
		result15 = 2
	if str(oku[14]) == "p":
		result15 = 3
	if str(oku[14]) == "d":
		result15 = 3
else :
	result15 = 0

if int(oku[13]) == 2 :
	if str(oku[14]) == "t":
		result25 = 5
	if str(oku[14]) == "c":
		result25 = 2
	if str(oku[14]) == "p":
		result25 = 3
	if str(oku[14]) == "d":
		result25 = 3
else :
	result25 = 0

sum1 = result11 + result12 + result13 + result14 + result15
sum2 = result21 + result22 + result23 + result24 + result25

print(sum1 , ":" , sum2)
f = open(sys.argv[2],"a")
f.write('{}:{}'.format(sum1  , sum2))
f.close()


