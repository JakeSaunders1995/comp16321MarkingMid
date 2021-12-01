import argparse 
import re

parser = argparse.ArgumentParser(description='calculate the score of two rugby teams')
parser.add_argument('input', type=str, help='input file path')
parser.add_argument('output', type=str, help='output file path')
args = parser.parse_args()

def readfile(inputpath):
	f=open(inputpath)
	global lines
	lines = f.read()
	f.close()
readfile(args.input)
print(lines)

def writeresult(outputpath):
	f = open(outputpath,'w')
	f.write(result)
	f.close

t1 = re.findall('T1.',lines)
t2 = re.findall('T2.',lines)
print(t1)
print(t2)

def countnumbert1(word):
	global i
	i = 0 
	times = 0
	while times < len(t1):
		if word == t1[times][2]:
			i+=1
			times +=1
		else:
			times +=1


socret1=0
countnumbert1('t')
socret1+=i*5
countnumbert1('c')
socret1+=i*2
countnumbert1('p')
socret1+=i*3
countnumbert1('d')
socret1+=i*3

def countnumbert2(word):
	global i
	i = 0 
	times = 0
	while times < len(t2):
		if word == t2[times][2]:
			i+=1
			times +=1
		else:
			times +=1

socret2=0
countnumbert2('t')
socret2+=i*5
countnumbert2('c')
socret2+=i*2
countnumbert2('p')
socret2+=i*3
countnumbert2('d') 
socret2+=i*3
result = str(socret1)+':'+str(socret2)
print(result)
if socret1 > socret2:
	print('T1 win')
elif socret1 < socret2:
	print('T2 win')
elif socret1 == socret2:
	print('Draw')	
writeresult(args.output)

