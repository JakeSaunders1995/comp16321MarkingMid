import os
import sys
import re
import contextlib

file1 = sys.argv[1]
file2 = sys.argv[2]

# sys.stdin = open(file2, "r")
# data = sys.stdin.read()
# sys.stdout = open(file2, "w")
# print(data)
with open(file1, "r") as fin:
	data = fin.read()
	n=3
	out = [(data[i:i+n]) for i in range(0, len(data), n)] #list data
	score = {'t','c','d','p'}
	dic= {'t':'5', 'c':'','p':'3','d':'2'}
	reOut1 = ''
	reOut2 =''
	has_one = [one for one in out if '1' in one]
	has_two = [two for two in out if '2' in two] #to seperate group
	str1 = ''.join(has_one)
	str2= ''.join(has_two)
	remove_nameGroup1 = str1.replace('T1','')
	remove_nameGroup2 = str2.replace('T2','')
	for i in remove_nameGroup1:
		if i in dic:
			sc = dic[i]
			reOut1=reOut1+sc
	sum_of_score1 = 0
	for digit in reOut1:
		sum_of_score1+=int(digit)

	for i in remove_nameGroup2:
		if i in dic:
			sc2 = dic[i]
			reOut2=reOut2+sc2
	sum_of_score2 = 0
	for digit in reOut2:
		sum_of_score2+=int(digit)
	ratio=str(sum_of_score1)+':'+str(sum_of_score2)
	

with open(file2, "w") as fout:
	with contextlib.redirect_stdout(fout):
		print(ratio)