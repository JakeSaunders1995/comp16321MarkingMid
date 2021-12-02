import os, sys, re
import string as strin

inputoutput = sys.argv

wordspath = sys.argv[1]
inpath = sys.argv[2]
outpath = sys.argv[3]


os.chdir(wordspath)

for file in os.listdir():
	if file.endswith('.txt'):
		with open(f'{file}', "r") as f:
			listowords = f.read()
		
os.chdir(inpath)
print(os.getcwd())
for file in os.listdir():
	temp = ''
	if file.endswith('.txt'):
		with open(f'{file}', "r") as f:
			text = f.read()
			frmt = text.lower()
			string = re.sub('[^A-Za-z ]+', '', frmt)
			lis = string.split()
			n = 0
			for i in lis:
				if i in listowords:
					n += 1
			print(n)
			print(len(lis))
			up = 0
			punc = 0
			num = 0
			for i in text:
				if i.isupper() == True:
					up += 1 
				elif i in strin.punctuation:
					punc += 1
				elif i.isdigit() == True:
					num += 1
					print(i)
			print(num)
			print(up)
			print(punc)
		os.chdir(outpath)
		with open(f'{file} g28708at', "w") as f:
			f.write('g28708at')
			f.write('\n')
			f.write('Formatting ###################')
			f.write('\n')
			f.write(f'Number of upper case letters changed: {up}')
			f.write('\n')
			f.write(f'Number of punctuations removed: {punc}')
			f.write('\n')
			f.write(f'Number of numbers removed: {num}')
			f.write('\n')
			f.write('Spellchecking ###################')
			f.write('\n')
			f.write(f'Number of words: {len(lis)}')
			f.write('\n')
			f.write(f'Number of correct words: {n}')
			f.write('\n')
			f.write(f'Number of incorrect words: {len(lis) - n}')



	







